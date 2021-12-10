import io
import struct
import asyncio
import uuid

from typing import List, Tuple, Dict, Any, Union, Optional, Type as Class

class Type(object):
	pytype : type

	def write(self, data:Any, buffer:io.BytesIO, ctx:object=None) -> None:
		"""Write data to a packet buffer"""
		raise NotImplementedError
	
	def read(self, buffer:io.BytesIO, ctx:object=None) -> Any:
		"""Read data off a packet buffer"""
		raise NotImplementedError

	def check(self, ctx:object) -> bool:
		"""Check if this type exists in this context"""
		return True

class UnimplementedDataType(Type):
	pytype : type = bytes

	def write(self, data:bytes, buffer:io.BytesIO, ctx:object=None):
		if data:
			buffer.write(data)

	def read(self, buffer:io.BytesIO, ctx:object=None) -> bytes:
		return buffer.read()

TrailingData = UnimplementedDataType()
EntityMetadata = UnimplementedDataType()
EntityMetadataItem = UnimplementedDataType()
NBTTag = UnimplementedDataType()
Slot = UnimplementedDataType()

class PrimitiveType(Type):
	size : int
	fmt : str

	def __init__(self, pytype:type, fmt:str, size:int):
		self.pytype = pytype
		self.fmt = fmt
		self.size = size

	def write(self, data:Any, buffer:io.BytesIO, ctx:object=None):
		buffer.write(struct.pack(self.fmt, data))

	def read(self, buffer:io.BytesIO, ctx:object=None) -> Any:
		return struct.unpack(self.fmt, buffer.read(self.size))[0]

Boolean = PrimitiveType(bool, ">?", 1)
Byte = PrimitiveType(int, ">b", 1)
UnsignedByte = PrimitiveType(int, ">B", 1)
Short = PrimitiveType(int, ">h", 2)
UnsignedShort = PrimitiveType(int, ">H", 2)
Int = PrimitiveType(int, ">i", 4)
UnsignedInt = PrimitiveType(int, ">I", 4)
Long = PrimitiveType(int, ">q", 8)
UnsignedLong = PrimitiveType(int, ">Q", 8)
Float = PrimitiveType(float, ">f", 4)
Double = PrimitiveType(float, ">d", 8)
Angle = PrimitiveType(int, ">b", 1)

class VarLenPrimitive(Type):
	pytype : type = int
	max_bytes : int

	def __init__(self, max_bytes:int):
		self.max_bytes = max_bytes

	def write(self, data:int, buffer:io.BytesIO, ctx:object=None):
		count = 0
		while count < self.max_bytes:
			byte = data & 0b01111111
			data >>= 7
			if data > 0:
				byte |= 0b10000000
			buffer.write(struct.pack("B", byte))
			count += 1
			if not data:
				break

	def read(self, buffer:io.BytesIO, ctx:object=None) -> int:
		numRead = 0
		result = 0
		while True:
			data = buffer.read(1)
			if len(data) < 1:
				raise ValueError("VarInt/VarLong is too short")
			buf = int.from_bytes(data, 'little')
			result |= (buf & 0b01111111) << (7 * numRead)
			numRead +=1
			if numRead > self.max_bytes:
				raise ValueError("VarInt/VarLong is too big")
			if buf & 0b10000000 == 0:
				break
		return result

	# utility methods since VarInt is super used

	def serialize(self, data:int) -> bytes:
		buf = io.BytesIO()
		self.write(data, buf)
		buf.seek(0)
		return buf.read()

	def deserialize(self, data:bytes) -> int:
		buf = io.BytesIO(data)
		return self.read(buf)

VarInt = VarLenPrimitive(5)
VarLong = VarLenPrimitive(10)

class StringType(Type):
	pytype : type = str

	def write(self, data:str, buffer:io.BytesIO, ctx:object=None):
		encoded = data.encode('utf-8')
		VarInt.write(len(encoded), buffer, ctx=ctx)
		buffer.write(encoded)

	def read(self, buffer:io.BytesIO, ctx:object=None) -> str:
		length = VarInt.read(buffer, ctx=ctx)
		return buffer.read(length).decode('utf-8')

String = StringType()
Chat = StringType()
Identifier = StringType()

