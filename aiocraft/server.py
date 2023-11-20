import re
import json
import asyncio
import logging
import uuid

from dataclasses import dataclass
from asyncio import Task, StreamReader, StreamWriter
from asyncio.base_events import Server # just for typing

from .dispatcher import Dispatcher
from .types import ConnectionState
from .proto.status.serverbound import PacketPing, PacketPingStart
from .proto.status.clientbound import PacketServerInfo, PacketPing as PacketPong
from .proto.handshaking.serverbound import PacketSetProtocol
from .proto.play.clientbound import PacketKickDisconnect, PacketPosition, PacketLogin
from .proto.login.serverbound import PacketLoginStart, PacketEncryptionBegin as PacketEncryptionResponse
from .proto.login.clientbound import PacketDisconnect, PacketSuccess

REMOVE_COLOR_FORMATS = re.compile(r"§[0-9a-z]")
LOGGER = logging.getLogger(__name__)

@dataclass
class ServerOptions:
	online_mode : bool
	spawn_player : bool
	poll_interval : float
	motd : str
	max_players : int

class AbstractMinecraftServer:
	host:str
	port:int
	options:ServerOptions

	_dispatcher_pool : list[Dispatcher]
	_processing : bool
	_server : Server
	_worker : Task

	logger : logging.Logger

	def __init__(
		self,
		host:str = "127.0.0.1",
		port:int = 25565,
		online_mode:bool = False,
		spawn_player:bool = True,
		poll_interval:float = 1.0,
		motd:str = "aiocraft server",
		max_players:int = 10,
	):
		super().__init__()
		self.host = host
		self.port = port

		self.options = ServerOptions(
			online_mode=online_mode,
			spawn_player=spawn_player,
			poll_interval=poll_interval,
			motd=motd,
			max_players=max_players,
		)

		self._dispatcher_pool = []
		self._processing = False

		self.logger = LOGGER.getChild(f"@({self.host}:{self.port})")

	@property
	def started(self) -> bool:
		return self._processing

	@property
	def connected(self) -> int:
		return len(self._dispatcher_pool)

	async def start(self):
		if self.started:
			return
		self._server = await asyncio.start_server(
			self._server_worker, self.host, self.port
		)
	
		self._processing = True
		await self._server.start_serving()
		self.logger.info("Minecraft server started")

	async def stop(self, force:bool = False):
		self._processing = False
		self._server.close()
		await asyncio.gather(*[d.disconnect(block=not force) for d in self._dispatcher_pool])
		if not force:
			await self._server.wait_closed()

	async def _server_worker(self, reader:StreamReader, writer:StreamWriter):
		dispatcher = Dispatcher(host=self.host, port=self.port, server=True)
		self._dispatcher_pool.append(dispatcher)

		self.logger.debug("Starting dispatcher for client")
		await dispatcher.connect(reader=reader,	writer=writer)

		await self._handshake(dispatcher)
		if dispatcher.state == ConnectionState.STATUS:
			await self._status(dispatcher)
		elif dispatcher.state == ConnectionState.LOGIN:
			if await self._login(dispatcher):
				await self._play(dispatcher)

		if dispatcher.connected:
			await dispatcher.write(
				PacketKickDisconnect(reason="Connection terminated")
				if dispatcher.state == ConnectionState.PLAY else
				PacketDisconnect(reason="Connection terminated")
			)
			await dispatcher.disconnect()

	async def _handshake(self, dispatcher:Dispatcher) -> bool:
		self.logger.info("Awaiting handshake")
		async for packet in dispatcher.packets():
			if isinstance(packet, PacketSetProtocol):
				self.logger.info("Received set protocol packet")
				dispatcher._proto = packet.protocolVersion # TODO shouldn't be doing it this way
				if packet.nextState == 1:
					self.logger.debug("Changing state to STATUS")
					dispatcher.state = ConnectionState.STATUS
					return True
				elif packet.nextState == 2:
					self.logger.debug("Changing state to LOGIN")
					dispatcher.state = ConnectionState.LOGIN
					return True
		return False

	async def _status(self, dispatcher:Dispatcher) -> bool:
		self.logger.info("Answering ping")
		async for packet in dispatcher.packets():
			if isinstance(packet, PacketPingStart):
				await dispatcher.write(
					PacketServerInfo(
						response=json.dumps({
							"online": True,
							"ip": self.host,
							"port": self.port,
							"motd": {
								"raw": self.options.motd.split("\n"),
								"clean": REMOVE_COLOR_FORMATS.sub("", self.options.motd).split("\n"),
								"html": self.options.motd.replace("\n", "<br/>"),
							},
							"players": {
								"online": len(self._dispatcher_pool),
								"max": self.options.max_players,
								# "list": [
								# 	"notch",
								# ],
								# "uuid": {
								# 	"notch": "xxx-xxx...",
								# }
							},
							"version": "many", # TODO proto number to string
							"protocol": dispatcher.proto,
							# "hostname": "server.mymcserver.tld", # TODO get from config?
							# "icon": "data:image\/png;base64,iVBORw0KGgoAAAANSUhEU...dSk6AAAAAElFTkSuQmCC",
							"software": "aiocraft",
							"map": "null",
							# "info": { # TODO overrules default player names list
							# 	"raw": [],
							# 	"clean": [],
							# 	"html": []
							# }
						})
					)
				)
			elif isinstance(packet, PacketPing):
				await dispatcher.write(PacketPong(time=packet.time))
		return False

	async def _login(self, dispatcher:Dispatcher) -> bool:
		self.logger.info("Logging in player")
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
							uuid=str(uuid.uuid4()),
							username=packet.username,
						)
					)
					return True
			elif isinstance(packet, PacketEncryptionResponse):
				pass # TODO enable encryption?
				# shared_secret = packet.sharedSecret
				# verify_token = packet.verifyToken
				# return True
		return False

	async def _play(self, dispatcher:Dispatcher) -> bool:
		self.logger.info("Player connected")

		if self.options.spawn_player:
			await dispatcher.write(
				PacketLogin(
					gameMode=3,
					isFlat=False,
					worldNames=[],
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

		async for packet in dispatcher.packets():
			# TODO handle play
			pass

		return False

