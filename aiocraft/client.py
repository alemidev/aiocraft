import asyncio
import logging
from asyncio import Task
from enum import Enum

from typing import Dict, List, Callable, Type

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
	token:Token

	dispatcher : Dispatcher
	_processing : bool
	_worker : Task

	_packet_callbacks : Dict[ConnectionState, Dict[Packet, List[Callable]]]

	def __init__(
		self,
		token:Token,
		host:str,
		port:int = 25565,
	):
		self.host = host
		self.port = port
		self.token = token

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

	async def start(self):
		await self.dispatcher.start()
		self._processing = True

		await self.dispatcher.write(
			proto.handshaking.serverbound.PacketSetProtocol(
				340, # TODO!!!!
				protocolVersion=340,
				serverHost=self.host,
				serverPort=self.port,
				nextState=2, # play
			)
		)

		await self.dispatcher.write( # TODO PROTO!!!!
			proto.login.serverbound.PacketLoginStart(340, username=self.token.profile.name)
		)

		self.dispatcher.state = ConnectionState.LOGIN
		self._processing = True
		self._worker = asyncio.get_event_loop().create_task(self._client_worker())

	async def stop(self, block=True):
		await self.dispatcher.stop()
		self._processing = False
		if block:
			await self._worker

	async def _client_worker(self):
		while self._processing:
			try:
				# logger.info("Awaiting packet")
				packet = await asyncio.wait_for(self.dispatcher.incoming.get(), timeout=5)
				# logger.info("Client processing packet %s [state %s]", str(packet), str(self.dispatcher.state))

				# Process packets? switch state, invoke callbacks? Maybe implement Reactors?
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

	async def login_logic(self, packet:Packet):
		if isinstance(packet, proto.login.clientbound.PacketEncryptionBegin):
			logger.info("Encryption request")
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

			await self.dispatcher.encrypt(secret)
		
		elif isinstance(packet, proto.login.clientbound.PacketDisconnect):
			logger.error("Disconnected while logging in")
			await self.stop(False)
			# raise Exception("Disconnected while logging in") # TODO make a more specific one, do some shit

		elif isinstance(packet, proto.login.clientbound.PacketCompress):
			logger.info("Set compression")
			self.dispatcher.compression = packet.threshold

		elif isinstance(packet, proto.login.clientbound.PacketSuccess):
			logger.info("Login success")
			self.dispatcher.state = ConnectionState.PLAY

		elif isinstance(packet, proto.login.clientbound.PacketLoginPluginRequest):
			pass # TODO ?

	async def play_logic(self, packet:Packet):
		if isinstance(packet, proto.play.clientbound.PacketSetCompression):
			logger.info("Set compression")
			self.dispatcher.compression = packet.threshold

		elif isinstance(packet, proto.play.clientbound.PacketKeepAlive):
			logger.info("Keep Alive")
			keep_alive_packet = proto.play.serverbound.packet_keep_alive.PacketKeepAlive(340, keepAliveId=packet.keepAliveId)
			await self.dispatcher.write(keep_alive_packet)

		elif isinstance(packet, proto.play.clientbound.PacketPosition):
			logger.info("PlayerPosLook")
			# if self.connection.context.protocol_later_eq(107):
			# 	teleport_confirm = serverbound.play.TeleportConfirmPacket()
			# 	teleport_confirm.teleport_id = packet.teleport_id
			# 	self.connection.write_packet(teleport_confirm)
			# else:
			# 	position_response = serverbound.play.PositionAndLookPacket()
			# 	position_response.x = packet.x
			# 	position_response.feet_y = packet.y
			# 	position_response.z = packet.z
			# 	position_response.yaw = packet.yaw
			# 	position_response.pitch = packet.pitch
			# 	position_response.on_ground = True
			# 	self.connection.write_packet(position_response)
			# self.connection.spawned = True
			pass

		elif isinstance(packet, proto.play.clientbound.PacketKickDisconnect):
			logger.info("Play Disconnect")
			raise Exception("Disconnected while playing") # TODO make a more specific one, do some shit

