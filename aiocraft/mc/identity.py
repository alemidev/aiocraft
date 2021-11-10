"""Minecraft identity utilities."""
import json
import uuid

from dataclasses import dataclass
from typing import Optional

import aiohttp

@dataclass
class Profile:
	id : str
	name : str

	def dict(self):
		return {
			"id": self.id,
			"name": self.name
		}

@dataclass
class Token:
	username : str
	access_token : str
	client_token : str
	profile : Profile

	AGENT_NAME = "Minecraft"
	AGENT_VERSION = 1
	AUTH_SERVER = "https://authserver.mojang.com"
	SESSION_SERVER = "https://sessionserver.mojang.com/session/minecraft"
	CONTENT_TYPE = "application/json"
	HEADERS = {"content-type": CONTENT_TYPE}

	@classmethod
	async def authenticate(cls, username, password, invalidate=False):
		payload = {
			"agent": {
				"name": cls.AGENT_NAME,
				"version": cls.AGENT_VERSION
			},
			"username": username,
			"password": password
		}

		if not invalidate:
			payload["clientToken"] = uuid.uuid4().hex

		res = await cls._post(cls.AUTH_SERVER + "/authenticate", payload)

		return cls(
			username=username,
			access_token=res["accessToken"],
			client_token=res["clientToken"],
			profile=Profile(res["selectedProfile"]["id"], res["selectedProfile"]["name"])
		)

	@classmethod
	async def sign_out(cls, username:str, password:str) -> dict:
		return await cls._post(cls.AUTH_SERVER + "/signout", {
			"username": username,
			"password": password
		})

	async def refresh(self) -> dict:
		res = await self._post(self.AUTH_SERVER + "/refresh", {
			"accessToken": self.access_token,
			"clientToken": self.client_token
		})

		self.access_token = res["accessToken"]
		self.client_token = res["clientToken"]
		self.profile = Profile(res["selectedProfile"]["id"], res["selectedProfile"]["name"])

		return res

	async def validate(self) -> dict:
		return await self._post(self.AUTH_SERVER + "/validate", {
			"accessToken": self.access_token
		})

	async def invalidate(self) -> dict:
		return await self._post(self.AUTH_SERVER + "/invalidate", {
			"accessToken": self.access_token,
			"clientToken": self.client_token
		})

	async def join(self, server_id) -> dict:
		return await self._post(self.SESSION_SERVER + "/join", {
			"serverId": server_id,
			"accessToken": self.access_token,
			"selectedProfile": self.profile.dict()
		})

	@classmethod
	async def _post(cls, endpoint:str, data:dict) -> dict:
		async with aiohttp.ClientSession() as sess:
			async with sess.post(endpoint, headers=cls.HEADERS, data=json.dumps(data).encode('utf-8')) as res:
				# TODO parse and raise exceptions
				return await res.json(content_type=None)
