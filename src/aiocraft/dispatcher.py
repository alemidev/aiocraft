import io
import asyncio
import zlib
import logging

from typing import Type, AsyncIterator
from asyncio import StreamReader, StreamWriter, Queue, Task
from types import ModuleType

from cryptography.hazmat.primitives.ciphers import CipherContext

from . import proto as minecraft_protocol
from .primitives import VarInt, Context
from .packet import Packet
from .types import ConnectionState
from .util import encryption

LOGGER = logging.getLogger(__name__)


class InvalidState(Exception):
	pass

class ConnectionError(Exception):
	pass

class Dispatcher:
	_is_server : bool # True when receiving packets from clients

	_down : StreamReader
	_reader : Task | None
	_decryptor : CipherContext

	_up   : StreamWriter
	_writer : Task | None
	_encryptor : CipherContext

	_dispatching : bool

	_incoming : Queue
	_outgoing : Queue

	_packet_whitelist : set[Type[Packet]] | None
	_packet_id_whitelist : set[int] | None

	_log_ignored_packets : bool

	_host : str
	_port : int

	_proto : int

	_encryption : bool
	_compression : int | None

	state : ConnectionState # TODO make getter/setter ?
	logger : logging.Logger

	def __init__(
			self,
			host:str = "localhost",
			port:int = 25565,
			proto:int = 757,
			compression_threshold: int | None = None,
			server:bool = False,
			log_ignored_packets: bool = False,
			whitelist: set[Type[Packet]] = set(),
	):
		self._proto = proto
		self._host = host
		self._port = port
		self._compression = compression_threshold
		self._is_server = server
		self._dispatching = False
		self._packet_whitelist = None
		self._packet_id_whitelist = None
		self._log_ignored_packets = log_ignored_packets
		self._packet_whitelist = set(whitelist) if whitelist is not None else None
		if self._packet_whitelist:
			self._packet_whitelist.add(minecraft_protocol.play.clientbound.PacketKeepAlive)
			self._packet_whitelist.add(minecraft_protocol.play.clientbound.PacketKickDisconnect)
		self._packet_id_whitelist = set((P().for_proto(self.proto) for P in self._packet_whitelist)) if self._packet_whitelist else None

	def promote(self, next_state:ConnectionState):
		# change dispatcher state
		self.state = next_state

	@property
	def proto(self) -> int:
		return self._proto

	@property
	def host(self) -> str:
		return self._host

	@property
	def port(self) -> int:
		return self._port

	@property
	def encryption(self) -> bool:
		return self._encryption

	@property
	def compression(self) -> int | None:
		return self._compression

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

	def encrypt(self, secret: bytes | None = None):
		if secret is not None:
			cipher = encryption.create_AES_cipher(secret)
			self._encryptor = cipher.encryptor()
			self._decryptor = cipher.decryptor()
			self._encryption = True
			self.logger.info("Encryption enabled")
		else:
			self._encryption = False
			self.logger.info("Encryption disabled")

	def update_compression_threshold(self, threshold: int | None):
		self._compression = threshold or 0

	async def connect(self,
		reader : StreamReader | None = None,
		writer : StreamWriter | None = None,
		queue_size : int = 100,
	):
		if self.connected:
			raise InvalidState("Dispatcher already connected")

		self.logger = LOGGER.getChild(f"on({self._host}:{self._port})")

		self._encryption = False
		self._compression = None
		self._incoming = Queue(queue_size)
		self._outgoing = Queue(queue_size)
		self._dispatching = False
		self._reader = None
		self._writer = None

		if reader and writer:
			self._down, self._up = reader, writer
		else: # TODO put a timeout here and throw exception
			self.logger.debug("Attempting to connect to %s:%d", self._host, self._port)
			self._down, self._up = await asyncio.open_connection(
				host=self._host,
				port=self._port,
			)

		self._dispatching = True
		self._reader = asyncio.get_event_loop().create_task(self._down_worker())
		self._writer = asyncio.get_event_loop().create_task(self._up_worker())
		self.logger.info("Connected")
		return self

	async def disconnect(self, block:bool=True):
		self._dispatching = False
		if block and self._writer and self._reader:
			await asyncio.gather(self._writer, self._reader)
			self.logger.debug("Net workers stopped")
		if self._up:
			if isinstance(self._up, StreamWriter) and not self._up.is_closing() and self._up.can_write_eof():
				try:
					self._up.write_eof()
					self.logger.debug("Wrote EOF on socket")
				except OSError as e:
					self.logger.error("Could not write EOF : %s", str(e))
			self._up.close()
			if block and isinstance(self._up, StreamWriter):
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

		if not self._proto:
			raise InvalidState("Cannot access registries from invalid protocol")

		proto = self._proto
		while proto not in reg:
			proto -= 1
		proto_reg = reg[proto]

		return proto_reg[packet_id]

	async def _read_varint_from_stream(self) -> int:
		if not isinstance(self._down, StreamReader):
			raise InvalidState("Requires a TCP connection")
		numRead = 0
		result = 0
		while True:
			data = await self._down.readexactly(1)
			if self._encryption:
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
		length = await self._read_varint_from_stream()
		return await self._down.readexactly(length)

	async def _write_packet(self, data:bytes):
		self._up.write(data)
		await self._up.drain() # TODO maybe no need to call drain?

	async def _down_worker(self, timeout:float=30):
		while self._dispatching:
			try: # Will timeout or raise EOFError if client gets disconnected
				data = await asyncio.wait_for(self._read_packet(), timeout=timeout)
				if not data:
					continue

				if self._encryption:
					data = self._decryptor.update(data)

				buffer = io.BytesIO(data)

				if self._compression is not None:
					decompressed_size = VarInt.read(buffer, Context(_proto=self._proto))
					if decompressed_size > 0:
						decompressor = zlib.decompressobj()
						decompressed_data = decompressor.decompress(buffer.read())
						if len(decompressed_data) != decompressed_size:
							raise ValueError(f"Failed decompressing packet: expected size is {decompressed_size}, but actual size is {len(decompressed_data)}")
						buffer = io.BytesIO(decompressed_data)

				packet_id = VarInt.read(buffer, Context(_proto=self._proto))
				if self.state == ConnectionState.PLAY and self._packet_id_whitelist \
				and packet_id not in self._packet_id_whitelist:
					if self._log_ignored_packets:
						self.logger.debug("[<--] Received | Packet(0x%02x) (ignored)", packet_id)
					continue # ignore this packet, we rarely need them all, should improve performance
				cls = self._packet_type_from_registry(packet_id)
				packet = cls.deserialize(self._proto, buffer)
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

	async def _up_worker(self, timeout:float = 1.):
		while self._dispatching:
			try:
				packet : Packet = await asyncio.wait_for(self._outgoing.get(), timeout=timeout)
			except asyncio.TimeoutError:
				continue # check again self._dispatching

			if not self._dispatching: # uglier than 'while self._dispatching' but I need to check it again after unblocking
				return

			try:
				buffer = packet.serialize(self.proto)
				length = len(buffer.getvalue()) # ewww TODO

				if self._compression is not None:
					if length > self._compression:
						new_buffer = io.BytesIO()
						VarInt.write(length, new_buffer, Context(_proto=self._proto))
						new_buffer.write(zlib.compress(buffer.read()))
						buffer = new_buffer
					else:
						new_buffer = io.BytesIO()
						VarInt.write(0, new_buffer, Context(_proto=self._proto))
						new_buffer.write(buffer.read())
						buffer = new_buffer
					length = len(buffer.getvalue())

				data = VarInt.serialize(length) + buffer.getvalue()
				if self._encryption:
					data = self._encryptor.update(data)
				await self._write_packet(data)
				self.logger.debug("[-->] Sent | %s", repr(packet))
			except Exception:
				self.logger.exception("Exception dispatching packet %s", str(packet))

			packet.processed.set() # Notify that packet has been processed

