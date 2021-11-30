from math import sqrt
from enum import Enum
from dataclasses import dataclass

@dataclass # TODO use the one from types
class BlockPos:
	x : float
	y : float
	z : float

	def distance(self, p:'BlockPos'):
		return sqrt(
			( self.x - p.x ) ** 2 +
			( self.y - p.y ) ** 2 +
			( self.z - p.z ) ** 2
		)

class Dimension(Enum):
	NETHER = -1
	OVERWORLD = 0
	END = 1

class Difficulty(Enum):
	PEACEFUL = 0
	EASY = 1
	NORMAL = 2
	HARD = 3

class Gamemode(Enum):
	SURVIVAL = 0
	CREATIVE = 1
	ADVENTURE = 2
	SPECTATOR = 3

class ConnectionState(Enum):
	NONE = -1
	HANDSHAKING = 0
	STATUS = 1
	LOGIN = 2
	PLAY = 3
