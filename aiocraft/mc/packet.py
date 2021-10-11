import json
from typing import Tuple, Dict

from .mctypes import Type, VarInt

class Packet:
	id : int
	slots : Tuple[Tuple[str, Type]]

	_ids : Dict[int, int] # definitions are compiled at install time
	_slots : Dict[int, Tuple[Tuple[str, Type]]] # definitions are compiled at install time

	def __init__(self, proto:int, **kwargs):
		self._protocol = proto
		self.slots = self._slots[proto]
		self.id = self._ids[proto]
		for name, t in self.slots:
			setattr(self, name, t._pytype(kwargs[name]) if name in kwargs else None)

	@classmethod
	def deserialize(cls, proto:int, data:bytes):
		return cls(proto, **{ name : t.deserialize(data) for (name, t) in cls._slots[proto] })

	def serialize(self) -> bytes:
		return VarInt.serialize(self.id) + b''.join(
			slot[1].serialize(getattr(self, slot[0], None))
			for slot in self.slots
		)

	def __str__(self) -> str:
		obj = {} # could be done with dict comp but the _ key gets put last :(
		obj["_"] = self.__class__.__name__
		obj["_proto"] = self._protocol
		for key, t in self.slots:
			obj[key] = getattr(self, key, None)
		return json.dumps(obj, indent=2, default=str)

	def __repr__(self) -> str:
		attrs = (f"{key}={repr(getattr(self, key, None))}" for (key, t) in self.slots)
		return f"{self.__class__.__name__}({self._protocol}, {', '.join(attrs)})"


