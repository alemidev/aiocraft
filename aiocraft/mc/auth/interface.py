"""Minecraft authentication interface"""
import logging
from multiprocessing.sharedctypes import Value
from typing import Optional, Dict, Any

import aiohttp
from json.decoder import JSONDecodeError

from ..definitions import GameProfile

logger = logging.getLogger(__file__)

class AuthException(Exception):
	endpoint : str
	code     : int
	data     : dict
	kwargs   : dict

	def __init__(self, endpoint:str, code:int, data:dict, kwargs:dict):
		self.endpoint = endpoint
		self.code = code
		self.data = data
		self.kwargs = kwargs
		super().__init__(f"[{self.code}:{self.endpoint}] {self.data} : (**{self.kwargs})")

class AuthInterface:
	accessToken : str
	selectedProfile : GameProfile

	SESSION_SERVER = "https://sessionserver.mojang.com/session/minecraft"
	TIMEOUT = aiohttp.ClientTimeout(total=3)

	async def login(self) -> 'AuthInterface':
		raise NotImplementedError

	async def refresh(self) -> 'AuthInterface':
		raise NotImplementedError

	async def validate(self) -> 'AuthInterface':
		raise NotImplementedError

	def serialize(self) -> Dict[str, Any]:
		raise NotImplementedError

	def deserialize(self, data:Dict[str, Any]):
		raise NotImplementedError

	async def join(self, server_id) -> dict:
		return await self._post(
			self.SESSION_SERVER + "/join",
			headers={"content-type":"application/json"},
			json={
				"serverId": server_id,
				"accessToken": self.accessToken,
				"selectedProfile": self.selectedProfile.as_dict()
			}
		)

	@classmethod # TODO more love for server side!
	async def server_join(cls, username:str, serverId:str, ip:Optional[str] = None):
		params = {"username":username, "serverId":serverId}
		if ip:
			params["ip"] = ip
		return await cls._get(cls.SESSION_SERVER + "/hasJoined", params=params)

	@classmethod
	async def _post(cls, endpoint:str, **kwargs) -> Dict[str, Any]:
		async with aiohttp.ClientSession(timeout=cls.TIMEOUT) as session:
			async with session.post(endpoint, **kwargs) as res:
				try:
					data = await res.json(content_type=None)
				except JSONDecodeError:
					raise AuthException(endpoint, res.status, {"invalid": await res.text()}, kwargs)
				logger.debug("POST /%s [%s] : %s", endpoint, str(kwargs), str(data))
				if res.status >= 400:
					raise AuthException(endpoint, res.status, data, kwargs)
				return data

	@classmethod
	async def _get(cls, endpoint:str, **kwargs) -> Dict[str, Any]:
		async with aiohttp.ClientSession(timeout=cls.TIMEOUT) as session:
			async with session.get(endpoint, **kwargs) as res:
				try:
					data = await res.json(content_type=None)
				except JSONDecodeError:
					raise AuthException(endpoint, res.status, {"invalid": await res.text()}, kwargs)
				logger.debug("GET /%s [%s] : %s", endpoint, str(kwargs), str(data))
				if res.status >= 400:
					raise AuthException(endpoint, res.status, data, kwargs)
				return data

class OfflineAuthenticator(AuthInterface):
	def __init__(self, name:str, id:str=''):
		self.accessToken = ''
		self.selectedProfile = GameProfile(id=id, name=name)

	async def login(self) -> 'AuthInterface':
		raise AuthException('login', 418, {"error":"offline authenticator cannot login"}, kwargs={})

	async def refresh(self) -> 'AuthInterface':
		raise AuthException('refresh', 418, {"error":"offline authenticator cannot refresh"}, kwargs={})

	async def validate(self) -> 'AuthInterface':
		raise AuthException('validate', 418, {"error":"offline authenticator cannot validate"}, kwargs={})

	def serialize(self) -> Dict[str, Any]:
		return {}

	def deserialize(self, data:Dict[str, Any]) -> 'AuthInterface':
		pass

