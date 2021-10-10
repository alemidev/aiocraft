from typing import Tuple

from .mctypes import Type

class Packet:
	id : int
	_slots : Tuple[Tuple[str, Type]]

	def serialize(self) -> bytes:
		return b''.join(
			slot[1].serialize(getattr(self, slot[0]))
			for slot in self._slots
		)

	@classmethod
	def deserialize(cls, data:bytes):
		pkt = cls()
		for slot in cls._slots:
			setattr(pkt, slot[0], slot[1].deserialize(data))
		return pkt

