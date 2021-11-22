import sys
import json
import logging

from .mc.proto.play.clientbound import PacketChat
from .mc.token import Token
from .dispatcher import ConnectionState
from .client import MinecraftClient
from .server import MinecraftServer
from .util.helpers import parse_chat

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)

	if sys.argv[1] == "--server":
		host = sys.argv[2] if len(sys.argv) > 2 else "localhost"
		port = sys.argv[3] if len(sys.argv) > 3 else 25565

		serv = MinecraftServer(host, port)

		serv.run() # will block and start asyncio event loop
	else:
		username = sys.argv[1]
		pwd = sys.argv[2]
		server = sys.argv[3]
		color = not (len(sys.argv) > 4 and sys.argv[4] == "--no-color" )

		if ":" in server:
			_host, _port = server.split(":")
			host = _host.strip()
			port = int(_port)
		else:
			host = server.strip()
			port = 25565

		client = MinecraftClient(host, port, username=username, password=pwd)

		@client.on_packet(PacketChat, ConnectionState.PLAY)
		async def print_chat(packet: PacketChat):
			msg = parse_chat(packet.message, ansi_color=color)
			print(f"[{packet.position}] {msg}")

		client.run() # will block and start asyncio event loop

	logging.info("Terminated")

