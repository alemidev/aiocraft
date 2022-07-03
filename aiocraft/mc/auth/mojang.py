"""Minecraft identity utilities."""
import json
import uuid
import logging

from dataclasses import dataclass
from typing import Optional, Dict, Any

import aiohttp

from .interface import AuthInterface, AuthException
from ..definitions import GameProfile

@dataclass
class MojangAuthenticator(AuthInterface):
	username : str
	password : Optional[str]
	accessToken : str
	clientToken : str
	selectedProfile : GameProfile

	AGENT_NAME = "Minecraft"
	AGENT_VERSION = 1
	AUTH_SERVER = "https://authserver.mojang.com"
	CONTENT_TYPE = "application/json"
	HEADERS = {"content-type": CONTENT_TYPE}

	def __init__(self, username:str="", password:Optional[str]=None):
		self.username = username
		self.password = password
		self.accessToken = ""
		self.clientToken = ""
		self.selectedProfile = GameProfile("", username)

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
		return json.dumps(self.serialize())

	def __str__(self) -> str:
		return repr(self)

	def serialize(self) -> Dict[str, Any]:
		return {
			"username":self.username,
			"accessToken":self.accessToken,
			"clientToken":self.clientToken,
			"selectedProfile": self.selectedProfile.serialize(),
		}

	def deserialize(self, data:Dict[str, Any]) -> AuthInterface:
		self.username = data["username"] if "username" in data else data["selectedProfile"]["name"]
		self.accessToken = data["accessToken"]
		self.clientToken = data["clientToken"]
		self.selectedProfile = GameProfile(**data["selectedProfile"])
		return self

	async def login(self) -> AuthInterface:
		payload = {
			"agent": {
				"name": self.AGENT_NAME,
				"version": self.AGENT_VERSION
			},
			"username": self.username,
			"password": self.password
		}

		payload["clientToken"] = uuid.uuid4().hex # don't include this to invalidate all other sessions

		res = await self._post(self.AUTH_SERVER + "/authenticate", json=payload)

		self.accessToken=res["accessToken"]
		self.clientToken=res["clientToken"]
		self.selectedProfile=GameProfile(**res["selectedProfile"])

		return self

	@classmethod
	async def sign_out(cls, username:str, password:str) -> dict:
		return await cls._post(
			cls.AUTH_SERVER + "/signout",
			headers=cls.HEADERS,
			json={
				"username": username,
				"password": password
			}
		)

	async def refresh(self, requestUser:bool = False) -> AuthInterface:
		if not self.accessToken or not self.clientToken:
			raise AuthException("/refresh", 0, {"message":"No access token or client token"}, {})
		res = await self._post(
			self.AUTH_SERVER + "/refresh",
			headers=self.HEADERS,
			json={
				"accessToken": self.accessToken,
				"clientToken": self.clientToken
			}
		)

		self.accessToken = res["accessToken"]
		self.clientToken = res["clientToken"]
		self.selectedProfile = GameProfile(**res["selectedProfile"])

		if "user" in res:
			self.username = res["user"]["username"]

		return self

	async def validate(self, clientToken:bool = True) -> AuthInterface:
		if not self.accessToken:
			raise AuthException("/validate", 0, {"message":"No access token"}, {})
		payload = { "accessToken": self.accessToken }
		if clientToken:
			payload["clientToken"] = self.clientToken
		await self._post(
			self.AUTH_SERVER + "/validate",
			headers=self.HEADERS,
			json=payload,
		)
		return self

	async def invalidate(self) -> AuthInterface:
		await self._post(
			self.AUTH_SERVER + "/invalidate",
			headers=self.HEADERS,
			json= {
				"accessToken": self.accessToken,
				"clientToken": self.clientToken
			}
		)
		return self
