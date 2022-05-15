"""aiocraft is an asyncio-driven headless minecraft client"""
# from .client import Client
from .mc import * # TODO move mc out of mc

from .client import MinecraftClient
from .server import MinecraftServer
from .mc.auth import MicrosoftAuthenticator, MojangAuthenticator

from .aiocraft import * # This is needed for PyO3 functions! No clue why or how...

__author__ = "alemidev"
__credits__ = "Thanks to pyCraft, really inspired this"
