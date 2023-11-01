import io
import json
from asyncio import Event
from typing import Tuple, List, Dict, Any

from .types import Type, VarInt, Context

MAX_FIELD_PRINT_SIZE = 255

class Packet:
	__slots__ = 'id', 'definition', '_processed', '_proto', '_state'

	id : int
	definition : List[Tuple[str, Type]]
	_processed : Event
	_proto : int
	_state : int

	_ids : Dict[int, int] # definitions are compiled at install time
	_definitions : Dict[int, List[Tuple[str, Type]]] # definitions are compiled at install time

	def __init__(self, proto:int, **kwargs):
		self._proto = proto
		self._processed = Event()
		while proto not in self._definitions:
			proto -= 1
		self.definition = self._definitions[proto]
		self.id = self._ids[proto]
		for name, t in self.definition:
			if name in kwargs and kwargs[name] is not None:
				setattr(self, name, kwargs[name])

	@property
	def processed(self) -> Event:
		"""Returns an event which will be set only after the packet has been processed (either sent or raised exc)"""
		return self._processed

	@classmethod
	def deserialize(cls, proto:int, buffer:io.BytesIO):
		ctx = Context(_proto=proto)
		fallback_proto = proto
		while fallback_proto not in cls._definitions:
			fallback_proto -= 1
		for k, t in cls._definitions[fallback_proto]:
			setattr(ctx, k, t.read(buffer, ctx=ctx))
		return cls(proto, **ctx.serialize())
		# return cls(proto, **{ name : t.read(buffer) for (name, t) in cls._definitions[proto] })

	def serialize(self) -> io.BytesIO:
		ctx = Context(_proto=self._proto)
		buf = io.BytesIO()
		VarInt.write(self.id, buf, ctx=ctx)
		for name, t in self.definition:
			if getattr(self, name, None) is not None: # minecraft proto has no null type: this is an optional field left unset
				setattr(ctx, name, getattr(self, name)) # TODO maybe  **vars(self)  in ctx constructor?
				t.write(getattr(self, name), buf, ctx=ctx)
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
		obj["_id"] = f"0x{self.id:02x}"
		for key, t in self.definition:
			obj[key] = getattr(self, key, None)
		return json.dumps(obj, indent=2, default=str)

	def __repr__(self) -> str:
		trunc = lambda x : x if len(x) < MAX_FIELD_PRINT_SIZE else "[blob]"
		attrs = (f"{key}={trunc(repr(getattr(self, key, None)))}" for (key, t) in self.definition)
		return f"{self.__class__.__name__}({self._proto}, {', '.join(attrs)})"


