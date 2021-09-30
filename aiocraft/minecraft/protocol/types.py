import struct

from typing import Any

class Type(object):
	_fmt : str

	@classmethod
	def serialize(cls, data:Any) -> bytes:
		return struct.pack(cls._fmt, data)

	@classmethod
	def unserialize(cls, data:bytes) -> Any:
		return struct.unpack(cls._fmt, data)[0]

class Boolean(Type):
	_fmt : str = ">?"

class Byte(Type):
	_fmt : str = ">b"

class UnsignedByte(Type):
	_fmt : str = ">B"

class Short(Type):
	_fmt : str = ">h"

class UnsignedShort(Type):
	_fmt : str = ">H"

class Int(Type):
	_fmt : str = ">i"

class Long(Type):
	_fmt : str = ">q"

class Float(Type):
	_fmt : str = ">f"

class Double(Type):
	_fmt : str = ">d"

class VarInt(Type):
	_maxBytes = 5
	@classmethod
	def serialize(cls, data:int) -> bytes:
		res : bytearray = bytearray()
		count = 0
		while True:
			if count >= cls._maxBytes:
				break
			buf = data >> (7*count)
			val = (buf & 0b01111111)
			if (buf & 0b0000000) != 0:
				val |= 0b1000000
			res.extend(val.to_bytes(1, 'little'))
			if (buf & 0b0000000) == 0:
				break
			count += 1
		return res

	@classmethod
	def unserialize(cls, data:bytes) -> int:
		numRead = 0
		result = 0
		pos = 0
		while True:
			buf = data[0]
			value = buf & 0b01111111
			result |= value << (7 * numRead)
			numRead +=1
			if numRead > cls._maxBytes:
				raise ValueError("VarInt is too big")
			if buf & 0b10000000 == 0:
				break
		return result

class VarLong(VarInt):
	_maxBytes = 10

class String(Type):
	@classmethod
	def serialize(cls, data:str) -> bytes:
		encoded = data.encode('utf-8')
		return VarInt.serialize(len(encoded)) + struct.pack(f">{len(encoded)}s", encoded)

	@classmethod
	def unserialize(cls, data:bytes) -> str:
		length = VarInt.unserialize(data)
		start_index = len(data) - length
		return struct.unpack(f">{length}s", data[start_index:])[0]

class Chat(String):
	pass

class Identifier(String):
	pass

class EntityMetadata(Type):
	# TODO
	pass

class Slot(Type):
	# TODO
	pass
			if buf & 0b10000000 == 0:
				break

class NBTTag(Type):
	# TODO
	pass

class Position(Type):
	# TODO
	pass

class Angle(Type):
	# TODO
	pass

class UUID(Type):
	# TODO
	pass
