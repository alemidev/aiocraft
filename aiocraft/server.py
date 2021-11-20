import asyncio
import logging
import uuid

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

class Server:
	host:str
	port:int
	options:dict

	_dispatcher_pool : List[Dispatcher]
	_processing : bool
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
			"reconnect" : True,
			"rctime" : 5.0,
			"keep-alive" : True,
			"poll-timeout" : 1,
		}

		self._dispatcher_pool = []
		self._processing = False
		self._authenticated = False

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

	async def start(self):
		self._processing = True
		self._worker = asyncio.get_event_loop().create_task(self._server_worker())
		self._logger.info("Minecraft server started")

	async def stop(self, block=True, wait_tasks=True):
		self._processing = False
		if self.dispatcher.connected:
			await self.dispatcher.disconnect(block=block)
		if block:
			await self._worker
			self._logger.info("Minecraft server stopped")
		if block and wait_tasks:
			await asyncio.gather(*list(self._callbacks.values()))

	async def _server_worker(self):
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
		pass

	async def _login(self) -> bool:
		pass

	async def _play(self) -> bool:
		pass
