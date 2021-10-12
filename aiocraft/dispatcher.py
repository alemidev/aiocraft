import asyncio
from asyncio import StreamReader, StreamWriter, Queue, Task
from enum import Enum

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

	async def _down_worker(self):
		while self._dispatching:
			length = await read_varint(self._down)
			buffer = await self._down.read(length)
			# TODO encryption
			# TODO compression
			await self.incoming.put(packet)

	async def _up_worker(self):
		while self._dispatching:
			buffer = await self.outgoing.get()
			length = len(buffer)
			# TODO compression
			# TODO encryption
			await self._up.write(VarInt.serialize(length) + buffer)

	async def run(self):
		if self.connected:
			raise InvalidState("Dispatcher already connected")
		await self.connect()
		self._dispatching = True
		self._reader = asyncio.get_event_loop().create_task(self._down_worker())
		self._writer = asyncio.get_event_loop().create_task(self._up_worker())

	async def stop(self):
		self._dispatching = False
		await asyncio.gather(self._writer, self._reader)


