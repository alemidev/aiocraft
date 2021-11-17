import sys
import json
import asyncio
import logging

from .mc.proto.play.clientbound import PacketChat
from .mc.token import Token
from .dispatcher import ConnectionState
from .client import Client
from .util.helpers import parse_chat

async def idle():
	while True:
		await asyncio.sleep(1)

if __name__ == "__main__":
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

	logging.basicConfig(level=logging.INFO)

	# TODO rework how this is started! Maybe implement client context manager?
	loop = asyncio.get_event_loop()

	client = Client(host, port, username=username, password=pwd)

	@client.on_packet(PacketChat, ConnectionState.PLAY)
	async def print_chat(packet: PacketChat):
		msg = parse_chat(json.loads(packet.message), color=color)
		print(f"[{packet.position}] {msg}")

	loop.run_until_complete(client.start())

	try:
		loop.run_until_complete(idle())
	except KeyboardInterrupt:
		logging.info("Received SIGINT, stopping...")
		loop.run_until_complete(client.stop())

	logging.info("Terminated")

