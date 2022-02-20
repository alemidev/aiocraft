"""Microsoft made everyhing worse and now logging in is such a hassle..."""
import asyncio
from aiocraft.mc.auth import MicrosoftAuthenticator

print("To login into your Microsoft account, aiocraft needs to request an authentication code from Microsoft via OAuth.")
print("You will need to register an Azure application (or get access to an existing one).")
print("Please visit https://portal.azure.com/, select 'Azure Active Directory', then 'App registrations' and register a new application.")
print("You will need to register a redirect_uri, put anything there (even https://localhost)")
print()

client_id     = input("your Azure app client_id     > ")
client_secret = input("your Azure app client_secret > ")
redirect_uri  = input("your Azure app redirect_uri  > ") or "https://localhost"

auth = MicrosoftAuthenticator(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

print("Please visit")
print('\t' + auth.url())
print("Login into your microsoft account and authorize your application.")
print("Once you have logged in, you will be redirected to a (possibly blank) page.")
print("Check the page url for 'code=...'. Copy that code: it will allow to login into your MS account.")
print()
print("If you just wanted the login code, press enter to exit.")
print("If you instead want a Minecraft JWT token, to login into a server, paste your login code and press enter.")
code = input(" > ")
if code:
	asyncio.run(auth.login(code=code))
	print(f"\tJWT token    : {auth.accessToken}")
	print(f"\tGame Profile : {repr(auth.selectedProfile)}")
