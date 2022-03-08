import asyncio
import logging
import json
import uuid

from dataclasses import dataclass
from asyncio import Task
from enum import Enum
from time import time

from typing import Dict, List, Callable, Type, Optional, Tuple, AsyncIterator, Any, Set

from .dispatcher import Dispatcher
from .mc.packet import Packet
from .mc.auth import AuthInterface, AuthException, MojangToken, MicrosoftAuthenticator
from .mc.definitions import Dimension, Difficulty, Gamemode, ConnectionState
from .mc.proto.status.serverbound import PacketPing, PacketPingStart
from .mc.proto.status.clientbound import PacketServerInfo, PacketPing as PacketPong
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
	reconnect : bool = True
	reconnect_delay : float = 10.0
	keep_alive : bool = True
	poll_interval : float = 1.0
	use_packet_whitelist : bool = True

class MinecraftClient:
	host:str
	port:int
	options:ClientOptions

	_authenticator:MicrosoftAuthenticator
	_username:str
	code:Optional[str]

	dispatcher : Dispatcher
	_processing : bool
	_authenticated : bool
	_worker : Task

	_logger : logging.Logger

	def __init__(
		self,
		server:str,
		login_code:str = '',
		online_mode:bool = True,
		username:str = '',
		client_id:str = '', # TODO maybe hardcode defaults?
		client_secret:str='',
		redirect_uri:str='http://localhost',
		**kwargs
	):
		super().__init__()
		if ":" in server:
			_host, _port = server.split(":", 1)
			self.host = _host.strip()
			self.port = int(_port)
		else:
			self.host = server.strip()
			self.port = 25565

		self.options = ClientOptions(**kwargs)

		self.code = login_code or None # TODO put this directly in the authenticator maybe?
		self._username = username
		self._authenticator = MicrosoftAuthenticator(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
		self.online_mode = online_mode

		self.dispatcher = Dispatcher()
		self._processing = False
		self._authenticated = False

		self._logger = LOGGER.getChild(f"on({self.host}:{self.port})")

	@property
	def connected(self) -> bool:
		return self.dispatcher.connected

	async def write(self, packet:Packet, wait:bool=False):
		await self.dispatcher.write(packet, wait)

	async def authenticate(self):
		if self._authenticated:
			return # Don't spam Auth endpoint!
		try:
			await self._authenticator.validate() # will raise an exc if token is invalid
		except AuthException:
			if self.code:
				await self._authenticator.login(self.code)
				self.code = None
				self._logger.info("Logged in with OAuth code")
			elif self._authenticator.refreshable:
				await self._authenticator.refresh()
				self._logger.warning("Refreshed Token")
			else:
				raise ValueError("No refreshable auth or code to login")
		self._authenticated = True

	async def info(self, host:str="", port:int=0, proto:int=0, ping:bool=False) -> Dict[str, Any]:
		"""Make a mini connection to asses server status and version"""
		self.host = host or self.host
		self.port = port or self.port
		try:
			await self.dispatcher.connect(self.host, self.port)
			await self._handshake(ConnectionState.STATUS)
			return await self._status(ping)
		finally:
			await self.dispatcher.disconnect()

	async def join(self, host:str="", port:int=0, proto:int=0, packet_whitelist:Optional[Set[Type[Packet]]]=None): # jank packet_whitelist argument! TODO
		self.host = host or self.host
		self.port = port or self.port
		if self.online_mode:
			await self.authenticate()
		try:
			await self.dispatcher.connect(
				host=self.host,
				port=self.port,
				proto=proto,
				queue_timeout=self.options.poll_interval,
				packet_whitelist=packet_whitelist
			)
			await self._handshake(ConnectionState.LOGIN)
			if await self._login():
				await self._play()
		finally:
			await self.dispatcher.disconnect()

	async def _handshake(self, state:ConnectionState):
		await self.dispatcher.write(
			PacketSetProtocol(
				self.dispatcher.proto,
				protocolVersion=self.dispatcher.proto,
				serverHost=self.host,
				serverPort=self.port,
				nextState=state.value
			)
		)

	async def _status(self, ping:bool=False) -> Dict[str, Any]:
		self.dispatcher.state = ConnectionState.STATUS
		await self.dispatcher.write(
			PacketPingStart(self.dispatcher.proto) #empty packet
		)
		#Response
		data : Dict[str, Any] = {}
		ping_id : int = 0
		ping_time : float = 0
		async for packet in self.dispatcher.packets():
			if isinstance(packet, PacketServerInfo):
				data = json.loads(packet.response)
				self._logger.debug("Server data : %s", json.dumps(data, indent=2))
				if not ping:
					break
				ping_id = int(time())
				ping_time = time()
				await self.dispatcher.write(
					PacketPing(
						self.dispatcher.proto,
						time=ping_id,
					)
				)
			if isinstance(packet, PacketPong):
				if packet.time == ping_id:
					data['ping'] = int(time() - ping_time)
				break
		return data

	async def _login(self) -> bool:
		self.dispatcher.state = ConnectionState.LOGIN
		await self.dispatcher.write(
			PacketLoginStart(
				self.dispatcher.proto,
				username=self._authenticator.selectedProfile.name if self.online_mode else self._username
			)
		)
		async for packet in self.dispatcher.packets():
			if isinstance(packet, PacketEncryptionBegin):
				if not self.online_mode:
					self._logger.error("Cannot answer Encryption Request in offline mode")
					return False
				if not self._authenticator:
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
						await self._authenticator.join(
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
					self.dispatcher.proto,
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

	async def _play(self):
		self.dispatcher.state = ConnectionState.PLAY
		async for packet in self.dispatcher.packets():
			self._logger.debug("[ * ] Processing %s", packet.__class__.__name__)
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
