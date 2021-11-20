import io
import asyncio
import contextlib
import zlib
import logging
from asyncio import StreamReader, StreamWriter, Queue, Task
from enum import Enum
from typing import List, Dict, Optional, AsyncIterator

from cryptography.hazmat.primitives.ciphers import CipherContext

from .mc import proto
from .mc.types import VarInt
from .mc.packet import Packet
from .mc.definitions import ConnectionState
from .util import encryption

LOGGER = logging.getLogger(__name__)


class InvalidState(Exception):
	pass

class ConnectionError(Exception):
	pass

_STATE_REGS = {
	ConnectionState.HANDSHAKING : proto.handshaking.clientbound.REGISTRY,
	ConnectionState.STATUS : proto.status.clientbound.REGISTRY,
	ConnectionState.LOGIN : proto.login.clientbound.REGISTRY,
	ConnectionState.PLAY : proto.play.clientbound.REGISTRY,
}

class Dispatcher:
	_down : StreamReader
	_reader : Optional[Task]
	_decryptor : CipherContext

	_up   : StreamWriter
	_writer : Optional[Task]
	_encryptor : CipherContext

	_dispatching : bool

	_incoming : Queue
	_outgoing : Queue

	_host : str
	_port : int

	proto : int
	state : ConnectionState
	encryption : bool
	compression : Optional[int]

	_logger : logging.Logger

	def __init__(self):
		self._prepare()

	@property
	def connected(self) -> bool:
		return self._dispatching

	async def write(self, packet:Packet, wait:bool=False) -> int:
		await self._outgoing.put(packet)
		if wait:
			await packet.processed.wait()
		return self._outgoing.qsize()

	async def packets(self, timeout=1) -> AsyncIterator[Packet]:
		while self.connected:
			try: # TODO replace this timed busy-wait with an event which resolves upon disconnection, and await both
				packet = await asyncio.wait_for(self._incoming.get(), timeout=timeout)
				try:
					yield packet
				finally:
					self._incoming.task_done()
			except asyncio.TimeoutError:
				pass # so we recheck self.connected

	def encrypt(self, secret:bytes):
		cipher = encryption.create_AES_cipher(secret)
		self._encryptor = cipher.encryptor()
		self._decryptor = cipher.decryptor()
		self.encryption = True
		self._logger.info("Encryption enabled")

	def _prepare(self, host:Optional[str] = None, port:Optional[int] = None, queue_timeout:int = 1, queue_size:int = 100):
		self._host = host or self._host or "localhost"
		self._port = port or self._port or 25565
		self._logger = LOGGER.getChild(f"@({self._host}:{self._port})")

		self.encryption = False
		self.compression = None
		self.state = ConnectionState.HANDSHAKING
		self.proto = 340 # TODO 

		# Make new queues, do set a max size to sorta propagate back pressure
		self._incoming = Queue(queue_size)
		self._outgoing = Queue(queue_size)
		self._dispatching = False
		self._reader = None
		self._writer = None

	async def connect(self,
			host : Optional[str] = None,
			port : Optional[int] = None,
			queue_timeout : int = 1,
			queue_size : int = 100
	):
		if self.connected:
			raise InvalidState("Dispatcher already connected")

		self._prepare(host, port, queue_timeout, queue_size)

		self._down, self._up = await asyncio.open_connection(
			host=self._host,
			port=self._port,
		)

		self._dispatching = True
		self._reader = asyncio.get_event_loop().create_task(self._down_worker())
		self._writer = asyncio.get_event_loop().create_task(self._up_worker(timeout=queue_timeout))
		self._logger.info("Connected")

	@classmethod
	def serve(cls,
			container : List[Dispatcher],
			host : Optional[str] = None,
			port : Optional[int] = None,
			queue_timeout : int = 1,
			queue_size : int = 100
	):
		async def _client_connected(reader:StreamReader, writer:StreamWriter):
			dispatcher = cls()
			container.append(dispatcher)
			dispatcher._prepare(host, port, queue_timeout, queue_size)
	
			dispatcher._down, dispatcher._up = reader, writer
			dispatcher._dispatching = True
			dispatcher._reader = asyncio.get_event_loop().create_task(dispatcher._down_worker())
			dispatcher._writer = asyncio.get_event_loop().create_task(dispatcher._up_worker(timeout=queue_timeout))
			dispatcher._logger.info("Serving client")
		return _client_connected

	async def disconnect(self, block:bool=True):
		self._dispatching = False
		if block and self._writer and self._reader:
			await asyncio.gather(self._writer, self._reader)
			self._logger.debug("Net workers stopped")
		if self._up:
			if not self._up.is_closing() and self._up.can_write_eof():
				try:
					self._up.write_eof()
				except OSError as e:
					self._logger.error("Could not write EOF : %s", str(e))
			self._up.close()
			if block:
				await self._up.wait_closed()
				self._logger.debug("Socket closed")
		self._logger.info("Disconnected")

	async def _read_varint(self) -> int:
		numRead = 0
		result = 0
		while True:
			data = await self._down.readexactly(1)
			if self.encryption:
				data = self._decryptor.update(data)
			buf = int.from_bytes(data, 'little')
			result |= (buf & 0b01111111) << (7 * numRead)
			numRead +=1
			if numRead > 5:
				raise ValueError("VarInt is too big")
			if buf & 0b10000000 == 0:
				break
		return result

	async def _down_worker(self):
		while self._dispatching:
			try: # these 2 will timeout or raise EOFError if client gets disconnected
				length = await self._read_varint()
				data = await self._down.readexactly(length)

				if self.encryption:
					data = self._decryptor.update(data)

				buffer = io.BytesIO(data)

				if self.compression is not None:
					decompressed_size = VarInt.read(buffer)
					if decompressed_size > 0:
						decompressor = zlib.decompressobj()
						decompressed_data = decompressor.decompress(buffer.read())
						if len(decompressed_data) != decompressed_size:
							raise ValueError(f"Failed decompressing packet: expected size is {decompressed_size}, but actual size is {len(decompressed_data)}")
						buffer = io.BytesIO(decompressed_data)

				packet_id = VarInt.read(buffer)
				cls = _STATE_REGS[self.state][self.proto][packet_id]
				packet = cls.deserialize(self.proto, buffer)
				self._logger.debug("[<--] Received | %s", str(packet))
				await self._incoming.put(packet)
				if self.state == ConnectionState.LOGIN:
					await self._incoming.join() # During login we cannot pre-process any packet, first need to maybe get encryption/compression
			except AttributeError:
				self._logger.debug("Unimplemented packet %d", packet_id)
			except asyncio.IncompleteReadError:
				self._logger.error("EOF from server")
				await self.disconnect(block=False)
			except Exception:
				self._logger.exception("Exception parsing packet %d | %s", packet_id, buffer.getvalue())

	async def _up_worker(self, timeout=1):
		while self._dispatching:
			try:
				packet = await asyncio.wait_for(self._outgoing.get(), timeout=timeout)
			except asyncio.TimeoutError:
				continue # check again self._dispatching

			try:
				buffer = packet.serialize()
				length = len(buffer.getvalue()) # ewww TODO

				if self.compression is not None:
					if length > self.compression:
						new_buffer = io.BytesIO()
						VarInt.write(length, new_buffer)
						new_buffer.write(zlib.compress(buffer.read()))
						buffer = new_buffer
					else:
						new_buffer = io.BytesIO()
						VarInt.write(0, new_buffer)
						new_buffer.write(buffer.read())
						buffer = new_buffer
					length = len(buffer.getvalue())

				data = VarInt.serialize(length) + buffer.getvalue()
				if self.encryption:
					data = self._encryptor.update(data)

				self._up.write(data)
				await self._up.drain()

				self._logger.debug("[-->] Sent | %s", str(packet))
			except Exception:
				self._logger.exception("Exception dispatching packet %s", str(packet))

			packet.processed.set() # Notify that packet has been processed

