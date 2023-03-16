import io
import struct
import asyncio
import json
import uuid

import logging
import pynbt

from typing import List, Tuple, Dict, Any, Union, Optional, Callable, Type as Class

from .definitions import Item

class Context(object):
	def __init__(self, **kwargs):
		for k, v in kwargs.items():
			setattr(self, k, v)

	def serialize(self) -> dict:
		return vars(self) # is this reliable?

	def __getattr__(self, name) -> Any:
		return None # return None rather than raising an exc

	def __str__(self) -> str:
		return json.dumps(self.serialize(), indent=2, default=str, sort_keys=True)

	def __repr__(self) -> str:
		values = ( f"{k}={repr(v)}" for k,v in vars(self).items() )
		return f"Context({', '.join(values)})"

class Type(object):
	pytype : Union[type, Callable] = lambda x : x

	def write(self, data:Any, buffer:io.BytesIO, ctx:Context) -> None:
		"""Write data to a packet buffer"""
		raise NotImplementedError
	
	def read(self, buffer:io.BytesIO, ctx:Context) -> Any:
		"""Read data off a packet buffer"""
		raise NotImplementedError

	def check(self, ctx:Context) -> bool:
		"""Check if this type exists in this context"""
		return True

class VoidType(Type):

	def write(self, v:None, buffer:io.BytesIO, ctx:Context):
		pass

	def read(self, buffer:io.BytesIO, ctx:Context) -> None:
		return None

Void = VoidType()

class UnimplementedDataType(Type):
	pytype : type = bytes

	def write(self, data:bytes, buffer:io.BytesIO, ctx:Context):
		if data:
			buffer.write(data)

	def read(self, buffer:io.BytesIO, ctx:Context) -> bytes:
		return buffer.read()

TrailingData = UnimplementedDataType()

class PrimitiveType(Type):
	size : int
	fmt : str

	def __init__(self, pytype:type, fmt:str, size:int):
		self.pytype = pytype
		self.fmt = fmt
		self.size = size

	def write(self, data:Any, buffer:io.BytesIO, ctx:Context):
		buffer.write(struct.pack(self.fmt, data))

	def read(self, buffer:io.BytesIO, ctx:Context) -> Any:
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

def nbt_to_py(item:pynbt.BaseTag) -> Any:
	if isinstance(item, pynbt.TAG_Compound):
		return { k: nbt_to_py(v) for k,v in dict(item).items() }
	if isinstance(item, pynbt.TAG_List):
		return [ nbt_to_py(v) for v in list(item) ]
	if isinstance(item, pynbt.BaseTag):
		return item.value
	return item

class NBTType(Type):
	pytype : type = dict

	def write(self, data:Optional[dict], buffer:io.BytesIO, ctx:Context):
		if data is None:
			buffer.write(b'\x00')
		else:
			pynbt.NBTFile(value=data).save(buffer)

	def read(self, buffer:io.BytesIO, ctx:Context) -> Optional[dict]:
		head = Byte.read(buffer, ctx)
		if head == 0x0:
			return None
		buffer.seek(-1,1) # go back 1 byte
		return nbt_to_py(pynbt.NBTFile(io=buffer))

NBTTag = NBTType()

class VarLenPrimitive(Type):
	pytype : type = int
	max_bytes : int

	def __init__(self, max_bytes:int):
		self.max_bytes = max_bytes

	def write(self, data:int, buffer:io.BytesIO, ctx:Context):
		count = 0 # TODO raise exceptions
		while count < self.max_bytes:
			byte = data & 0b01111111
			data >>= 7
			if data > 0:
				byte |= 0b10000000
			buffer.write(struct.pack("B", byte))
			count += 1
			if not data:
				break

	def read(self, buffer:io.BytesIO, ctx:Context) -> int:
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
		self.write(data, buf, Context())
		buf.seek(0)
		return buf.read()

	def deserialize(self, data:bytes) -> int:
		buf = io.BytesIO(data)
		return self.read(buf, Context())

VarInt = VarLenPrimitive(5)
VarLong = VarLenPrimitive(10)

class StringType(Type):
	pytype : type = str

	def write(self, data:str, buffer:io.BytesIO, ctx:Context):
		encoded = data.encode('utf-8')
		VarInt.write(len(encoded), buffer, ctx=ctx)
		buffer.write(encoded)

	def read(self, buffer:io.BytesIO, ctx:Context) -> str:
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

	def write(self, data:bytes, buffer:io.BytesIO, ctx:Context):
		self.count.write(len(data), buffer, ctx=ctx)
		buffer.write(data)

	def read(self, buffer:io.BytesIO, ctx:Context) -> bytes:
		length = self.count.read(buffer, ctx=ctx)
		return buffer.read(length)

ByteArray = BufferType()
IntegerByteArray = BufferType(Int)

def twos_comp(val, bits):
	"""compute the 2's complement of int value val"""
	if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
		val = val - (1 << bits)        # compute negative value
	return val                         # return positive value as is


