import io
import asyncio
import contextlib
import zlib
import logging
from asyncio import StreamReader, StreamWriter, Queue, Task
from enum import Enum
from typing import List, Dict, Set, Optional, AsyncIterator, Type, Union
from types import ModuleType

from cryptography.hazmat.primitives.ciphers import CipherContext

from .mc import proto as minecraft_protocol
from .mc.types import VarInt, Context
from .mc.packet import Packet
from .mc.definitions import ConnectionState
from .util import encryption

LOGGER = logging.getLogger(__name__)

class InvalidState(Exception):
	pass

class ConnectionError(Exception):
	pass

class Dispatcher:
	_is_server : bool # True when receiving packets from clients

	_down : StreamReader
	_reader : Optional[Task]
	_decryptor : CipherContext

	_up   : StreamWriter
	_writer : Optional[Task]
	_encryptor : CipherContext

	_dispatching : bool

	_incoming : Queue
	_outgoing : Queue

	_packet_whitelist : Optional[Set[Type[Packet]]]
	_packet_id_whitelist : Optional[Set[int]]

	_log_ignored_packets : bool

	host : str
	port : int

	proto : int
	state : ConnectionState
	encryption : bool
	compression : Optional[int]

	logger : logging.Logger

	def __init__(self, server:bool = False):
		self.proto = 757
		self._is_server = server
		self.host = "localhost"
		self.port = 25565
		self._dispatching = False
		self._packet_whitelist = None
		self._packet_id_whitelist = None
		self._log_ignored_packets = False

	@property
	def is_server(self) -> bool:
		return self._is_server

	@property
	def connected(self) -> bool:
		return self._dispatching

	async def write(self, packet:Packet, wait:bool=False) -> int:
		await self._outgoing.put(packet)
		if wait:
			await packet.processed.wait()
		return self._outgoing.qsize()

	async def packets(self, timeout=1) -> AsyncIterator[Packet]:
		while self.connected or self._incoming.qsize(): # Finish processing packets on disconnect
			try: # TODO replace this timed busy-wait with an event which resolves upon disconnection, and await both
				packet = await asyncio.wait_for(self._incoming.get(), timeout=timeout)
				try:
					yield packet
				finally:
					self._incoming.task_done()
			except asyncio.TimeoutError:
				pass # so we recheck self.connected

	def encrypt(self, secret:Optional[bytes]=None) -> 'Dispatcher':
		if secret is not None:
			cipher = encryption.create_AES_cipher(secret)
			self._encryptor = cipher.encryptor()
			self._decryptor = cipher.decryptor()
			self.encryption = True
			self.logger.info("Encryption enabled")
		else:
			self.encryption = False
			self.logger.info("Encryption disabled")
		return self

	def whitelist(self, ids:Optional[List[Type[Packet]]]) -> 'Dispatcher':
		self._packet_whitelist = set(ids) if ids is not None else None
		if self._packet_whitelist:
			self._packet_whitelist.add(minecraft_protocol.play.clientbound.PacketKeepAlive)
			self._packet_whitelist.add(minecraft_protocol.play.clientbound.PacketKickDisconnect)
		self._packet_id_whitelist = set((P(self.proto).id for P in self._packet_whitelist)) if self._packet_whitelist else None
		return self

	def set_host(self, host:Optional[str]="localhost", port:Optional[int]=25565) -> 'Dispatcher':
		self.host = host or self.host
		self.port = port or self.port
		self.logger = LOGGER.getChild(f"on({self.host}:{self.port})")
		return self

	def set_proto(self, proto:Optional[int]=757) -> 'Dispatcher':
		self.proto = proto or self.proto
		if self._packet_whitelist:
			self._packet_id_whitelist = set((P(self.proto).id for P in self._packet_whitelist))
		return self

	def set_state(self, state:Optional[ConnectionState]=ConnectionState.HANDSHAKING) -> 'Dispatcher':
		self.state = state or self.state
		return self

	def log_ignored_packets(self, log:bool) -> 'Dispatcher':
		self._log_ignored_packets = log
		return self

	async def connect(self,
			reader : Optional[StreamReader] = None,
			writer : Optional[StreamWriter] = None,
			queue_size : int = 100,
	) -> 'Dispatcher':
		if self.connected:
			raise InvalidState("Dispatcher already connected")

		self.encryption = False
		self.compression = None
		self._incoming = Queue(queue_size)
		self._outgoing = Queue(queue_size)
		self._dispatching = False
		self._reader = None
		self._writer = None

		if reader and writer:
			self._down, self._up = reader, writer
		else:
			self._down, self._up = await asyncio.open_connection(
				host=self.host,
				port=self.port,
			)

		self._dispatching = True
		self._reader = asyncio.get_event_loop().create_task(self._down_worker())
		self._writer = asyncio.get_event_loop().create_task(self._up_worker())
		self.logger.info("Connected")
		return self

	async def disconnect(self, block:bool=True) -> 'Dispatcher':
		self._dispatching = False
		if block and self._writer and self._reader:
			await asyncio.gather(self._writer, self._reader)
			self.logger.debug("Net workers stopped")
		if self._up:
			if not self._up.is_closing() and self._up.can_write_eof():
				try:
					self._up.write_eof()
				except OSError as e:
					self.logger.error("Could not write EOF : %s", str(e))
			self._up.close()
			if block:
				await self._up.wait_closed()
				self.logger.debug("Socket closed")
		if block:
			self.logger.info("Disconnected")
		return self

	def _packet_type_from_registry(self, packet_id:int) -> Type[Packet]:
		m : ModuleType

		if self.state == ConnectionState.HANDSHAKING:
			m = minecraft_protocol.handshaking
		elif self.state == ConnectionState.STATUS:
			m = minecraft_protocol.status
		elif self.state == ConnectionState.LOGIN:
			m = minecraft_protocol.login
		elif self.state == ConnectionState.PLAY:
			m = minecraft_protocol.play
		else:
			raise InvalidState("Cannot access registries from invalid state")

		if self.is_server:
			reg = m.serverbound.REGISTRY
		else:
			reg = m.clientbound.REGISTRY

		if not self.proto:
			raise InvalidState("Cannot access registries from invalid protocol")

		proto_reg = reg[self.proto]

		return proto_reg[packet_id]

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

	async def _read_packet(self) -> bytes:
		length = await self._read_varint()
		return await self._down.readexactly(length)


	async def _down_worker(self, timeout:float=30):
		while self._dispatching:
			try: # Will timeout or raise EOFError if client gets disconnected
				data = await asyncio.wait_for(self._read_packet(), timeout=timeout)

				if self.encryption:
					data = self._decryptor.update(data)

				buffer = io.BytesIO(data)

				if self.compression is not None:
					decompressed_size = VarInt.read(buffer, Context(_proto=self.proto))
					if decompressed_size > 0:
						decompressor = zlib.decompressobj()
						decompressed_data = decompressor.decompress(buffer.read())
						if len(decompressed_data) != decompressed_size:
							raise ValueError(f"Failed decompressing packet: expected size is {decompressed_size}, but actual size is {len(decompressed_data)}")
						buffer = io.BytesIO(decompressed_data)

				packet_id = VarInt.read(buffer, Context(_proto=self.proto))
				if self.state == ConnectionState.PLAY and self._packet_id_whitelist \
				and packet_id not in self._packet_id_whitelist:
					if self._log_ignored_packets:
						self.logger.debug("[<--] Received | Packet(0x%02x) (ignored)", packet_id)
					continue # ignore this packet, we rarely need them all, should improve performance
				cls = self._packet_type_from_registry(packet_id)
				packet = cls.deserialize(self.proto, buffer)
				self.logger.debug("[<--] Received | %s", repr(packet))
				await self._incoming.put(packet)
				if self.state != ConnectionState.PLAY:
					await self._incoming.join() # During play we can pre-process packets

			except (asyncio.TimeoutError, TimeoutError):
				self.logger.error("Connection timed out")
				await self.disconnect(block=False)
			except (ConnectionResetError, BrokenPipeError):
				self.logger.error("Connection reset while reading packet")
				await self.disconnect(block=False)
			except (asyncio.IncompleteReadError, EOFError):
				self.logger.error("Received EOF while reading packet")
				await self.disconnect(block=False)
			except Exception:
				self.logger.exception("Exception parsing packet %d", packet_id)
				self.logger.debug("%s", buffer.getvalue())
				await self.disconnect(block=False)

	async def _up_worker(self, timeout=1):
		while True:
			try:
				packet : Packet = await asyncio.wait_for(self._outgoing.get(), timeout=timeout)
			except asyncio.TimeoutError:
				continue # check again self._dispatching

			if not self._dispatching: # uglier than 'while self._dispatching' but I need to check it again after unblocking
				return

			try:
				buffer = packet.serialize()
				length = len(buffer.getvalue()) # ewww TODO

				if self.compression is not None:
					if length > self.compression:
						new_buffer = io.BytesIO()
						VarInt.write(length, new_buffer, Context(_proto=self.proto))
						new_buffer.write(zlib.compress(buffer.read()))
						buffer = new_buffer
					else:
						new_buffer = io.BytesIO()
						VarInt.write(0, new_buffer, Context(_proto=self.proto))
						new_buffer.write(buffer.read())
						buffer = new_buffer
					length = len(buffer.getvalue())

				data = VarInt.serialize(length) + buffer.getvalue()
				if self.encryption:
					data = self._encryptor.update(data)

				self._up.write(data)
				await self._up.drain() # TODO maybe no need to call drain?

				self.logger.debug("[-->] Sent | %s", repr(packet))
			except Exception:
				self.logger.exception("Exception dispatching packet %s", str(packet))

			packet.processed.set() # Notify that packet has been processed

