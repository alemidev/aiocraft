import asyncio
import zlib
from asyncio import StreamReader, StreamWriter, Queue, Task
from enum import Enum

from .mc import proto
from .mc.mctypes import VarInt

class ConnectionState(Enum):
	HANDSHAKING = 0
	STATUS = 1
	LOGIN = 2
	PLAY = 3

def _registry_from_state(state:ConnectionState) -> Dict[int, Dict[int, Packet]]:
	if state == ConnectionState.HANDSHAKING:
		return proto.handshaking.clientbound.REGISTRY
	if state == ConnectionState.STATUS:
		return proto.status.clientbound.REGISTRY
	if state == ConnectionState.LOGIN:
		return proto.login.clientbound.REGISTRY
	if state == ConnectionState.PLAY:
		return proto.play.clientbound.REGISTRY

class InvalidState(Exception):
	pass

async def read_varint(stream: asyncio.StreamReader) -> int:
	"""Utility method to read a VarInt off the socket, because len comes as a VarInt..."""
	buf = 0
	off = 0
	while True:
		byte = int.from_bytes(await stream.read(1), 'little')
		buf |= (byte & 0b01111111) >> (7*off)
		if not byte & 0b10000000:
			break
		off += 1
	return buf

_STATE_REGS = {
	ConnectionState.HANDSHAKING : proto.handshaking,
	ConnectionState.STATUS : proto.status,
	ConnectionState.LOGIN : proto.login,
	ConnectionState.PLAY : proto.play,
}

class Dispatcher:
	_down : StreamReader
	_up   : StreamWriter
	_reader : Task
	_writer : Task
	_dispatching : bool

	incoming : Queue
	outgoing : Queue

	connected : bool
	state : ConnectionState
	encryption : bool
	compression : Optional[int]

	host : str
	port : int

	def __init__(self, host:str, port:int):
		self.host = host
		self.port = port
		self.connected = False
		self._dispatching = False

	async def connect(self):
		self._down, self._up = await asyncio.open_connection(
			host=self.host,
			port=self.port,
		)
		self.state = ConnectionState.HANDSHAKING
		self.encryption = False
		self.compression = None
		self.connected = True

		packet_handshake = proto.handshaking.serverbound.PacketSetProtocol(
			self.proto,
			protocolVersion=self.proto,
			serverHost=self.host,
			serverPost=self.port,
			nextState=3, # play
		)
		packet_login = proto.login.serverbound.PacketLoginStart(340, username=self.username)

		await self.outgoing.put(packet_handshake)
		await self.outgoing.put(packet_login)

		self._dispatching = True
		self._reader = asyncio.get_event_loop().create_task(self._down_worker())
		self._writer = asyncio.get_event_loop().create_task(self._up_worker())

	async def _down_worker(self):
		while self._dispatching:
			length = await read_varint(self._down)
			buffer = io.BytesIO(await self._down.read(length))

			# TODO encryption

			if self.compression is not None:
				decompressed_size = VarInt.read(buffer)
				if decompressed_size > 0:
					decompressor = zlib.decompressobj()
					decompressed_data = decompressor.decompress(buffer.read())
					if len(decompressed_data) != decompressed_size:
						raise ValueError(f"Failed decompressing packet: expected size is {decompressed_size}, but actual size is {len(decompressed_data)}")
					buffer = io.BytesIO(decompressed_data)

			packet_id = VarInt.read(buffer)
			cls = _registry_from_state(self.state)[self.proto][packet_id]
			await self.incoming.put(cls.deserialize(self.proto, buffer))

	async def _up_worker(self):
		while self._dispatching:
			packet = await self.outgoing.get()
			buffer = packet.serialize()
			length = len(buffer)

			if self.compression is not None:
				if length > self.compression:
					new_buffer = io.BytesIO()
					VarInt.write(length, new_buffer)
					new_buffer.write(zlib.compress(buffer.read()))
					buffer = new_buffer
				else:
					new_buffer = io.BytesIO()
					VarInt.write(0, new_buffer)
					new_buffer.write(buffer.read)
					buffer = new_buffer
				length = len(buffer)

			# TODO encryption

			await self._up.write(VarInt.serialize(length) + buffer)

	async def run(self):
		if self.connected:
			raise InvalidState("Dispatcher already connected")
		await self.connect()

	async def stop(self):
		self._dispatching = False
		await asyncio.gather(self._writer, self._reader)


