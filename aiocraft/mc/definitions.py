from datetime import datetime
import uuid
import json
from math import sqrt
from enum import Enum
from dataclasses import dataclass
from typing import Tuple, Optional, List, Any, Dict

class ConnectionState(Enum):
	NONE = -1
	HANDSHAKING = 0
	STATUS = 1
	LOGIN = 2
	PLAY = 3

class Dimension(Enum):
	NETHER = -1
	OVERWORLD = 0
	END = 1
	UNKNOWN = 666

	@classmethod
	def from_str(cls, txt:str) -> 'Dimension':
		txt = txt.lower().replace('minecraft:', '')
		if txt == 'overworld':
			return Dimension.OVERWORLD
		if txt == 'the_nether':
			return Dimension.NETHER
		if txt == 'the_end':
			return Dimension.END
		return Dimension.UNKNOWN

class Difficulty(Enum):
	PEACEFUL = 0
	EASY = 1
	NORMAL = 2
	HARD = 3
	UNKNOWN = -1

class Gamemode(Enum):
	SURVIVAL = 0
	CREATIVE = 1
	ADVENTURE = 2
	SPECTATOR = 3
	UNKNOWN = -1

@dataclass
class GameProfile:
	id : str
	name : str

	def __str__(self):
		return json.dumps(self.serialize(), indent=2)

	def __repr__(self):
		return f"GameProfile(id='{self.id}', name='{self.name}')"

	def serialize(self):
		return {
			"id": self.id,
			"name": self.name
		}

class EnchantmentType(Enum):
	protection            = 0
	fire_protection       = 1
	feather_falling       = 2
	blast_protection      = 3
	projectile_protection = 4
	respiration           = 5
	aqua_affinity         = 6
	thorns                = 7
	depth_strider         = 8
	frost_walker          = 9
	binding_curse         = 10
	sharpness             = 16
	smite                 = 17
	bane_of_arthropods    = 18
	knockback             = 19
	fire_aspect           = 20
	looting               = 21
	sweeping              = 22
	efficiency            = 32
	silk_touch            = 33
	unbreaking            = 34
	fortune               = 35
	power                 = 48
	punch                 = 49
	flame                 = 50
	infinity              = 51
	luck_of_the_sea       = 61
	lure                  = 62
	mending               = 70
	vanishing_curse       = 71

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

	def close(self, other:'BlockPos', threshold:float = 0.1) -> bool:
		return (self.x - other.x) < threshold \
			and (self.y - other.y) < threshold \
			and (self.z - other.z) < threshold

	def clone(self) -> 'BlockPos':
		return BlockPos(self.x, self.y, self.z)

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
	nbt : dict # TODO
	damage : Optional[int] # This got removed past 1.12.2

	def __init__(self, item:'Item' = None, id:int=0, count:int=1, nbt:dict=None, damage:int=0):
		self.id = id
		self.count = count
		self.nbt = nbt or {}
		self.damage = damage
		if item:
			self.id = item.id
			self.count = item.count
			self.nbt = item.nbt
			self.damage = item.damage

	def serialize(self) -> dict:
		return {
			'id': self.id,
			'count': self.count,
			'nbt': self.nbt,
			'damage': self.damage,
		}

	@classmethod
	def deserialize(cls, data:dict) -> 'Item':
		return cls(
			id=data["id"],
			count=data["count"],
			nbt=data["nbt"],
			damage=data["damage"]
		)

	def __getitem__(self, key:str): # backwards compatibility
		return getattr(self, key)

	def __str__(self) -> str:
		return repr(self)

	def __repr__(self) -> str:
		return f"Item(id={self.id}, count={self.count}, damage={self.damage}, nbt={str(self.nbt)})"

	@property
	def durability(self) -> int:
		# TODO make a map of durability for each item and subtract damage?
		return self.damage or -1

class Enchantment:
	eid : int
	type : EnchantmentType
	level : int

	def __init__(self, type:EnchantmentType=None, id:int=None, lvl:int=1):
		if type is None and id is None:
			raise ValueError("No enchantment type or enchantment id provided")
		self.type = type or EnchantmentType(id)
		self.eid = self.type.value
		self.level = lvl

	def repr(self) -> str:
		return f"<Enchantment({str(self)})>"

	def __str__(self) -> str:
		return f"{self.type.name}" + (f" {self.level}" if self.level > 1 else "")

@dataclass
class Texture:
	name : str
	value : str
	signature : Optional[str]

	def __getitem__(self, name:str) -> Optional[Any]:
		return getattr(self, name, None)

	def serialize(self) -> Dict[str, Any]:
		return {
			"_": "Texture",
			"name": self.name,
			"value": self.value,
			"signature": self.signature
		}

	@classmethod
	def deserialize(cls, data:Dict[str, Any]) -> 'Texture':
		if "_" in data and data["_"] != cls.__name__:
			raise ValueError(f"Cannot deserialize {data['_']} as {cls.__name__}")
		return cls(
			name=data["name"],
			value=data["value"],
			signature=data["signature"] if "signature" in data else None,
		)

@dataclass
class Player:
	UUID : uuid.UUID
	name : str
	joinTime : datetime
	properties : Optional[List[Texture]] = None
	gamemode : Gamemode = Gamemode.SURVIVAL
	ping : int = -1
	displayName : Optional[str] = None

	def __getitem__(self, name:str) -> Optional[Any]:
		return getattr(self, name, None)

	def serialize(self) -> Dict[str, Any]:
		return {
			"_": "Player",
			"UUID": self.UUID,
			"name": self.name,
			"joinTime": self.joinTime,
			"properties": [ p.serialize() for p in self.properties ] \
				if self.properties is not None else None,
			"gamemode": self.gamemode,
			"ping": self.ping,
			"displayName": self.displayName
		}

	@classmethod
	def deserialize(cls, data:Dict[str, Any]) -> 'Player':
		if "_" in data and data["_"] != cls.__name__:
			raise ValueError(f"Cannot deserialize {data['_']} as {cls.__name__}")
		return cls(
			UUID=data["UUID"],
			name=data["name"],
			joinTime=data["joinTime"] if "joinTime" in data else datetime(2011, 11, 18, 0, 0, 0),
			properties=[ Texture.deserialize(t) for t in data["properties"] ] \
				if "properties" in data and data["properties"] else None,
			gamemode=data["gamemode"],
			ping=data["ping"],
			displayName=data["displayName"] if "displayName" in data else None,
		)

