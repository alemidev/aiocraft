import asyncio
from asyncio import StreamReader, StreamWriter
from enum import Enum

class ConnectionState(Enum):
	HANDSHAKING = 0
	STATUS = 1
	LOGIN = 2
	PLAY = 3

class InvalidState(Exception):
	pass

class Dispatcher:
	connected : bool
	down : StreamReader
	up   : StreamWriter
	host : str
	port : int

	def __init__(self, host:str, port:int):
		self.host = host
		self.port = port
		self.connected = False

	async def _connect(self):
		self.down, self.up = await asyncio.open_connection(
			host=self.host,
			port=self.port,
		)
		self.connected = True

	async def _work(self):
		while True:
			buf = await self.down.

	async def run(self):
		if self.connected:
			raise InvalidState("Dispatcher already connected")
		await self._connect()