class PositionType(Type):
	pytype : type = tuple
	MAX_SIZE : int = 8

	def write(self, data:tuple, buffer:io.BytesIO, ctx:Context):
		if ctx._proto <= 441:
			packed = ((0x3FFFFFF & data[0]) << 38) \
				| ((0xFFF & data[1]) << 26) \
				| (0x3FFFFFF & data[2])
			UnsignedLong.write(packed, buffer, ctx=ctx)
		else:
			packed = ((0x3FFFFFF & data[0]) << 38) \
				| ((0x3FFFFFF & data[2]) << 12) \
				| (0xFFF & data[1])
			UnsignedLong.write(packed, buffer, ctx=ctx)
			pass

	def read(self, buffer:io.BytesIO, ctx:Context) -> tuple:
		if ctx._proto <= 441:
			packed = UnsignedLong.read(buffer, ctx)
			x = twos_comp(packed >> 38, 26)
			y = (packed >> 26) & 0xFFF
			z = twos_comp(packed & 0x3FFFFFF, 26)
			return (x, y, z)
		else:
			packed = UnsignedLong.read(buffer, ctx)
			x = twos_comp(packed >> 38, 26)
			z = twos_comp((packed >> 12) & 0x3FFFFFF, 26)
			y = packed & 0xFFF
			return (x, y, z)

Position = PositionType()

class UUIDType(Type):
	pytype : type = uuid.UUID
	MAX_SIZE : int = 16

	def write(self, data:uuid.UUID, buffer:io.BytesIO, ctx:Context):
		buffer.write(int(data).to_bytes(self.MAX_SIZE, 'big'))

	def read(self, buffer:io.BytesIO, ctx:Context) -> uuid.UUID:
		return uuid.UUID(int=int.from_bytes(buffer.read(self.MAX_SIZE), 'big'))

UUID = UUIDType()

class ArrayType(Type):
	pytype : type = list
	counter : Union[int, Type]
	content : Type

	def __init__(self, content:Type, counter:Union[int, Type] = VarInt):
		self.content = content
		self.counter = counter

	def write(self, data:List[Any], buffer:io.BytesIO, ctx:Context):
		if isinstance(self.counter, Type):
			self.counter.write(len(data), buffer, ctx=ctx)
		for i, el in enumerate(data):
			self.content.write(el, buffer, ctx=ctx)
			if isinstance(self.counter, int) and i >= self.counter:
				break # jank but should do

	def read(self, buffer:io.BytesIO, ctx:Context) -> List[Any]:
		length = self.counter if isinstance(self.counter, int) else self.counter.read(buffer, ctx=ctx)
		out = []
		for _ in range(length):
			out.append(self.content.read(buffer, ctx=ctx))
		return out

class OptionalType(Type):
	t : Type

	def __init__(self, t:Type):
		self.t = t
		self.pytype = t.pytype

	def write(self, data:Optional[Any], buffer:io.BytesIO, ctx:Context):
		Boolean.write(bool(data), buffer, ctx=ctx)
		if data:
			self.t.write(data, buffer, ctx=ctx)

	def read(self, buffer:io.BytesIO, ctx:Context) -> Optional[Any]:
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

	def write(self, data:Any, buffer:io.BytesIO, ctx:Context):
		watched = getattr(ctx, self.field, None)
		if watched is not None and watched in self.mappings:
			return self.mappings[watched].write(data, buffer, ctx=ctx)
		elif self.default:
			return self.default.write(data, buffer, ctx=ctx)

	def read(self, buffer:io.BytesIO, ctx:Context) -> Optional[Any]:
		watched = getattr(ctx, self.field, None)
		if watched is not None and watched in self.mappings:
			return self.mappings[watched].read(buffer, ctx=ctx)
		elif self.default:
			return self.default.read(buffer, ctx=ctx)
		return None

class StructType(Type): # TODO sub objects
	pytype : type = dict
	fields : Tuple[Tuple[str, Type], ...]

	def __init__(self, *args:Tuple[str, Type]):
		self.fields = args

	def write(self, data:Dict[str, Any], buffer:io.BytesIO, ctx:Context):
		for k, t in self.fields:
			t.write(data[k], buffer, ctx=ctx)

	def read(self, buffer:io.BytesIO, ctx:Context) -> Dict[str, Any]:
		return { k : t.read(buffer, ctx=ctx) for k, t in self.fields }

