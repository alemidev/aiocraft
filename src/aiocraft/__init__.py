"""aiocraft is an asyncio-driven headless minecraft client"""
from .client import AbstractMinecraftClient
from .server import AbstractMinecraftServer

from .types import *
from .auth import MicrosoftAuthenticator, MojangAuthenticator

from .aiocraft import * # TODO why does PyO3 use the Cargo package name as top level name too??

__author__ = "alemidev"
__credits__ = "Thanks to pyCraft, really inspired this"
