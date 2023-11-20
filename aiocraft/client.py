import logging
import json

from asyncio import Task
from time import time

from typing import Any, Type

import dns.resolver

from .dispatcher import Dispatcher
from .auth import AuthInterface, AuthException
from .types import ConnectionState
from .packet import Packet
from .proto.status.serverbound import PacketPing, PacketPingStart
from .proto.status.clientbound import PacketServerInfo, PacketPing as PacketPong
from .proto.handshaking.serverbound import PacketSetProtocol
from .proto.play.serverbound import PacketKeepAlive as PacketKeepAliveResponse
from .proto.play.clientbound import PacketKeepAlive, PacketSetCompression, PacketKickDisconnect
from .proto.login.serverbound import PacketLoginStart, PacketEncryptionBegin as PacketEncryptionResponse
from .proto.login.clientbound import (
	PacketCompress, PacketDisconnect, PacketEncryptionBegin, PacketLoginPluginRequest, PacketSuccess
)
from .util import encryption, helpers

LOGGER = logging.getLogger(__name__)

class AbstractMinecraftClient:
	online_mode: bool
	authenticator: AuthInterface
	logger: logging.Logger
	_dispatcher: Dispatcher | None
	_authenticated: bool
	_processing: bool
	_worker: Task

	def __init__(
		self,
		authenticator:AuthInterface,
		online_mode:bool = True,
	):
		self.logger = LOGGER.getChild(f"as({authenticator.selectedProfile.name})")
		self.online_mode = online_mode
		self.authenticator = authenticator
		self._authenticated = False
		self._processing = False
		self._dispatcher = None

	def resolve_srv(self, server: str) -> tuple[str, int]:
		try:
			answ = dns.resolver.resolve(f"_minecraft._tcp.{server}", "SRV")
			# TODO can we just use the 1st record?
			host = str(answ[0].target).rstrip('.')
			port = answ[0].port
			return (host, port)
		except Exception:  # TODO what can I catch? dns.resolver.exception doesn't always exist, wtf
			self.logger.warning("Failed resolving SRV record for '%s'", server)
			return (server, 25565)

	@property
	def connected(self) -> bool:
		return self._dispatcher is not None and self.dispatcher.connected

	@property
	def dispatcher(self) -> Dispatcher:
		# This is a weird fix to avoid asserting dispatcher is not None in all handlers:
		# if i'm receiving a packet callback dispatcher is very likely not None, if I received 
		# a callback and it's None it's because client is stopping so an exc is ok
		if self._dispatcher is None:
			raise ValueError("Invalid state: connect first")
		return self._dispatcher

	async def authenticate(self):
		if self._authenticated:
			return # Don't spam Auth endpoint!
		try:
			await self.authenticator.validate() # will raise an exc if token is invalid
		except AuthException:
			try:
				await self.authenticator.refresh()
				self.logger.warning("Refreshed Token")
			except AuthException as e:
				if not self.authenticator.code:
					raise e  # no code to login, re-raise refresh exc
				await self.authenticator.login()
				self.logger.info("Logged in")
		self._authenticated = True

	async def info(
			self,
			host:str,
			port:int=0,
			proto:int=0,
			ping:bool=False,
			log_ignored_packets:bool=False,
			whitelist: set[Type[Packet]] = set(),
	) -> dict[str, Any]:
		"""Make a mini connection to asses server status and version"""
		if not port:
			host, port = self.resolve_srv(host)
		self._dispatcher = Dispatcher(
			host=host,
			port=port,
			proto=proto,
			log_ignored_packets=log_ignored_packets,
			whitelist=whitelist
		)
		try:
			await self.dispatcher.connect()
			await self._handshake(ConnectionState.STATUS)
			return await self._status(ping)
		finally:
			if self.dispatcher.connected:
				await self.dispatcher.disconnect()
			self._dispatcher = None

	async def join(
			self,
			host:str,
			port:int=0,
			proto:int=0,
			log_ignored_packets:bool=False,
			whitelist: set[Type[Packet]]=set(),
	):
		if not port:
			host, port = self.resolve_srv(host)
		self._dispatcher = Dispatcher(
			host=host,
			port=port,
			proto=proto,
			log_ignored_packets=log_ignored_packets,
			whitelist=whitelist,
		)
		if self.online_mode:
			await self.authenticate()
		try:
			await self.dispatcher.connect()
			await self._handshake(ConnectionState.LOGIN)
			if await self._login():
				await self._play()
		finally:
			if self.dispatcher.connected:
				await self.dispatcher.disconnect()
			self._dispatcher = None

	async def _handshake(self, state:ConnectionState):
		await self.dispatcher.write(
			PacketSetProtocol(
				protocolVersion=self.dispatcher.proto,
				serverHost=self.dispatcher.host,
				serverPort=self.dispatcher.port,
				nextState=state.value
			)
		)

	async def _status(self, ping:bool=False) -> dict[str, Any]:
		self.dispatcher.promote(ConnectionState.STATUS)
		await self.dispatcher.write(PacketPingStart()) #empty packet
		#Response
		data : dict[str, Any] = {}
		ping_id : int = 0
		ping_time : float = 0
		async for packet in self.dispatcher.packets():
			if isinstance(packet, PacketServerInfo):
				data = json.loads(packet.response)
				self.logger.debug("Server data : %s", json.dumps(data, indent=2))
				if not ping:
					break
				ping_id = int(time())
				ping_time = time()
				await self.dispatcher.write(
					PacketPing(time=ping_id)
				)
			if isinstance(packet, PacketPong):
				if packet.time == ping_id:
					data['ping'] = int(time() - ping_time)
				break
		return data

	async def _login(self) -> bool:
		self.dispatcher.promote(ConnectionState.LOGIN)
		await self.dispatcher.write(
			PacketLoginStart(username=self.authenticator.selectedProfile.name)
		)
		async for packet in self.dispatcher.packets():
			if isinstance(packet, PacketEncryptionBegin):
				if not self.online_mode or not self.authenticator or not self.authenticator.accessToken:  # overkill to check authenticator and accessToken but whatever
					self.logger.error("Cannot answer Encryption Request in offline mode")
					return False
				secret = encryption.generate_shared_secret()
				token, encrypted_secret = encryption.encrypt_token_and_secret(
					packet.publicKey,
					packet.verifyToken,
					secret
				)
				if packet.serverId != '-':
					try:
						await self.authenticator.join(
							encryption.generate_verification_hash(
								packet.serverId,
								secret,
								packet.publicKey
							)
						)
					except AuthException:
						self.logger.error("Could not authenticate with Mojang")
						self._authenticated = False
						return False
				else:
					self.logger.warning("Server gave an offline-mode serverId but still requested Encryption")
				encryption_response = PacketEncryptionResponse(
					sharedSecret=encrypted_secret,
					verifyToken=token
				)
				await self.dispatcher.write(encryption_response, wait=True)
				self.dispatcher.encrypt(secret)
			elif isinstance(packet, PacketCompress):
				self.logger.info("Compression enabled")
				self.dispatcher._compression = packet.threshold
			elif isinstance(packet, PacketLoginPluginRequest):
				self.logger.info("Ignoring plugin request") # TODO ?
			elif isinstance(packet, PacketSuccess):
				self.logger.info("Login success, joining world...")
				return True
			elif isinstance(packet, PacketDisconnect):
				self.logger.error("Kicked while logging in : %s", helpers.parse_chat(packet.reason))
				return False
		return False

	async def _play(self):
		self.dispatcher.promote(ConnectionState.PLAY)
		async for packet in self.dispatcher.packets():
			self.logger.debug("[ * ] Processing %s", packet.__class__.__name__)
			if isinstance(packet, PacketSetCompression):
				self.logger.info("Compression updated")
				self.dispatcher._compression = packet.threshold
			elif isinstance(packet, PacketKeepAlive):
				keep_alive_packet = PacketKeepAliveResponse(340, keepAliveId=packet.keepAliveId)
				await self.dispatcher.write(keep_alive_packet)
			elif isinstance(packet, PacketKickDisconnect):
				self.logger.error("Kicked while in game : %s", helpers.parse_chat(packet.reason))
				break
