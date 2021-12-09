import asyncio
import logging
import json
import uuid

from dataclasses import dataclass
from asyncio import Task
from enum import Enum

from typing import Dict, List, Callable, Type, Optional, Tuple, AsyncIterator

from .dispatcher import Dispatcher
from .traits import CallbacksHolder, Runnable
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
from .util import encryption, helpers

LOGGER = logging.getLogger(__name__)

@dataclass
class ClientOptions:
	reconnect : bool
	reconnect_delay : float
	keep_alive : bool
	poll_interval : float

class ClientEvent(Enum):
	CONNECTED = 0
	DISCONNECTED = 1

class MinecraftClient(CallbacksHolder, Runnable):
	host:str
	port:int
	options:ClientOptions

	username:Optional[str]
	password:Optional[str]
	token:Optional[Token]

	dispatcher : Dispatcher
	_processing : bool
	_authenticated : bool
	_worker : Task
	_callbacks = Dict[str, Task]

	_logger : logging.Logger

	def __init__(
		self,
		host:str,
		port:int = 25565,
		username:Optional[str] = None,
		password:Optional[str] = None,
		token:Optional[Token] = None,
		online_mode:bool = True,
		reconnect:bool = True,
		reconnect_delay:float = 10.0,
		keep_alive:bool = True,
		poll_interval:float = 1.0,

	):
		super().__init__()
		self.host = host
		self.port = port

		self.options = ClientOptions(
			reconnect=reconnect,
			reconnect_delay=reconnect_delay,
			keep_alive=keep_alive,
			poll_interval=poll_interval
		)

		self.token = token
		self.username = username
		self.password = password
		self.online_mode = online_mode

		self.dispatcher = Dispatcher()
		self._processing = False
		self._authenticated = False

		self._logger = LOGGER.getChild(f"on({self.host}:{self.port})")

	@property
	def started(self) -> bool:
		return self._processing

	@property
	def connected(self) -> bool:
		return self.started and self.dispatcher.connected

	def on_connected(self) -> Callable:
		def wrapper(fun):
			self.register(ClientEvent.CONNECTED, fun)
			return fun
		return wrapper

	def on_disconnected(self) -> Callable:
		def wrapper(fun):
			self.register(ClientEvent.DISCONNECTED, fun)
			return fun
		return wrapper

	def on_packet(self, packet:Type[Packet]) -> Callable:
		def wrapper(fun):
			self.register(packet, fun)
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

	async def start(self):
		if self.started:
			return
		self._processing = True
		self._worker = asyncio.get_event_loop().create_task(self._client_worker())
		self._logger.info("Minecraft client started")

	async def stop(self, force:bool=False):
		self._processing = False
		if self.dispatcher.connected:
			await self.dispatcher.disconnect(block=not force)
		if not force:
			await self._worker
			self._logger.info("Minecraft client stopped")
		if not force:
			await self.join_callbacks()

	async def _client_worker(self):
		while self._processing:
			if self.online_mode:
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
			except OSError as e:
				self._logger.error("Connection error : %s", str(e))
			except Exception:
				self._logger.exception("Exception in Client connection")
			if self.dispatcher.connected:
				await self.dispatcher.disconnect()
			if not self.options.reconnect:
				break
			if self._processing: # if client was stopped exit immediately
				await asyncio.sleep(self.options.reconnect_delay)
		await self.stop(force=True)

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
				username=self.token.profile.name if self.online_mode and self.token else self.username
			)
		)
		return True

	async def _login(self) -> bool:
		self.dispatcher.state = ConnectionState.LOGIN
		async for packet in self.dispatcher.packets():
			if isinstance(packet, PacketEncryptionBegin):
				if not self.online_mode:
					self._logger.error("Cannot answer Encryption Request in offline mode")
					return False
				if not self.token:
					self._logger.error("No available token to enable encryption")
					return False
				secret = encryption.generate_shared_secret()
				token, encrypted_secret = encryption.encrypt_token_and_secret(
					packet.publicKey,
					packet.verifyToken,
					secret
				)
				if packet.serverId != '-':
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
						self._authenticated = False
						return False
				else:
					self._logger.warning("Server gave an offline-mode serverId but still requested Encryption")
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
				self._logger.error("Kicked while logging in : %s", helpers.parse_chat(packet.reason))
				return False
		return False

	async def _play(self) -> bool:
		self.dispatcher.state = ConnectionState.PLAY
		self.run_callbacks(ClientEvent.CONNECTED)
		async for packet in self.dispatcher.packets():
			self._logger.debug("[ * ] Processing | %s", str(packet))
			if isinstance(packet, PacketSetCompression):
				self._logger.info("Compression updated")
				self.dispatcher.compression = packet.threshold
			elif isinstance(packet, PacketKeepAlive):
				if self.options.keep_alive:
					keep_alive_packet = PacketKeepAliveResponse(340, keepAliveId=packet.keepAliveId)
					await self.dispatcher.write(keep_alive_packet)
			elif isinstance(packet, PacketKickDisconnect):
				self._logger.error("Kicked while in game : %s", helpers.parse_chat(packet.reason))
				break
			self.run_callbacks(Packet, packet)
			self.run_callbacks(type(packet), packet)
		self.run_callbacks(ClientEvent.DISCONNECTED)
		return False
