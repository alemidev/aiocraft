from math import sqrt
from enum import Enum
from dataclasses import dataclass
from typing import Tuple

@dataclass # TODO use the one from types
class BlockPos:
	x : float
	y : float
	z : float

	@classmethod
	def from_tuple(cls, t:Tuple[float, float, float]):
		return cls(x=float(t[0]), y=float(t[1]), z=float(t[2]))

	def to_tuple(self, cast=float) -> Tuple[float, float, float]:
		return (cast(self.x), cast(self.y), cast(self.z))

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
