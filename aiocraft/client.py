import asyncio
from asyncio import Task
from enum import Enum

from .dispatcher import Dispatcher
from .mc.mctypes import VarInt

class ConnectionState(Enum):
	HANDSHAKING = 0
	STATUS = 1
	LOGIN = 2
	PLAY = 3

class Client:
	host:str
	port:int

	dispatcher : Dispatcher
	state : ConnectionState
	_processing : bool
	_worker : Task

	def __init__(
		self,
		username : str,
		password : str,
		host: str = "localhost",
		port: int = 25565,
	):
		self.host = host
		self.port = port

		self.state = ConnectionState.HANDSHAKING
		self.dispatcher = Dispatcher(host, port)
		self._processing = False
		

	async def run(self):
		await self.dispatcher.run()
		self._processing = True
		self._worker = asyncio.get_event_loop().create_task(self._logic_worker())


	async def _logic_worker(self):
		while self._processing:
			buffer = await self.dispatcher.incoming.get()
			packet_id = VarInt.deserialize(buffer)
			cls = PacketRegistry.state(self.state).clientbound.get(packet_id)
			packet = cls(buffer)
			# Process packets? switch state, invoke callbacks? Maybe implement Reactors?