class BufferType(Type):
	pytype : type = bytes
	count : Type

	def __init__(self, count:Type = VarInt):
		self.count = count

	def write(self, data:bytes, buffer:io.BytesIO, ctx:object=None):
		self.count.write(len(data), buffer, ctx=ctx)
		buffer.write(data)

	def read(self, buffer:io.BytesIO, ctx:object=None) -> bytes:
		length = self.count.read(buffer, ctx=ctx)
		return buffer.read(length)

ByteArray = BufferType()
IntegerByteArray = BufferType(Int)

class PositionType(Type):
	pytype : type = tuple
	MAX_SIZE : int = 8

	# TODO THIS IS FOR 1.12.2!!! Make a generic version-less?

	def write(self, data:tuple, buffer:io.BytesIO, ctx:object=None):
		packed = ((0x3FFFFFF & data[0]) << 38) | ((0xFFF & data[1]) << 26) | (0x3FFFFFF & data[2])
		UnsignedLong.write(packed, buffer, ctx=ctx)

	def read(self, buffer:io.BytesIO, ctx:object=None) -> tuple:
		packed = UnsignedLong.read(buffer)
		x = packed >> 38
		y = (packed >> 24) & 0xFFF
		z = packed & 0x3FFFFFF
		return (x, y, z)

Position = PositionType()

class UUIDType(Type):
	pytype : type = str # TODO maybe use partial with uuid constructor?
	MAX_SIZE : int = 16

	def write(self, data:uuid.UUID, buffer:io.BytesIO, ctx:object=None):
		buffer.write(int(data).to_bytes(self.MAX_SIZE, 'big'))

	def read(self, buffer:io.BytesIO, ctx:object=None) -> uuid.UUID:
		return uuid.UUID(int=int.from_bytes(buffer.read(self.MAX_SIZE), 'big'))

UUID = UUIDType()

class ArrayType(Type):
	pytype : type = list
	counter : Union[int, Type]
	content : Type

	def __init__(self, content:Type, counter:Union[int, Type] = VarInt):
		self.content = content
		self.counter = counter

	def write(self, data:List[Any], buffer:io.BytesIO, ctx:object=None):
		if isinstance(self.counter, Type):
			self.counter.write(len(data), buffer, ctx=ctx)
		for i, el in enumerate(data):
			self.content.write(el, buffer, ctx=ctx)
			if isinstance(self.counter, int) and i >= self.counter:
				break # jank but should do

	def read(self, buffer:io.BytesIO, ctx:object=None) -> List[Any]:
		length = self.counter if isinstance(self.counter, int) else self.counter.read(buffer, ctx=ctx)
		return [ self.content.read(buffer, ctx=ctx) for _ in range(length) ]

class OptionalType(Type):
	t : Type

	def __init__(self, t:Type):
		self.t = t
		self.pytype = t.pytype

	def write(self, data:Optional[Any], buffer:io.BytesIO, ctx:object=None):
		Boolean.write(bool(data), buffer, ctx=ctx)
		if data:
			self.t.write(data, buffer, ctx=ctx)

	def read(self, buffer:io.BytesIO, ctx:object=None) -> Optional[Any]:
		if Boolean.read(buffer, ctx=ctx):
			return self.t.read(buffer, ctx=ctx)
		return None

class SwitchType(Type):
	field : str
	mappings : Dict[Any, Type]

	def __init__(self, watch:str, mappings:Dict[Any, Type], default:Type = None):
		self.field = watch
		self.mappings = mappings
		self.default = default

	def write(self, data:Any, buffer:io.BytesIO, ctx:object=None):
		watched = getattr(ctx, self.field)
		if watched in self.mappings:
			return self.mappings[watched].write(data, buffer, ctx=ctx)
		elif self.default:
			return self.default.write(data, buffer, ctx=ctx)

	def read(self, buffer:io.BytesIO, ctx:object=None) -> Optional[Any]:
		watched = getattr(ctx, self.field)
		if watched in self.mappings:
			return self.mappings[watched].read(buffer, ctx=ctx)
		elif self.default:
			return self.default.read(buffer, ctx=ctx)
		return None

class StructType(Type):
	pytype : type = dict
	fields : Tuple[Tuple[str, Type], ...]

	def __init__(self, *args:Tuple[str, Type]):
		self.fields = args

	def write(self, data:Dict[str, Any], buffer:io.BytesIO, ctx:object=None):
		for k, t in self.fields:
			t.write(data[k], buffer, ctx=ctx)

	def read(self, buffer:io.BytesIO, ctx:object=None) -> Dict[str, Any]:
		return { k : t.read(buffer, ctx=ctx) for k, t in self.fields }


