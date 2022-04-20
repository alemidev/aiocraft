#!/usr/bin/env python
if __name__ == "__main__":
	import json
	import asyncio
	
	from getpass import getpass
	
	from aiocraft.mc.auth.mojang import MojangAuthenticator

	username = input("username > ")
	password = getpass("password > ")

	async def main(usr, pwd):
		tok = MojangAuthenticator(username=usr, password=pwd)
		await tok.login()
		return tok

	t = asyncio.run(main(username, password))

	print(json.dumps(t.serialize()))
