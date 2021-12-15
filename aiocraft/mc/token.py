"""Minecraft identity utilities."""
import json
import uuid
import logging

from dataclasses import dataclass
from typing import Optional

import aiohttp

class AuthException(Exception):
	action : str
	type : str
	message : str

	def __init__(self, action:str, data:dict):
		self.type = data["error"] if data and "error" in data else "Unknown"
		self.message = data["errorMessage"] if data and "errorMessage" in data else "Token or credentials invalid"
		self.action = action.rsplit('/',1)[1]
		super().__init__(f"[{self.action}] {self.type} : {self.message}")

@dataclass
class GameProfile:
	id : str
	name : str

	def as_dict(self):
		return {
			"id": self.id,
			"name": self.name
		}

@dataclass
class Token:
	username : str
	accessToken : str
	clientToken : str
	selectedProfile : GameProfile

	AGENT_NAME = "Minecraft"
	AGENT_VERSION = 1
	AUTH_SERVER = "https://authserver.mojang.com"
	SESSION_SERVER = "https://sessionserver.mojang.com/session/minecraft"
	CONTENT_TYPE = "application/json"
	HEADERS = {"content-type": CONTENT_TYPE}

	def __equals__(self, other) -> bool:
		if not isinstance(other, self.__class__):
			return False
		if self.accessToken == other.accessToken \
		and self.clientToken == other.clientToken \
		and self.selectedProfile == other.selectedProfile:
			# username doesn't matter, it can be included or not and we can fetch it at later time
			return True
		return False

	def __repr__(self) -> str:
		return json.dumps(self.as_dict())

	def __str__(self) -> str:
		return repr(self)

	def as_dict(self):
		return {
			"username":self.username,
			"accessToken":self.accessToken,
			"clientToken":self.clientToken,
			"selectedProfile": self.selectedProfile.as_dict(),
		}

	@classmethod
	def from_file(cls, fname:str):
		with open(fname) as f:
			return cls.from_dict(json.load(f))

	@classmethod
	def from_dict(cls, data:dict):
		return cls(
			username=data["username"] if "username" in data else data["selectedProfile"]["name"],
			accessToken=data["accessToken"],
			clientToken=data["clientToken"],
			selectedProfile=GameProfile(**data["selectedProfile"]),
		)

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
			accessToken=res["accessToken"],
			clientToken=res["clientToken"],
			selectedProfile=GameProfile(**res["selectedProfile"])
		)

	@classmethod
	async def sign_out(cls, username:str, password:str) -> dict:
		return await cls._post(cls.AUTH_SERVER + "/signout", {
			"username": username,
			"password": password
		})

	async def refresh(self, requestUser:bool = False) -> dict:
		res = await self._post(self.AUTH_SERVER + "/refresh", {
			"accessToken": self.accessToken,
			"clientToken": self.clientToken
		})

		self.accessToken = res["accessToken"]
		self.clientToken = res["clientToken"]
		self.selectedProfile = GameProfile(**res["selectedProfile"])

		if "user" in res:
			self.username = res["user"]["username"]

		return res

	async def validate(self, clientToken:bool = True) -> dict:
		payload = { "accessToken": self.accessToken }
		if clientToken:
			payload["clientToken"] = self.clientToken
		return await self._post(self.AUTH_SERVER + "/validate", payload)

	async def invalidate(self) -> dict:
		return await self._post(self.AUTH_SERVER + "/invalidate", {
			"accessToken": self.accessToken,
			"clientToken": self.clientToken
		})

	async def join(self, server_id) -> dict:
		return await self._post(self.SESSION_SERVER + "/join", {
			"serverId": server_id,
			"accessToken": self.accessToken,
			"selectedProfile": self.selectedProfile.as_dict()
		})

	@classmethod
	async def server_join(cls, username:str, serverId:str, ip:Optional[str] = None):
		params = {"username":username, "serverId":serverId}
		if ip:
			params["ip"] = ip
		return await cls._get(cls.SESSION_SERVER + "/hasJoined", params)

	@classmethod
	async def _post(cls, endpoint:str, data:dict) -> dict:
		async with aiohttp.ClientSession() as sess:
			async with sess.post(endpoint, headers=cls.HEADERS, json=data) as res:
				data = await res.json(content_type=None)
				if res.status >= 400:
					raise AuthException(endpoint, data)
				return data

	@classmethod
	async def _get(cls, endpoint:str, data:dict) -> dict:
		async with aiohttp.ClientSession() as sess:
			async with sess.get(endpoint, headers=cls.HEADERS, params=data) as res:
				data = await res.json(content_type=None)
				if res.status >= 400:
					raise AuthException(endpoint, data)
				return data
