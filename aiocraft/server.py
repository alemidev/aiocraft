import asyncio
import logging
import uuid

from dataclasses import dataclass
from asyncio import Task, StreamReader, StreamWriter
from asyncio.base_events import Server # just for typing
from enum import Enum

from typing import Dict, List, Callable, Coroutine, Type, Optional, Tuple, AsyncIterator

from .dispatcher import Dispatcher
from .traits import CallbacksHolder, Runnable
from .mc.packet import Packet
from .mc.token import Token, AuthException
from .mc.definitions import Dimension, Difficulty, Gamemode, ConnectionState
from .mc.proto.handshaking.serverbound import PacketSetProtocol
from .mc.proto.play.serverbound import PacketKeepAlive as PacketKeepAliveResponse
from .mc.proto.play.clientbound import PacketKeepAlive, PacketSetCompression, PacketKickDisconnect, PacketPosition, PacketLogin
from .mc.proto.login.serverbound import PacketLoginStart, PacketEncryptionBegin as PacketEncryptionResponse
from .mc.proto.login.clientbound import (
	PacketCompress, PacketDisconnect, PacketEncryptionBegin, PacketLoginPluginRequest, PacketSuccess
)
from .util import encryption

LOGGER = logging.getLogger(__name__)

@dataclass
class ServerOptions:
	online_mode : bool
	spawn_player : bool
	poll_interval : float

class ServerEvent(Enum):
	CLIENT_CONNECTED = 0
	CLIENT_DISCONNECTED = 1

class MinecraftServer(CallbacksHolder, Runnable):
	host:str
	port:int
	options:ServerOptions

	_dispatcher_pool : List[Dispatcher]
	_processing : bool
	_server : Server
	_worker : Task

	_logger : logging.Logger

	def __init__(
		self,
		host:str,
		port:int = 25565,
		online_mode:bool = False,
		spawn_player:bool = True,
		poll_interval:float = 1.0,
	):
		super().__init__()
		self.host = host
		self.port = port

		self.options = ServerOptions(
			online_mode=online_mode,
			spawn_player=spawn_player,
			poll_interval=poll_interval,
		)

		self._dispatcher_pool = []
		self._processing = False

		self._logger = LOGGER.getChild(f"@({self.host}:{self.port})")

	@property
	def started(self) -> bool:
		return self._processing

	@property
	def connected(self) -> int:
		return len(self._dispatcher_pool)

	def on_connect(self):
		def wrapper(fun):
			self.register(ServerEvent.CLIENT_CONNECTED, fun)
			return fun
		return wrapper

	def on_disconnect(self):
		def wrapper(fun):
			self.register(ServerEvent.CLIENT_DISCONNECTED, fun)
			return fun
		return wrapper

	def on_packet(self, packet:Type[Packet]):
		def wrapper(fun):
			self.register(packet, fun)
			return fun
		return wrapper

	async def start(self):
		if self.started:
			return
		self._server = await asyncio.start_server(
			self._server_worker, self.host, self.port
		)
	
		self._processing = True
		await self._server.start_serving()
		self._logger.info("Minecraft server started")

	async def stop(self, force:bool = False):
		self._processing = False
		self._server.close()
		await asyncio.gather(*[d.disconnect(block=not force) for d in self._dispatcher_pool])
		if not force:
			await asyncio.gather(
				self._server.wait_closed(),
				self.join_callbacks(),
			)

	async def _disconnect_client(self, dispatcher):
		if dispatcher.state == ConnectionState.LOGIN:
			await dispatcher.write(PacketDisconnect(dispatcher.proto, reason="Connection terminated"))
		else:
			await dispatcher.write(PacketKickDisconnect(dispatcher.proto, reason="Connection terminated"))

	async def _server_worker(self, reader:StreamReader, writer:StreamWriter):
		dispatcher = Dispatcher(server=True)
		self._dispatcher_pool.append(dispatcher)

		self._logger.debug("Starting dispatcher for client")
		await dispatcher.connect(
			host=self.host,
			port=self.port,
			reader=reader,
			writer=writer,
		)

		await self._handshake(dispatcher)
		if dispatcher.state == ConnectionState.STATUS:
			await self._status(dispatcher)
		elif dispatcher.state == ConnectionState.LOGIN:
			if await self._login(dispatcher):
				await self._play(dispatcher)

		if dispatcher.connected:
			await self._disconnect_client(dispatcher)
			await dispatcher.disconnect()

	async def _handshake(self, dispatcher:Dispatcher) -> bool: # TODO make this fancier! poll for version and status first
		self._logger.info("Awaiting handshake")
		async for packet in dispatcher.packets():
			if isinstance(packet, PacketSetProtocol):
				self._logger.info("Received set protocol packet")
				dispatcher.proto = packet.protocolVersion
				if packet.nextState == 1:
					self._logger.debug("Changing state to STATUS")
					dispatcher.state = ConnectionState.STATUS
					return True
				elif packet.nextState == 2:
					self._logger.debug("Changing state to LOGIN")
					dispatcher.state = ConnectionState.LOGIN
					return True
		return False

	async def _status(self, dispatcher:Dispatcher) -> bool:
		self._logger.info("Answering ping")
		async for packet in dispatcher.packets():
			pass # TODO handle status!
		return False

	async def _login(self, dispatcher:Dispatcher) -> bool:
		self._logger.info("Logging in player")
		async for packet in dispatcher.packets():
			if isinstance(packet, PacketLoginStart):
				if self.options.online_mode:
					# await dispatcher.write(
					# 	PacketEncryptionBegin(
					# 		dispatcher.proto,
					# 		serverId="????",
					# 		publicKey=b"??????",
					# 		verifyToken=b"1234",
					# 	)
					# )
					pass
				else:
					await dispatcher.write(
						PacketSuccess(
							dispatcher.proto,
							uuid=str(uuid.uuid4()),
							username=packet.username,
						)
					)
					return True
			elif isinstance(packet, PacketEncryptionResponse):
				shared_secret = packet.sharedSecret
				verify_token = packet.verifyToken
				# TODO enable encryption?
				# return True
		return False

	async def _play(self, dispatcher:Dispatcher) -> bool:
		self._logger.info("Player connected")

		if self.options.spawn_player:
			await dispatcher.write(
				PacketLogin(
					dispatcher.proto,
					gameMode=3,
					isFlat=False,
					worldNames=b'',
					worldName='aiocraft',
					previousGameMode=3,
					entityId=1,
					isHardcore=False,
					difficulty=0,
					isDebug=True,
					enableRespawnScreen=False,
					maxPlayers=1,
					dimension=1,
					levelType='aiocraft',
					reducedDebugInfo=False,
					hashedSeed=1234,
					viewDistance=4
				)
			)

			await dispatcher.write(
				PacketPosition(
					dispatcher.proto,
					dismountVehicle=True,
					x=0,
					y=120,
					flags=0,
					yaw=0.0,
					onGround=False,
					teleportId=1,
					pitch=0.0,
					z=0,
				)
			)

		self.run_callbacks(ServerEvent.CLIENT_CONNECTED)

		async for packet in dispatcher.packets():
			# TODO handle play
			self.run_callbacks(Packet, packet)
			self.run_callbacks(type(packet), packet)

		self.run_callbacks(ServerEvent.CLIENT_DISCONNECTED)

		return False

