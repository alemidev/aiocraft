import struct
import asyncio

from typing import Any

class Type(object):
	_pytype : type
	_fmt : str

	@classmethod
	def serialize(cls, data:Any) -> bytes:
		return struct.pack(cls._fmt, data)

	@classmethod
	def deserialize(cls, data:bytes) -> Any:
		return struct.unpack(cls._fmt, data)[0]

class Boolean(Type):
	_pytype : type = bool
	_fmt : str = ">?"

class Byte(Type):
	_pytype : type = int
	_fmt : str = ">b"

class UnsignedByte(Type):
	_pytype : type = int
	_fmt : str = ">B"

class Short(Type):
	_pytype : type = int
	_fmt : str = ">h"

class UnsignedShort(Type):
	_pytype : type = int
	_fmt : str = ">H"

class Int(Type):
	_pytype : type = int
	_fmt : str = ">i"

class UnsignedInt(Type):
	_pytype : type = int
	_fmt : str = ">I"

class Long(Type):
	_pytype : type = int
	_fmt : str = ">q"

class UnsignedLong(Type):
	_pytype : type = int
	_fmt : str = ">Q"

class Float(Type):
	_pytype : type = float
	_fmt : str = ">f"

class Double(Type):
	_pytype : type = float
	_fmt : str = ">d"

class VarInt(Type):
	_pytype : type = int
	_maxBytes = 5

	@classmethod
	async def read(cls, stream: asyncio.StreamReader) -> int:
		"""Utility method to read a VarInt off the socket, because len comes as a VarInt..."""
		buf = 0
		off = 0
		while True:
			byte = await stream.read(1)
			buf |= (byte & 0b01111111) >> (7*off)
			if not byte & 0b10000000:
				break
			off += 1
		return buf

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
	_pytype : type = int
	_maxBytes = 10

class String(Type):
	_pytype : type = str

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
	_pytype : type = str
	pass

class Identifier(String):
	_pytype : type = str
	pass

class EntityMetadata(Type):
	_pytype : type = bytes
	# TODO
	pass

class EntityMetadataItem(Type):
	_pytype : type = bytes
	# TODO
	pass

class Slot(Type):
	_pytype : type = bytes
	# TODO
	pass

class NBTTag(Type):
	_pytype : type = bytes
	# TODO
	pass

class Position(Type):
	_pytype : type = bytes
	# TODO
	pass

class Angle(Type):
	_pytype : type = bytes
	# TODO
	pass

class UUID(Type):
	_pytype : type = bytes
	# TODO
	pass
