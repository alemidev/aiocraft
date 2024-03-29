import logging

from urllib.parse import urlencode
from typing import Any

from ..types import GameProfile
from .interface import AuthInterface, AuthException

class InvalidStateError(Exception):
	pass

class MicrosoftAuthenticator(AuthInterface):
	client_id : str
	client_secret : str
	redirect_uri : str
	code : str | None

	accessToken : str
	selectedProfile : GameProfile
	refreshToken : str | None

	MINECRAFT_CLIENT_ID = "00000000402b5328"
	OAUTH_LOGIN = "https://login.live.com/oauth20"
	XBL_LOGIN = "https://user.auth.xboxlive.com/user/authenticate"
	XSTS_LOGIN = "https://xsts.auth.xboxlive.com/xsts/authorize"
	MINECRAFT_API = "https://api.minecraftservices.com"

	def __init__(self,
		client_id:str,
		client_secret:str,
		redirect_uri:str="http://localhost",
		code:str|None = None
	):
		self.client_id = client_id
		self.client_secret = client_secret
		self.redirect_uri = redirect_uri
		self.code = code
		self.refreshToken = None
		self.accessToken = ''
		self.selectedProfile = GameProfile(id='', name='')

	def serialize(self) -> dict[str, Any]:
		return {
			'accessToken': self.accessToken,
			'refreshToken': self.refreshToken,
			'selectedProfile': self.selectedProfile.serialize(),
		}

	def deserialize(self, data:dict[str, Any]):
		self.accessToken = data['accessToken']
		self.refreshToken = data['refreshToken']
		self.selectedProfile = GameProfile(**data['selectedProfile'])

	@property
	def refreshable(self) -> bool:
		return self.refreshToken is not None

	def url(self, state:str=""):
		"""Builds MS OAuth url for the user to login"""
		return (
			self.OAUTH_LOGIN + "_authorize.srf" +
			f"?client_id={self.client_id}" +
			 "&response_type=code" +
			f"&redirect_uri={self.redirect_uri}" +
			 "&scope=XboxLive.signin%20offline_access" +
			f"&state={state}"
		)

	async def login(self): # TODO nicer way to get code?
		if not self.code:
			raise AuthException("/login", 0, {"error": "Missing login code"}, {})
		self.accessToken = await self.authenticate(self.code)
		self.code = None  # this is only valid once
		prof = await self.fetch_profile()
		self.selectedProfile = GameProfile(id=prof['id'], name=prof['name'])
		logging.info("Successfully logged into Microsoft account")

	async def refresh(self):
		if not self.refreshToken:
			raise AuthException("/refresh", 0, {"error": "Missing refresh token"}, {})
		self.accessToken = await self.authenticate()
		prof = await self.fetch_profile()
		self.selectedProfile = GameProfile(id=prof['id'], name=prof['name'])
		logging.info("Successfully refreshed Microsoft token")

	async def validate(self):
		if not self.accessToken:
			raise AuthException("/validate", 0, {"error": "No access token"}, {})
		prof = await self.fetch_profile()
		self.selectedProfile = GameProfile(id=prof['id'], name=prof['name'])
		logging.info("Session validated : %s", repr(self.selectedProfile))

	async def authenticate(self, code:str="") -> str:
		"""Authorize Microsoft account"""
		logging.debug("Authenticating Microsoft account")
		payload = {
			"client_id": self.client_id,
			"client_secret": self.client_secret,
			"redirect_uri": self.redirect_uri,
		}
		if code:
			payload['code'] = code
			payload['grant_type'] = 'authorization_code'
		elif self.refreshToken:
			payload['refresh_token'] = self.refreshToken
			payload['grant_type'] = 'refresh_token'
		else:
			raise InvalidStateError("Missing auth code and refresh token")
		auth_response = await self._post(
			self.OAUTH_LOGIN + "_token.srf", 
			headers={ "Content-Type": "application/x-www-form-urlencoded" },
			data=urlencode(payload)
		)
		self.refreshToken = auth_response['refresh_token']
		# maybe store expire_in and other stuff too? TODO

		ms_token = auth_response['access_token']
		return await self._xbl_auth(ms_token)

	async def _xbl_auth(self, ms_token:str) -> str:
		"""Authorize with XBox Live"""
		logging.debug("Authenticating against XBox Live")
		auth_response = await self._post(
			self.XBL_LOGIN,
			headers={
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			json={
				"Properties": {
					"AuthMethod": "RPS",
					"SiteName": "user.auth.xboxlive.com",
					"RpsTicket": f"d={ms_token}"
				},
				"RelyingParty": "http://auth.xboxlive.com",
				"TokenType": "JWT"
			}
		)
		xbl_token = auth_response["Token"]
		return await self._xsts_auth(xbl_token)

	async def _xsts_auth(self, xbl_token:str) -> str:
		"""Authenticate with XBox Security Tokens"""
		logging.debug("Authenticating against XSTS")
		auth_response = await self._post(
			self.XSTS_LOGIN,
			headers={
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			json={
				"Properties": {
					"SandboxId": "RETAIL",
					"UserTokens": [ xbl_token ]
				},
				"RelyingParty": "rp://api.minecraftservices.com/",
				"TokenType": "JWT"
			}
		)
		xsts_token = auth_response["Token"]
		userhash = auth_response["DisplayClaims"]["xui"][0]["uhs"]
		return await self._mc_auth(userhash, xsts_token)

	async def _mc_auth(self, userhash:str, xsts_token:str) -> str:
		"""Authenticate with Minecraft"""
		logging.debug("Authenticating against Minecraft")
		auth_response = await self._post(
			self.MINECRAFT_API + "/authentication/login_with_xbox",
			headers={
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			json={
				"identityToken": f"XBL3.0 x={userhash};{xsts_token}"
			},
		)
		return auth_response['access_token']

	async def fetch_mcstore(self) -> dict[str, Any]:
		"""Get the store information"""
		logging.debug("Fetching MC Store")
		return await self._get(
			self.MINECRAFT_API + "/entitlements/mcstore",
			headers={ "Authorization": f"Bearer {self.accessToken}" },
		)

	async def fetch_profile(self) -> dict[str, Any]:
		"""Get player profile"""
		logging.debug("Fetching profile")
		return await self._get(
			self.MINECRAFT_API + "/minecraft/profile",
			headers={ "Authorization": f"Bearer {self.accessToken}" },
		)
