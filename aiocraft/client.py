import asyncio
from asyncio import Task
from enum import Enum

from typing import Dict

from .dispatcher import Dispatcher, ConnectionState
from .mc.mctypes import VarInt
from .mc.packet import Packet
from .mc import proto


def _registry_from_state(state:ConnectionState) -> Dict[int, Dict[int, Packet]]:
	if state == ConnectionState.HANDSHAKING:
		return proto.handshaking.clientbound.REGISTRY
	if state == ConnectionState.STATUS:
		return proto.status.clientbound.REGISTRY
	if state == ConnectionState.LOGIN:
		return proto.login.clientbound.REGISTRY
	if state == ConnectionState.PLAY:
		return proto.play.clientbound.REGISTRY

class Client:
	host:str
	port:int

	proto : int
	state : ConnectionState

	dispatcher : Dispatcher
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

		self.proto = 340 # TODO default to max available proto
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
			cls = _registry_from_state(self.state)[self.proto][packet_id]
			packet = cls.deserialize(buffer)

			# Process packets? switch state, invoke callbacks? Maybe implement Reactors?
			if self.state == ConnectionState.HANDSHAKING:
				self.handshaking_logic(packet)
			elif self.state == ConnectionState.LOGIN:
				self.login_logic(packet)
			elif self.state == ConnectionState.PLAY:
				self.play_logic(packet)

	async def handshaking_logic(self, packet:Packet):
		pass

	async def status_logic(self, packet:Packet):
		pass

	async def login_logic(self, packet:Packet):
		pass

	async def play_logic(self, packet:Packet):
		pass

