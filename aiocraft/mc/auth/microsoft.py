import re
import uuid
import logging

from urllib.parse import urlencode
from typing import Dict, Optional, Any

from yarl import URL
import aiohttp

from ..definitions import GameProfile
from .interface import AuthInterface

class InvalidStateError(Exception):
	pass

class MicrosoftAuthenticator(AuthInterface):
	client_id : str
	client_secret : str
	redirect_uri : str

	ms_token : Optional[str]
	ms_refresh_token : Optional[str]
	xbl_token : Optional[str]
	xsts_token : Optional[str]
	userhash : Optional[str]

	mcstore : dict
	accessToken : str
	selectedProfile : GameProfile

	MINECRAFT_CLIENT_ID = "00000000402b5328"
	OAUTH_LOGIN = "https://login.live.com/oauth20"
	XBL_LOGIN = "https://user.auth.xboxlive.com/user/authenticate"
	XSTS_LOGIN = "https://xsts.auth.xboxlive.com/xsts/authorize"
	MINECRAFT_API = "https://api.minecraftservices.com"

	def __init__(self,
		client_id:str,
		client_secret:str,
		redirect_uri:str="http://localhost"
	):
		self.client_id = client_id
		self.client_secret = client_secret
		self.redirect_uri = redirect_uri
		self.ms_token = None
		self.ms_refresh_token = None
		self.xbl_token = None
		self.xsts_token = None
		self.userhash = None
		self.mcstore = {}
		self.accessToken = ''
		self.selectedProfile = GameProfile(id='', name='')

	def url(self, state:str=""):
		"""Builds MS OAuth url for the user to login"""
		return (
			self.OAUTH_LOGIN + "_authorize.srf" +
			f"?client_id={self.client_id}" +
			f"&response_type=code" +
			f"&redirect_uri={self.redirect_uri}" +
			f"&scope=XboxLive.signin%20offline_access" +
			f"&state={state}"
		)

	async def login(self, code:str): # TODO nicer way to get code?
		await self._ms_auth(code)
		await self._xbl_auth()
		await self._xsts_auth()
		await self._mc_auth()
		await self.fetch_mcstore()
		await self.fetch_profile()
		logging.info("Successfully logged into Microsoft account")

	async def refresh(self):
		if not self.ms_refresh_token:
			raise InvalidStateError("Missing MS refresh token")
		await self._ms_auth()
		await self._xbl_auth()
		await self._xsts_auth()
		await self._mc_auth()
		logging.info("Successfully refreshed Microsoft token")

	async def _ms_auth(self, code:str=""):
		"""Authorize Microsoft account"""
		logging.debug("Authenticating Microsoft account")
		payload = {
			"client_id": self.client_id,
			"client_secret": self.client_secret,
			"redirect_uri": self.redirect_uri,
			"grant_type": "authorization_code",
		}
		if code:
			payload['code'] = code
		elif self.ms_refresh_token:
			payload['refresh_token'] = self.ms_refresh_token
		else:
			raise InvalidStateError("Missing auth code and refresh token")
		auth_response = await self._post(
			self.OAUTH_LOGIN + "_token.srf", 
			headers={ "Content-Type": "application/x-www-form-urlencoded" },
			data=urlencode(payload)
		)
		self.ms_token = auth_response['access_token']
		self.ms_refresh_token = auth_response['refresh_token']
		# maybe store expire_in and other stuff too? TODO

	async def _xbl_auth(self):
		"""Authorize with XBox Live"""
		if not self.ms_token:
			raise InvalidStateError("Missing MS access token")
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
					"RpsTicket": f"d={self.ms_token}"
				},
				"RelyingParty": "http://auth.xboxlive.com",
				"TokenType": "JWT"
			}
		)
		self.userhash = auth_response["DisplayClaims"]["xui"][0]["uhs"]
		self.xbl_token = auth_response["Token"]

	async def _xsts_auth(self):
		"""Authenticate with XBox Security Tokens"""
		if not self.xbl_token:
			raise InvalidStateError("Missing XBL Token")
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
					"UserTokens": [
						self.xbl_token
					]
				},
				"RelyingParty": "rp://api.minecraftservices.com/",
				"TokenType": "JWT"
			}
		)
		self.xsts_token = auth_response["Token"]
		if self.userhash != auth_response["DisplayClaims"]["xui"][0]["uhs"]:
			raise InvalidStateError("userhash differs from XBL and XSTS")

	async def _mc_auth(self):
		"""Authenticate with Minecraft"""
		if not self.userhash:
			raise InvalidStateError("Missing userhash")
		if not self.xsts_token:
			raise InvalidStateError("Missing XSTS Token")
		logging.debug("Authenticating against Minecraft")
		auth_response = await self._post(
			self.MINECRAFT_API + "/authentication/login_with_xbox",
			headers={
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			json={
				"identityToken": f"XBL3.0 x={self.userhash};{self.xsts_token}"
			},
		)
		self.access_token = auth_response['access_token']

	async def fetch_mcstore(self):
		"""Get the store information"""
		logging.debug("Fetching MC Store")
		self.mcstore = await self._get(
			self.MINECRAFT_API + "/entitlements/mcstore",
			headers={ "Authorization": f"Bearer {self.access_token}" },
		)

	async def fetch_profile(self):
		"""Get player profile"""
		logging.debug("Fetching profile")
		p = await self._get(
			self.MINECRAFT_API + "/minecraft/profile",
			headers={ "Authorization": f"Bearer {self.access_token}" },
		)
		self.profile = GameProfile(id=p['id'], name=p['name'])
