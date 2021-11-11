import asyncio
import logging
from asyncio import Task
from enum import Enum

from typing import Dict, List, Callable, Type, Optional, Tuple

from .dispatcher import Dispatcher, ConnectionState
from .mc.mctypes import VarInt
from .mc.packet import Packet
from .mc.identity import Token
from .mc import proto, encryption

logger = logging.getLogger(__name__)

def _registry_from_state(state:ConnectionState) -> Dict[int, Dict[int, Type[Packet]]]:
	if state == ConnectionState.HANDSHAKING:
		return proto.handshaking.clientbound.REGISTRY
	if state == ConnectionState.STATUS:
		return proto.status.clientbound.REGISTRY
	if state == ConnectionState.LOGIN:
		return proto.login.clientbound.REGISTRY
	if state == ConnectionState.PLAY:
		return proto.play.clientbound.REGISTRY
	return {}

_STATE_REGS = {
	ConnectionState.HANDSHAKING : proto.handshaking,
	ConnectionState.STATUS : proto.status,
	ConnectionState.LOGIN : proto.login,
	ConnectionState.PLAY : proto.play,
}

class Client:
	host:str
	port:int
	username:Optional[str]
	password:Optional[str]
	token:Optional[Token]

	dispatcher : Dispatcher
	_processing : bool
	_worker : Task

	_packet_callbacks : Dict[ConnectionState, Dict[Packet, List[Callable]]]

	def __init__(
		self,
		host:str,
		port:int = 25565,
		username:Optional[str] = None,
		password:Optional[str] = None,
		token:Optional[Token] = None,
	):
		self.host = host
		self.port = port

		self.token = token
		self.username = username
		self.password = password

		self.dispatcher = Dispatcher(host, port)
		self._processing = False

		self._packet_callbacks = {}

	def on(self, hook):
		def wrapper(fun):
			pass # TODO
		return wrapper

	def on_packet(self, packet:Type[Packet], state:ConnectionState) -> Callable:
		def wrapper(fun):
			if state not in self._packet_callbacks:
				self._packet_callbacks[state] = {}
			if packet not in self._packet_callbacks[state]:
				self._packet_callbacks[state][packet] = []
			self._packet_callbacks[state][packet].append(fun)
			return fun
		return wrapper

	async def authenticate(self) -> bool:
		if not self.token:
			if self.username and self.password:
				self.token = await Token.authenticate(self.username, self.password)
				logger.info("Authenticated from credentials")
				return True
			return False
		try:
			await self.token.validate() # will raise an exc if token is invalid
		except Exception: # idk TODO
			try:
				await self.token.refresh()
				logger.info("Refreshed Token")
			except Exception:
				return False
		return True

	async def run(self):
		await self.start()

		try:
			while True: # TODO don't busywait even if it doesn't matter much
				await asyncio.sleep(5)
		except KeyboardInterrupt:
			logger.info("Received SIGINT, stopping...")

		await self.stop()

	async def start(self):
		self._processing = True
		self._worker = asyncio.get_event_loop().create_task(self._client_worker())
		logger.info("Minecraft client started")

	async def stop(self, block=True):
		self._processing = False
		await self.dispatcher.disconnect()
		if block:
			await self._worker
		logger.info("Minecraft client stopped")

	async def _client_worker(self):
		while self._processing:
			if not await self.authenticate():
				raise Exception("Token not refreshable or credentials invalid") # TODO!
			try:
				await self.dispatcher.connect()
				for packet in self._handshake():
					await self.dispatcher.write(packet)
				self.dispatcher.state = ConnectionState.LOGIN
				await self._process_packets()
			except Exception:
				logger.exception("Connection terminated")
			await asyncio.sleep(2)

	def _handshake(self, force:bool=False) -> Tuple[Packet, Packet]: # TODO make this fancier! poll for version and status first
		return ( proto.handshaking.serverbound.PacketSetProtocol(
				340, # TODO!!!!
				protocolVersion=340,
				serverHost=self.host,
				serverPort=self.port,
				nextState=2, # play
			),
			proto.login.serverbound.PacketLoginStart(
				340,
				username=self.token.profile.name if self.token else self.username
			)
		)

	async def _process_packets(self):
		while self.dispatcher.connected:
			try:
				packet = await asyncio.wait_for(self.dispatcher.incoming.get(), timeout=5)
				logger.debug("[ * ] Processing | %s", str(packet))

				if self.dispatcher.state == ConnectionState.LOGIN:
					await self.login_logic(packet)
				elif self.dispatcher.state == ConnectionState.PLAY:
					await self.play_logic(packet)

				if self.dispatcher.state in self._packet_callbacks:
					if Packet in self._packet_callbacks[self.dispatcher.state]: # callback for any packet
						for cb in self._packet_callbacks[self.dispatcher.state][Packet]:
							await cb(packet)
					if packet.__class__ in self._packet_callbacks[self.dispatcher.state]: # callback for this packet
						for cb in self._packet_callbacks[self.dispatcher.state][packet.__class__]:
							await cb(packet)
				self.dispatcher.incoming.task_done()
			except asyncio.TimeoutError:
				pass # need this to recheck self._processing periodically
			except Exception:
				logger.exception("Exception while processing packet %s", packet)

	# TODO move these in separate module

	async def login_logic(self, packet:Packet):
		if isinstance(packet, proto.login.clientbound.PacketEncryptionBegin):
			secret = encryption.generate_shared_secret()

			token, encrypted_secret = encryption.encrypt_token_and_secret(
				packet.publicKey,
				packet.verifyToken,
				secret
			)

			if packet.serverId != '-' and self.token:
				await self.token.join(
					encryption.generate_verification_hash(
						packet.serverId,
						secret,
						packet.publicKey
					)
				)

			encryption_response = proto.login.serverbound.PacketEncryptionBegin(
				340, # TODO!!!!
				sharedSecret=encrypted_secret,
				verifyToken=token
			)

			await self.dispatcher.write(encryption_response, wait=True)

			self.dispatcher.encrypt(secret)
		
		elif isinstance(packet, proto.login.clientbound.PacketDisconnect):
			logger.error("Disconnected while logging in")
			await self.dispatcher.disconnect(block=False)
			# raise Exception("Disconnected while logging in") # TODO make a more specific one, do some shit

		elif isinstance(packet, proto.login.clientbound.PacketCompress):
			logger.info("Compression enabled")
			self.dispatcher.compression = packet.threshold

		elif isinstance(packet, proto.login.clientbound.PacketSuccess):
			logger.info("Login success, joining world...")
			self.dispatcher.state = ConnectionState.PLAY

		elif isinstance(packet, proto.login.clientbound.PacketLoginPluginRequest):
			pass # TODO ?

	async def play_logic(self, packet:Packet):
		if isinstance(packet, proto.play.clientbound.PacketSetCompression):
			logger.info("Compression updated")
			self.dispatcher.compression = packet.threshold

		elif isinstance(packet, proto.play.clientbound.PacketKeepAlive):
			keep_alive_packet = proto.play.serverbound.packet_keep_alive.PacketKeepAlive(340, keepAliveId=packet.keepAliveId)
			await self.dispatcher.write(keep_alive_packet)

		elif isinstance(packet, proto.play.clientbound.PacketPosition):
			logger.info("Position synchronized")
			await self.dispatcher.write(
				proto.play.serverbound.PacketTeleportConfirm(
					340,
					teleportId=packet.teleportId
				)
			)

		elif isinstance(packet, proto.play.clientbound.PacketUpdateHealth):
			if packet.health <= 0:
				logger.info("Dead, respawning...")
				await self.dispatcher.write(
					proto.play.serverbound.PacketClientCommand(self.dispatcher.proto, actionId=0) # respawn
				)

		elif isinstance(packet, proto.play.clientbound.PacketKickDisconnect):
			logger.error("Disconnected")
			await self.dispatcher.disconnect(block=False)

