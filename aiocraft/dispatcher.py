import io
import asyncio
import zlib
import logging
from asyncio import StreamReader, StreamWriter, Queue, Task
from enum import Enum
from typing import Dict, Optional

from cryptography.hazmat.primitives.ciphers import CipherContext

from .mc import proto
from .mc.mctypes import VarInt
from .mc.packet import Packet
from .mc import encryption

LOGGER = logging.getLogger(__name__)

class ConnectionState(Enum):
	NONE = -1
	HANDSHAKING = 0
	STATUS = 1
	LOGIN = 2
	PLAY = 3

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

	incoming : Queue
	outgoing : Queue

	_host : str
	_port : int

	proto : int
	state : ConnectionState
	encryption : bool
	compression : Optional[int]

	_logger : logging.Logger

	def __init__(self):
		self.proto = 340
		self._dispatching = False
		self.compression = None
		self.encryption = False
		self.incoming = Queue()
		self.outgoing = Queue()
		self._reader = None
		self._writer = None
		self._host = "localhost"
		self._port = 25565

		self._logger = LOGGER.getChild(f"{self._host}:{self._port}")

	@property
	def connected(self) -> bool:
		return self._dispatching

	async def write(self, packet:Packet, wait:bool=False) -> int:
		await self.outgoing.put(packet)
		if wait:
			await packet.sent.wait()
		return self.outgoing.qsize()

	async def disconnect(self, block:bool=True):
		self._dispatching = False
		if block and self._writer and self._reader:
			await asyncio.gather(self._writer, self._reader)
		if self._up.can_write_eof():
			self._up.write_eof()
		self._up.close()
		if block:
			await self._up.wait_closed()
		self._logger.info("Disconnected")

	async def connect(self, host:Optional[str] = None, port:Optional[int] = None):
		if self.connected:
			raise InvalidState("Dispatcher already connected")

		if host is not None:
			self._host = host
		if port is not None:
			self._port = port
		self._logger = LOGGER.getChild(f"{self._host}:{self._port}")

		self.encryption = False
		self.compression = None
		self.state = ConnectionState.HANDSHAKING
		# self.proto = 340 # TODO 

		# Make new queues
		self.incoming = Queue()
		self.outgoing = Queue()

		self._down, self._up = await asyncio.open_connection(
			host=self._host,
			port=self._port,
		)

		self._dispatching = True
		self._reader = asyncio.get_event_loop().create_task(self._down_worker())
		self._writer = asyncio.get_event_loop().create_task(self._up_worker())
		self._logger.info("Connected")

	def encrypt(self, secret:bytes):
		cipher = encryption.create_AES_cipher(secret)
		self._encryptor = cipher.encryptor()
		self._decryptor = cipher.decryptor()
		self.encryption = True
		self._logger.info("Encryption enabled")

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
			if self.state != ConnectionState.PLAY:
				await self.incoming.join() # During login we cannot pre-process any packet, first need to maybe get encryption/compression
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
				await self.incoming.put(packet)
			except AttributeError:
				self._logger.debug("Unimplemented packet %d", packet_id)
			except asyncio.IncompleteReadError:
				self._logger.error("EOF from server")
				await self.disconnect(block=False)
			except Exception:
				self._logger.exception("Exception parsing packet %d | %s", packet_id, buffer.getvalue())

	async def _up_worker(self):
		while self._dispatching:
			try:
				packet = await asyncio.wait_for(self.outgoing.get(), timeout=5)
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

				packet.sent.set() # Notify
				self._logger.debug("[-->] Sent | %s", str(packet))
			except asyncio.TimeoutError:
				pass # need this to recheck self._dispatching periodically
			except Exception:
				self._logger.exception("Exception dispatching packet %s", str(packet))