class SlotType(Type):
	pytype : type = Item

	def write(self, data:Item, buffer:io.BytesIO, ctx:Context):
		new_way = ctx._proto > 340
		check_type = Boolean if new_way else Short
		if data:
			check_type.write(True if new_way else data.id, buffer, ctx)
			if new_way:
				VarInt.write(data.id, buffer, ctx)
			Byte.write(data.count, buffer, ctx)
			if not new_way:
				Short.write(data.damage, buffer, ctx)
			NBTTag.write(data.nbt, buffer, ctx) # TODO handle None maybe?
		else:
			check_type.write(False if new_way else -1, buffer, ctx)

	def read(self, buffer:io.BytesIO, ctx:Context) -> Item:
		slot : Dict[Any, Any] = {}
		new_way = ctx._proto > 340
		check_type = Boolean if new_way else Short
		val = check_type.read(buffer, ctx)
		if (new_way and val) or (not new_way and val != -1):
			if new_way:
				slot["id"] = VarInt.read(buffer, ctx)
			else:
				slot["id"] = val
			slot["count"] = Byte.read(buffer, ctx)
			if not new_way:
				slot["damage"] = Short.read(buffer, ctx)
			slot["nbt"] = NBTTag.read(buffer, ctx)
		return Item(**slot)

Slot = SlotType()

class ParticleType(Type):
	pytype : type = dict

	def write(self, data:dict, buffer:io.BytesIO, ctx:Context):
		raise NotImplementedError

	# TODO this changes across versions!
	def read(self, data:dict, buffer:io.BytesIO, ctx:Context):
		data : Dict[str, Any] = {}
		data["id"] = VarInt.read(buffer, ctx)
		if data["id"] in (3, 23):
			data["blockState"] = VarInt.read(buffer, ctx)
		elif data["id"] == 32:
			data["item"] = Slot.read(buffer, ctx)
		elif data["id"] == 14:
			data["red"] = Float.read(buffer, ctx)
			data["green"] = Float.read(buffer, ctx)
			data["blue"] = Float.read(buffer, ctx)
			data["scale"] = Float.read(buffer, ctx)
		return data

Particle = ParticleType()

# wiki.vg does not document these anymore. Minecraft 1.12.2 has these as metadata types
_ENTITY_METADATA_TYPES = {
	0  : Byte,
	1  : VarInt,
	2  : Float,
	3  : String,
	4  : Chat,
	5  : Slot,
	6  : Boolean,
	7  : StructType(("x", Float), ("y", Float), ("z", Float)), # Rotation
	8  : Position,
	9  : OptionalType(Position),
	10 : VarInt, # Direction (Down = 0, Up = 1, North = 2, South = 3, West = 4, East = 5)
	11 : OptionalType(UUID),
	12 : VarInt, # OptBlockID (VarInt) 0 for absent (implies air); otherwise, a block state ID as per the global palette
	13 : NBTTag,
}

_ENTITY_METADATA_TYPES_NEW = {
	0  : Byte,
	1  : VarInt,
	2  : Float,
	3  : String,
	4  : Chat,
	5  : OptionalType(Chat),
	6  : Slot,
	7  : Boolean,
	8  : StructType(("x", Float), ("y", Float), ("z", Float)), 
	9  : Position,
	10 : OptionalType(Position),
	11 : VarInt, # Direction
	12 : OptionalType(UUID),
	13 : VarInt, # Optional BlockID
	14 : NBTTag,
	15 : Particle,
	16 : StructType(("type", VarInt), ("profession", VarInt), ("level", VarInt)),
	17 : OptionalType(VarInt),
	18 : VarInt, # pose
}

# This is for 1.19
# _ENTITY_METADATA_TYPES_NEW = {
# 	0  : Byte,
# 	1  : VarInt,
# 	2  : VarLong,
# 	3  : Float,
# 	4  : String,
# 	5  : Chat,
# 	6  : OptionalType(Chat),
# 	7  : Slot,
# 	8  : Boolean,
# 	9  : StructType(("x", Float), ("y", Float), ("z", Float)), 
# 	10 : Position,
# 	11 : OptionalType(Position),
# 	12 : VarInt, # Direction
# 	13 : OptionalType(UUID),
# 	14 : OptionalType(VarInt), # Optional BlockID
# 	15 : NBTTag,
# 	16 : Particle,
# 	17 : StructType(("type", VarInt), ("profession", VarInt), ("level", VarInt)),
# 	18 : OptionalType(VarInt),
# 	19 : VarInt, # pose
# 	20 : VarInt, # cat variant
# 	21 : VarInt, # frog variant
# 	22 : StructType(("dimension", Identifier), ("position", Position)),
# 	23 : VarInt, # painting variant
# }

class EntityMetadataType(Type):
	pytype : type = dict

	def write(self, data:Dict[int, Any], buffer:io.BytesIO, ctx:Context):
		logging.error("Sending entity metadata isn't implemented yet") # TODO
		buffer.write(b'\xFF')

	def read(self, buffer:io.BytesIO, ctx:Context) -> Dict[int, Any]:
		types_map = _ENTITY_METADATA_TYPES_NEW if ctx._proto > 340 else _ENTITY_METADATA_TYPES
		out : Dict[int, Any] = {}
		while True:
			index = UnsignedByte.read(buffer, ctx)
			if index == 0xFF:
				break
			tp = VarInt.read(buffer, ctx)
			out[index] = types_map[tp].read(buffer, ctx)
		return out

EntityMetadata = EntityMetadataType()
