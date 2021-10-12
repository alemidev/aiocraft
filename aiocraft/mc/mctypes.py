import io
import struct
import asyncio

from typing import Any

class Type(object):
	_pytype : type
	_size : int
	_fmt : str

	# These methods will work only for fixed size data, if _size and _fmt are defined.
	#  For anything variabile in size, define custom read() and write() classmethods

	@classmethod
	def write(cls, data:Any, buffer:io.BytesIO):
		buffer.write(struct.pack(cls._fmt, data))

	@classmethod
	def read(cls, buffer:io.BytesIO) -> Any:
		return struct.unpack(cls._fmt, buffer.read(cls._size))[0]

class Boolean(Type):
	_pytype : type = bool
	_size : int = 1
	_fmt : str = ">?"

class Byte(Type):
	_pytype : type = int
	_size : int = 1
	_fmt : str = ">b"

class UnsignedByte(Type):
	_pytype : type = int
	_size : int = 1
	_fmt : str = ">B"

class Short(Type):
	_pytype : type = int
	_size : int = 2
	_fmt : str = ">h"

class UnsignedShort(Type):
	_pytype : type = int
	_size : int = 2
	_fmt : str = ">H"

class Int(Type):
	_pytype : type = int
	_size : int = 4
	_fmt : str = ">i"

class UnsignedInt(Type):
	_pytype : type = int
	_size : int = 4
	_fmt : str = ">I"

class Long(Type):
	_pytype : type = int
	_size : int = 8
	_fmt : str = ">q"

class UnsignedLong(Type):
	_pytype : type = int
	_size : int = 8
	_fmt : str = ">Q"

class Float(Type):
	_pytype : type = float
	_size : int = 4
	_fmt : str = ">f"

class Double(Type):
	_pytype : type = float
	_size : int = 8
	_fmt : str = ">d"

class VarInt(Type):
	_pytype : type = int
	_size = 5

	# @classmethod
	# async def read(cls, stream: asyncio.StreamReader) -> int:
	# 	"""Utility method to read a VarInt off the socket, because len comes as a VarInt..."""
	# 	buf = 0
	# 	off = 0
	# 	while True:
	# 		byte = await stream.read(1)
	# 		buf |= (byte & 0b01111111) >> (7*off)
	# 		if not byte & 0b10000000:
	# 			break
	# 		off += 1
	# 	return buf

	@classmethod
	def write(cls, data:int, buffer:io.BytesIO):
		count = 0
		while True:
			buf = data >> (7*count)
			val = (buf & 0b01111111)
			if (buf & 0b0000000) != 0:
				val |= 0b1000000
			buffer.write(val.to_bytes(1, 'little'))
			count += 1
			if count >= cls._size:
				break
			if (buf & 0b0000000) == 0:
				break

	@classmethod
	def read(cls, buffer:io.BytesIO) -> int:
		numRead = 0
		result = 0
		while True:
			buf = int.from_bytes(buffer.read(1), 'little')
			result |= (buf & 0b01111111) << (7 * numRead)
			numRead +=1
			if numRead > cls._size:
				raise ValueError("VarInt is too big")
			if buf & 0b10000000 == 0:
				break
		return result

	@classmethod
	def serialize(cls, data:int) -> bytes:
		buf = io.BytesIO()
		cls.write(data, buf)
		buf.seek(0)
		return buf.read()

class VarLong(VarInt):
	_pytype : type = int
	_size = 10

class String(Type):
	_pytype : type = str

	@classmethod
	def write(cls, data:str, buffer:io.BytesIO):
		encoded = data.encode('utf-8')
		VarInt.write(len(encoded), buffer)
		buffer.write(struct.pack(f">{len(encoded)}s", encoded))

	@classmethod
	def read(cls, buffer:io.BytesIO) -> str:
		length = VarInt.read(buffer)
		return struct.unpack(f">{length}s", buffer.read(length))[0]

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

class TrailingByteArray(Type):
	_pytype : type = bytes

	@classmethod
	def write(cls, data:bytes, buffer:io.BytesIO):
		buffer.write(data)

	@classmethod
	def read(cls, buffer:io.BytesIO) -> bytes:
		return buffer.read()
