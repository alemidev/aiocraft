import io
import json
from asyncio import Event
from typing import Tuple, Dict, Any

from .types import Type, VarInt

class Packet:
	__slots__ = 'definition', '_processed', '_proto', '_state'

	id : int
	definition : Tuple[Tuple[str, Type]]
	_processed : Event
	_proto : int
	_state : int

	_ids : Dict[int, int] # definitions are compiled at install time
	_definitions : Dict[int, Tuple[Tuple[str, Type]]] # definitions are compiled at install time

	def __init__(self, proto:int, **kwargs):
		self._proto = proto
		self._processed = Event()
		self.definition = self._definitions[proto]
		self.id = self._ids[proto]
		for name, t in self.definition:
			setattr(self, name, t.pytype(kwargs[name]) if name in kwargs else None)

	@property
	def processed(self) -> Event:
		"""Returns an event which will be set only after the packet has been processed (either sent or raised exc)"""
		return self._processed

	@classmethod
	def deserialize(cls, proto:int, buffer:io.BytesIO):
		pkt = cls(proto)
		for k, t in cls._definitions[proto]:
			setattr(pkt, k, t.read(buffer, ctx=pkt))
		return pkt
		# return cls(proto, **{ name : t.read(buffer) for (name, t) in cls._definitions[proto] })

	def serialize(self) -> io.BytesIO:
		buf = io.BytesIO()
		VarInt.write(self.id, buf)
		for name, t in self.definition:
			if getattr(self, name, None) is not None: # minecraft proto has no null type: this is an optional field left unset
				t.write(getattr(self, name), buf, ctx=self)
		buf.seek(0)
		return buf

	def __eq__(self, other) -> bool:
		if not isinstance(other, self.__class__):
			return False
		if self._proto != other._proto:
			return False
		for name, t in self.definition:
			if getattr(self, name) != getattr(other, name):
				return False
		return True


	def __str__(self) -> str:
		obj : Dict[str, Any] = {} # could be done with dict comp but the _ key gets put last :(
		obj["_"] = self.__class__.__name__
		obj["_proto"] = self._proto
		obj["_state"] = self._state
		for key, t in self.definition:
			obj[key] = getattr(self, key, None)
		return json.dumps(obj, indent=2, default=str)

	def __repr__(self) -> str:
		trunc = lambda x : x if len(x) < 100 else "[blob]"
		attrs = (f"{key}={trunc(repr(getattr(self, key, None)))}" for (key, t) in self.definition)
		return f"{self.__class__.__name__}({self._proto}, {', '.join(attrs)})"


