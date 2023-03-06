"""Minecraft identity utilities."""
import json
import uuid

from dataclasses import dataclass
from typing import Optional, Dict, Any


from .interface import AuthInterface, AuthException
from ..definitions import GameProfile

@dataclass
class MojangAuthenticator(AuthInterface):
	#selectedProfile : GameProfile
	#accessToken : str
	#session_server_override : str
	username : str
	password : Optional[str]
	clientToken : str
	auth_server_override : str

	AGENT_NAME = "Minecraft"
	AGENT_VERSION = 1
	AUTH_SERVER = "https://authserver.mojang.com"
	CONTENT_TYPE = "application/json"
	HEADERS = {"content-type": CONTENT_TYPE}

	def __init__(
		self, username:str="",
		password:Optional[str]=None,
		session_server_override:Optional[str]=None,
		auth_server_override:Optional[str]=None,
	):
		self.username = username
		self.password = password
		self.accessToken = ""
		self.clientToken = ""
		self.selectedProfile = GameProfile("", username)
		self.session_server_override = session_server_override
		self.auth_server_override = auth_server_override

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

	@property
	def auth_server(self) -> str:
		return self.auth_server_override or self.AUTH_SERVER

	@property
	def code(self) -> str:
		if self.username and self.password:
			return self.username
		return ""

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

		res = await self._post(self.auth_server + "/authenticate", json=payload)

		self.accessToken=res["accessToken"]
		self.clientToken=res["clientToken"]
		self.selectedProfile=GameProfile(**res["selectedProfile"])

		return self

	async def sign_out(self, username:str, password:str) -> dict:
		return await self._post(
			self.auth_server + "/signout",
			headers=self.HEADERS,
			json={
				"username": username,
				"password": password
			}
		)

	async def refresh(self, requestUser:bool = False) -> AuthInterface:
		if not self.accessToken or not self.clientToken:
			raise AuthException("/refresh", 0, {"message":"No access token or client token"}, {})
		res = await self._post(
			self.auth_server + "/refresh",
			headers=self.HEADERS,
			json={
				"accessToken": self.accessToken,
				"clientToken": self.clientToken
			}
		)

		self.accessToken = res["accessToken"]
		self.clientToken = res["clientToken"]
		self.selectedProfile = GameProfile(**res["selectedProfile"])

		if "user" in res and res["user"]:
			self.username = res["user"]["username"]

		return self

	async def validate(self, clientToken:bool = True) -> AuthInterface:
		if not self.accessToken:
			raise AuthException("/validate", 0, {"message":"No access token"}, {})
		payload = { "accessToken": self.accessToken }
		if clientToken:
			payload["clientToken"] = self.clientToken
		await self._post(
			self.auth_server + "/validate",
			headers=self.HEADERS,
			json=payload,
		)
		return self

	async def invalidate(self) -> AuthInterface:
		await self._post(
			self.auth_server + "/invalidate",
			headers=self.HEADERS,
			json= {
				"accessToken": self.accessToken,
				"clientToken": self.clientToken
			}
		)
		return self
