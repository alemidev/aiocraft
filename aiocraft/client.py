import asyncio
import logging
import json
import uuid

from dataclasses import dataclass
from asyncio import Task
from enum import Enum
from time import time

from typing import Dict, List, Callable, Type, Optional, Tuple, AsyncIterator, Any, Set

import dns.resolver

from .dispatcher import Dispatcher
from .mc.packet import Packet
from .mc.auth import AuthInterface, AuthException, MojangAuthenticator, MicrosoftAuthenticator
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

class MinecraftClient:
	online_mode:bool
	authenticator:AuthInterface
	dispatcher : Dispatcher
	logger : logging.Logger
	_authenticated : bool
	_processing : bool
	_worker : Task

	def __init__(
		self,
		server:str,
		authenticator:AuthInterface,
		online_mode:bool = True,
		force_port:int = 0,
		resolve_srv:bool = True,
	):
		self.logger = LOGGER.getChild(f"on({server})")
		self.online_mode = online_mode
		self.authenticator = authenticator
		self._authenticated = False
		self._processing = False

		host = server
		port = force_port or 25565

		if resolve_srv:
			try:
				answ = dns.resolver.resolve(f"_minecraft._tcp.{server}", "SRV")
				# TODO can we just use the 1st record?
				host = str(answ[0].target).rstrip('.')
				port = answ[0].port
			except Exception:  # TODO what can I catch? dns.resolver.exception doesn't always exist, wtf
				self.logger.warning("Failed resolving SRV record for '%s'", server)

		self.dispatcher = Dispatcher().set_host(host, port)

	@property
	def connected(self) -> bool:
		return self.dispatcher.connected

	async def write(self, packet:Packet, wait:bool=False):
		await self.dispatcher.write(packet, wait)

	async def authenticate(self):
		if self._authenticated:
			return # Don't spam Auth endpoint!
		try:
			await self.authenticator.validate() # will raise an exc if token is invalid
		except AuthException:
			try:
				await self.authenticator.refresh()
				self.logger.warning("Refreshed Token")
			except AuthException:
				await self.authenticator.login()
				self.logger.info("Logged in")
		self._authenticated = True

	async def info(self, host:str="", port:int=0, proto:int=0, ping:bool=False) -> Dict[str, Any]:
		"""Make a mini connection to asses server status and version"""
		try:
			await self.dispatcher.set_host(host, port).connect()
			await self._handshake(ConnectionState.STATUS)
			return await self._status(ping)
		finally:
			if self.dispatcher.connected:
				await self.dispatcher.disconnect()

	async def join(self, host:str="", port:int=0, proto:int=0):
		if self.online_mode:
			await self.authenticate()
		try:
			await self.dispatcher.set_host(host, port).set_proto(proto).connect()
			await self._handshake(ConnectionState.LOGIN)
			if await self._login():
				await self._play()
		finally:
			if self.dispatcher.connected:
				await self.dispatcher.disconnect()

	async def _handshake(self, state:ConnectionState):
		await self.dispatcher.write(
			PacketSetProtocol(
				self.dispatcher._proto,
				protocolVersion=self.dispatcher._proto,
				serverHost=self.dispatcher._host,
				serverPort=self.dispatcher._port,
				nextState=state.value
			)
		)

	async def _status(self, ping:bool=False) -> Dict[str, Any]:
		self.dispatcher.state = ConnectionState.STATUS
		await self.dispatcher.write(
			PacketPingStart(self.dispatcher._proto) #empty packet
		)
		#Response
		data : Dict[str, Any] = {}
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
					PacketPing(
						self.dispatcher._proto,
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
				self.dispatcher._proto,
				username=self.authenticator.selectedProfile.name
			)
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
					self.dispatcher._proto,
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
		self.dispatcher.state = ConnectionState.PLAY
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
