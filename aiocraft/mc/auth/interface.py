"""Minecraft authentication interface"""
from typing import Optional, Dict, Any

import aiohttp

from ..definitions import GameProfile

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

	# async def authenticate(self, user:str, pwd:str):
	# 	raise NotImplementedError

	async def refresh(self):
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
		async with aiohttp.ClientSession() as sess:
			async with sess.post(endpoint, **kwargs) as res:
				data = await res.json(content_type=None)
				if res.status >= 400:
					raise AuthException(endpoint, res.status, data, kwargs)
				return data

	@classmethod
	async def _get(cls, endpoint:str, **kwargs) -> Dict[str, Any]:
		async with aiohttp.ClientSession() as sess:
			async with sess.get(endpoint, **kwargs) as res:
				data = await res.json(content_type=None)
				if res.status >= 400:
					raise AuthException(endpoint, res.status, data, kwargs)
				return data
