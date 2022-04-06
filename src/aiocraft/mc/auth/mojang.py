"""Minecraft identity utilities."""
import json
import uuid
import logging

from dataclasses import dataclass
from typing import Optional

import aiohttp

from .interface import AuthInterface
from ..definitions import GameProfile

@dataclass
class MojangAuthenticator(AuthInterface):
	username : str
	accessToken : str
	clientToken : str
	selectedProfile : GameProfile

	AGENT_NAME = "Minecraft"
	AGENT_VERSION = 1
	AUTH_SERVER = "https://authserver.mojang.com"
	CONTENT_TYPE = "application/json"
	HEADERS = {"content-type": CONTENT_TYPE}

	def __init__(self):
		pass

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

	def serialize(self):
		return {
			"username":self.username,
			"accessToken":self.accessToken,
			"clientToken":self.clientToken,
			"selectedProfile": self.selectedProfile.as_dict(),
		}

	def deserialize(self, data:dict):
		self.username=data["username"] if "username" in data else data["selectedProfile"]["name"],
		self.accessToken=data["accessToken"],
		self.clientToken=data["clientToken"],
		self.selectedProfile=GameProfile(**data["selectedProfile"])

	async def login(self, username:str, password:str, invalidate=False) -> AuthInterface:
		payload = {
			"agent": {
				"name": self.AGENT_NAME,
				"version": self.AGENT_VERSION
			},
			"username": username,
			"password": password
		}

		if not invalidate:
			payload["clientToken"] = uuid.uuid4().hex

		res = await self._post(self.AUTH_SERVER + "/authenticate", payload)

		self.username=username,
		self.accessToken=res["accessToken"],
		self.clientToken=res["clientToken"],
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

	async def refresh(self, requestUser:bool = False) -> dict:
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

	async def validate(self, clientToken:bool = True) -> dict:
		payload = { "accessToken": self.accessToken }
		if clientToken:
			payload["clientToken"] = self.clientToken
		return await self._post(
			self.AUTH_SERVER + "/validate",
			headers=self.HEADERS,
			json=payload,
		)

	async def invalidate(self) -> dict:
		return await self._post(
			self.AUTH_SERVER + "/invalidate",
			headers=self.HEADERS,
			json= {
				"accessToken": self.accessToken,
				"clientToken": self.clientToken
			}
		)
