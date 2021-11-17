import asyncio
import logging
from asyncio import Task
from enum import Enum

from typing import Dict, List, Callable, Type, Optional, Tuple, AsyncIterator

from .dispatcher import Dispatcher
from .mc.packet import Packet
from .mc.token import Token, AuthException
from .mc.definitions import Dimension, Difficulty, Gamemode, ConnectionState
from .mc.proto.handshaking.serverbound import PacketSetProtocol
from .mc.proto.play.serverbound import PacketKeepAlive as PacketKeepAliveResponse
from .mc.proto.play.clientbound import PacketKeepAlive, PacketSetCompression, PacketKickDisconnect
from .mc.proto.login.serverbound import PacketLoginStart, PacketEncryptionBegin as PacketEncryptionResponse
from .mc.proto.login.clientbound import (
	PacketCompress, PacketDisconnect, PacketEncryptionBegin, PacketLoginPluginRequest, PacketSuccess
)
from .util import encryption

LOGGER = logging.getLogger(__name__)

class Client:
	host:str
	port:int
	options:dict

	username:Optional[str]
	password:Optional[str]
	token:Optional[Token]

	dispatcher : Dispatcher
	_processing : bool
	_authenticated : bool
	_worker : Task

	_packet_callbacks : Dict[Type[Packet], List[Callable]]
	_logger : logging.Logger

	def __init__(
		self,
		host:str,
		port:int = 25565,
		options:dict = None,
		username:Optional[str] = None,
		password:Optional[str] = None,
		token:Optional[Token] = None,
	):
		self.host = host
		self.port = port

		self.options = options or {
			"reconnect" : True,
			"rctime" : 5.0,
			"keep-alive" : True,
			"poll-timeout" : 1,
		}

		self.token = token
		self.username = username
		self.password = password

		self.dispatcher = Dispatcher()
		self._processing = False
		self._authenticated = False

		self._packet_callbacks = {}

		self._logger = LOGGER.getChild(f"{self.host}:{self.port}")

	@property
	def started(self) -> bool:
		return self._processing

	@property
	def connected(self) -> bool:
		return self.started and self.dispatcher.connected

	def on_packet(self, packet:Type[Packet], *args) -> Callable: # receive *args for retro compatibility
		def wrapper(fun):
			if packet not in self._packet_callbacks:
				self._packet_callbacks[packet] = []
			self._packet_callbacks[packet].append(fun)
			return fun
		return wrapper

	async def authenticate(self) -> bool:
		if self._authenticated:
			return True # Don't spam Auth endpoint!
		if not self.token:
			if self.username and self.password:
				self.token = await Token.authenticate(self.username, self.password)
				self._logger.info("Authenticated from credentials")
				self._authenticated = True
				return True
			raise AuthException("No token or credentials provided")
		try:
			await self.token.validate() # will raise an exc if token is invalid
			self._authenticated = True
		except AuthException:
			await self.token.refresh()
			self._authenticated = True
			self._logger.warning("Refreshed Token")
		return True

	async def change_server(self, server:str):
		restart = self.started
		if restart:
			await self.stop()

		if ":" in server:
			_host, _port = server.split(":", 1)
			self.host = _host.strip()
			self.port = int(_port)
		else:
			self.host = server.strip()
			self.port = 25565
		self._logger = LOGGER.getChild(f"{self.host}:{self.port}")

		if restart:
			await self.start()

	async def run(self):
		await self.start()

		try:
			while self._processing: # TODO don't busywait even if it doesn't matter much
				await asyncio.sleep(self.options["poll-timeout"])
		except KeyboardInterrupt:
			self._logger.info("Received SIGINT, stopping...")
		else:
			self._logger.warning("Client terminating...")

		await self.stop()

	async def start(self):
		self._processing = True
		self._worker = asyncio.get_event_loop().create_task(self._client_worker())
		self._logger.info("Minecraft client started")

	async def stop(self, block=True):
		self._processing = False
		if self.dispatcher.connected:
			await self.dispatcher.disconnect(block=block)
		if block:
			await self._worker
			self._logger.info("Minecraft client stopped")

	async def _client_worker(self):
		while self._processing:
			try:
				await self.authenticate()
			except AuthException as e:
				self._logger.error(str(e))
				break
			try:
				await self.dispatcher.connect(self.host, self.port)
				await self._handshake()
				if await self._login():
					await self._play()
			except ConnectionRefusedError:
				self._logger.error("Server rejected connection")
			except Exception:
				self._logger.exception("Exception in Client connection")
			if self.dispatcher.connected:
				await self.dispatcher.disconnect()
			if not self.options["reconnect"]:
				break
			await asyncio.sleep(self.options["rctime"])
		await self.stop(block=False)

	async def _handshake(self) -> bool: # TODO make this fancier! poll for version and status first
		await self.dispatcher.write(
			PacketSetProtocol(
				340, # TODO!!!!
				protocolVersion=340,
				serverHost=self.host,
				serverPort=self.port,
				nextState=2, # play
			)
		)
		await self.dispatcher.write(
			PacketLoginStart(
				340,
				username=self.token.profile.name if self.token else self.username
			)
		)
		return True

	async def _login(self) -> bool:
		self.dispatcher.state = ConnectionState.LOGIN
		async for packet in self.dispatcher.packets():
			if isinstance(packet, PacketEncryptionBegin):
				secret = encryption.generate_shared_secret()
				token, encrypted_secret = encryption.encrypt_token_and_secret(
					packet.publicKey,
					packet.verifyToken,
					secret
				)
				if packet.serverId != '-' and self.token:
					try:
						await self.token.join(
							encryption.generate_verification_hash(
								packet.serverId,
								secret,
								packet.publicKey
							)
						)
					except AuthException:
						self._logger.error("Could not authenticate with Mojang")
						break
				encryption_response = PacketEncryptionResponse(
					340, # TODO!!!!
					sharedSecret=encrypted_secret,
					verifyToken=token
				)
				await self.dispatcher.write(encryption_response, wait=True)
				self.dispatcher.encrypt(secret)
			elif isinstance(packet, PacketCompress):
				self._logger.info("Compression enabled")
				self.dispatcher.compression = packet.threshold
			elif isinstance(packet, PacketLoginPluginRequest):
				self._logger.info("Ignoring plugin request") # TODO ?
			elif isinstance(packet, PacketSuccess):
				self._logger.info("Login success, joining world...")
				return True
			elif isinstance(packet, PacketDisconnect):
				self._logger.error("Kicked while logging in")
				break
		return False

	async def _play(self) -> bool:
		self.dispatcher.state = ConnectionState.PLAY
		async for packet in self.dispatcher.packets():
			self._logger.debug("[ * ] Processing | %s", str(packet))
			if isinstance(packet, PacketSetCompression):
				self._logger.info("Compression updated")
				self.dispatcher.compression = packet.threshold
			elif isinstance(packet, PacketKeepAlive):
				if self.options["keep-alive"]:
					keep_alive_packet = PacketKeepAliveResponse(340, keepAliveId=packet.keepAliveId)
					await self.dispatcher.write(keep_alive_packet)
			elif isinstance(packet, PacketKickDisconnect):
				self._logger.error("Kicked while in game")
				break
			for packet_type in (Packet, packet.__class__): # check both callbacks for base class and instance class
				if packet_type in self._packet_callbacks:
					for cb in self._packet_callbacks[packet_type]:
						try: # TODO run in executor to not block
							await cb(packet)
						except Exception as e:
							self._logger.exception("Exception while handling callback")
		return False
