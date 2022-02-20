"""
A super simple MinecraftClient exmaple.
Will connect to a server and print chat messages.
Requires an authorization code to login
"""
import sys

from aiocraft.client import MinecraftClient
from aiocraft.mc.proto import PacketChat
from aiocraft.util.helpers import parse_chat

server = sys.argv[1]
login_code = sys.argv[2] # Check authenticator.py example

app = MinecraftClient(server, login_code=login_code)

@app.on_packet(PacketChat)
async def on_chat(packet: PacketChat):
	print(parse_chat(packet.message, ansi_color=True))

app.run()

