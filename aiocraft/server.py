import asyncio
import logging
import uuid

from asyncio import Task, StreamReader, StreamWriter, Server
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

class Server:
	host:str
	port:int
	options:dict

	_dispatcher_pool : List[Dispatcher]
	_processing : bool
	_server : Server
	_worker : Task
	_callbacks = Dict[str, Task]

	_logger : logging.Logger

	def __init__(
		self,
		host:str,
		port:int = 25565,
		options:dict = None,
	):
		self.host = host
		self.port = port

		self.options = options or {
			"online-mode" : False,
		}

		self._dispatcher_pool = []
		self._processing = False

		self._logger = LOGGER.getChild(f"@({self.host}:{self.port})")

	@property
	def started(self) -> bool:
		return self._processing

	def run(self):
		loop = asyncio.get_event_loop()

		loop.run_until_complete(self.start())

		async def idle():
			while self._processing: # TODO don't busywait even if it doesn't matter much
				await asyncio.sleep(self.options["poll-timeout"])

		try:
			loop.run_forever(idle())
		except KeyboardInterrupt:
			self._logger.info("Received SIGINT, stopping...")
			try:
				loop.run_until_complete(self.stop())
			except KeyboardInterrupt:
				self._logger.info("Received SIGINT, stopping for real")
				loop.run_until_complete(self.stop(wait_tasks=False))

	async def start(self, block=False):
		self._server = await asyncio.start_server(
			self._server_worker, self.host, self.port
		)
	
		addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
		print(f'Serving on {addrs}')
	
		self._processing = True
		async with self._server:
			self._logger.info("Minecraft server started")
			if block:
				await self._server.serve_forever()
			else:
				await self._server.start_serving()

	async def stop(self, block=True, wait_tasks=True):
		self._processing = False
		if self.dispatcher.connected:
			await self.dispatcher.disconnect(block=block)
		self._server.close()
		if block:
			await self._server.wait_closed()
		# if block and wait_tasks: # TODO wait for client workers
		# 	await asyncio.gather(*list(self._callbacks.values()))

	async def _disconnect_client(self, dispatcher):
		if dispatcher.state == ConnectionState.LOGIN:
			await dispatcher.write(PacketDisconnect(dispatcher.proto, reason="Connection terminated"))
		else:
			await dispatcher.write(PacketKickDisconnect(dispatcher.proto, reason="Connection terminated"))

	async def _server_worker(self, reader:StreamReader, writer:StreamWriter):
		dispatcher = Dispatcher()

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
		async for packet in dispatcher.packets():
			if isinstance(packet, PacketSetProtocol):
				dispatcher.proto = packet.protocolVersion
				if packet.nextState == ConnectionState.STATUS:
					dispatcher.state = ConnectionState.STATUS
					return True
				elif packet.nextState == ConnectionState.LOGIN:
					dispatcher.state = ConnectionState.LOGIN
					return True
		return False

	async def _status(self, dispatcher:Dispatcher) -> bool:
		async for packet in dispatcher.packets():
			pass # TODO handle status!
		return False

	async def _login(self, dispatcher:Dispatcher) -> bool:
		async for packet in dispatcher.packets():
			if isinstance(packet, PacketLoginStart):
				if self.options["online-mode"]:
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
							uuid=packet.username,
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
		async for packet in dispatcher.packets():
			pass # TODO handle play
		return False

