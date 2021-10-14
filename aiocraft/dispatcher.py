import asyncio
from asyncio import StreamReader, StreamWriter, Queue, Task
from enum import Enum

from .mc import proto

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
	ConnectionStatus.HANDSHAKING : proto.handshaking,
	ConnectionStatus.STATUS : proto.status,
	ConnectionStatus.LOGIN : proto.login,
	ConnectionStatus.PLAY : proto.play,
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
			buffer = await self._down.read(length)
			# TODO encryption
			# TODO compression
			await self.incoming.put(buffer)

	async def _up_worker(self):
		while self._dispatching:
			packet = await self.outgoing.get()
			buffer = packet.serialize()
			length = len(buffer)
			# TODO compression
			# TODO encryption
			await self._up.write(VarInt.serialize(length) + buffer)

	async def run(self):
		if self.connected:
			raise InvalidState("Dispatcher already connected")
		await self.connect()

	async def stop(self):
		self._dispatching = False
		await asyncio.gather(self._writer, self._reader)


