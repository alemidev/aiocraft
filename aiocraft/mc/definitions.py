from math import sqrt
from enum import Enum
from dataclasses import dataclass
from typing import Tuple

@dataclass # TODO use the one from types
class BlockPos:
	x : float
	y : float
	z : float

	def __equals__(self, other) -> bool:
		if not isinstance(other, self.__class__):
			return False
		return self.x == other.x \
			and self.y == other.y \
			and self.z == other.z

	def __repr__(self) -> str:
		return f"{self.__class__.__name__}(x={self.x},y={self.y},z={self.z})"

	def __str__(self) -> str:
		return repr(self)

	def __hash__(self) -> int:
		return hash(self.to_tuple())

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

class Item:
	id : int
	count : int
	nbt : dict
	damage : int # This got removed past 1.12.2

	def __init__(self, item:Item = None):
		if item:
			self.id = item.id
			self.count = item.count
			self.nbt = item.nbt
			self.damage = item.damage

	def __getitem__(self, key:str): # backwards compatibility
		return getattr(self, key)

	@property
	def durability(self) -> int:
		# TODO make a map of durability for each item and subtract damage?
		return self.damage

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
