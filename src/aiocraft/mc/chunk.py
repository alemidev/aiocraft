import io
import math
import logging
import struct

from typing import Dict, Tuple, Any

import numpy as np

from aiocraft.mc.types import VarInt, Short, UnsignedByte, Type, Context

class BitStream:
	data : bytes
	cursor : int
	size : int
	
	def __init__(self, data:bytes, size:int):
		self.data = data
		self.cursor = 0
		self.size = size if size > 0 else len(self.data) * 8

	def __len__(self) -> int:
		return self.size - self.cursor

	def read(self, size:int) -> int:
		if len(self) < size:
			raise ValueError(f"Not enough bits ({len(self)} left, {size} requested)")
		# Calculate splice indexes
		start_byte = math.floor(self.cursor / 8)
		end_byte = math.ceil((self.cursor + size) / 8)
		# Construct int from bytes
		buf = 0
		delta = end_byte-start_byte
		fmt = f">{delta}B" # TODO endianness doesn't seem to matter?
		unpacked = struct.unpack(fmt, self.data[start_byte:end_byte])
		for (i, x) in enumerate(unpacked):
			# buf |= (x << (8 * (len(unpacked) - (i + 1))))
			buf |= (x << (8 * i))
		# Trim extra bits
		# offset = self.cursor % 8 # start
		offset = (8*delta) - ((self.cursor + size) % (8 * delta)) # end
		if offset > 0:
			buf = buf >> offset # There's an extra 1 to the left in air, maybe shift 1 bit less?
		buf = buf & ((1 << size) - 1)
		# Increment and return
		self.cursor += size 
		return buf

class PalettedContainer(Type):
	"""
	block_data = [ UnsignedLong.read(buf) for _ in range(container_size) ]
	for y in range(self.size):
		for z in range(self.size):
			for x in range(self.size):
				i = x + ((y * 16) + z) * 16
				start_long = (i * bits) // 64
				start_offset = (i * bits) % 64
				end_long = ((i + 1) * bits - 1) // 64
				if start_long == end_long:
					block = (block_data[start_long] >> start_offset) & max_val
				else:
					end_offset = 64 - start_offset
					block = (block_data[start_long] >> start_offset |
							 block_data[end_long] << end_offset) & max_val
	"""
	pytype : type
	threshold : int
	size : int

	def __init__(self, threshold:int, size:int):
		self.threshold = threshold
		self.size = size

	def write(self, data, buffer:io.BytesIO, ctx:Context):
		raise NotImplementedError

	def read(self, buffer:io.BytesIO, ctx:Context):
		bits = UnsignedByte.read(buffer, ctx=ctx) # FIXME if bits > 4 it reads trash
		#logging.debug("[%d|%d@%d] Bits per block : %d", ctx.x, ctx.z, ctx.sec, bits)
		if bits < 4:
			bits = 4
		if bits >= self.threshold:
			bits = 13 # this should not be hardcoded but we have no way to calculate all possible block states
		palette_len = VarInt.read(buffer, ctx=ctx)
		palette = np.zeros((palette_len,), dtype='int32')
		for i in range(palette_len):
			palette[i] = VarInt.read(buffer, ctx=ctx)
		# logging.debug("[%d|%d@%d] Palette section : [%d] %s", ctx.x, ctx.z, ctx.sec, palette_len, str(palette))
		container_size = VarInt.read(buffer, ctx=ctx)
		section = np.zeros((self.size, self.size, self.size), dtype='int32')
		stream = BitStream(buffer.read(container_size * 8), container_size*8*8) # a Long is 64 bits long
		# logging.debug("[%d|%d@%d] Buffer : %s", ctx.x, ctx.z, ctx.sec, stream.data)
		for y in range(self.size):
			for z in range(self.size):
				for x in range(self.size):
					val = stream.read(bits)
					if val >= len(palette):
						logging.warning("out of bounds : %d (%d)", val, len(palette)) # FIXME happens a lot!
						section[x, y, z] = val
						continue
					section[x, y, z] = palette[val] if bits < self.threshold else val
		return section

BiomeContainer = PalettedContainer(4, 4)
BlockStateContainer = PalettedContainer(9, 16)

class HalfByteArrayType(Type):
	size : int

	def __init__(self, size:int):
		self.size = size

	def write(self, data, buffer:io.BytesIO, ctx:Context):
		raise NotImplementedError

	def read(self, buffer:io.BytesIO, ctx:Context):
		section = np.empty((self.size, self.size, self.size), dtype='int32')
		bit_buffer = BitStream(buffer.read((self.size**3)//2), (self.size**3)*4)
		for y in range(self.size):
			for z in range(self.size):
				for x in range(self.size):
					section[x, y, z] = bit_buffer.read(4)
		return section

BlockLightSection = HalfByteArrayType(16)
SkyLightSection = HalfByteArrayType(16)

class NewChunkSectionType(Type):
	pytype : type

	def write(self, data, buffer:io.BytesIO, ctx:Context):
		raise NotImplementedError

	def read(self, buffer:io.BytesIO, ctx:Context):
		block_count = Short.read(buffer, ctx=ctx)
		block_states = BlockStateContainer.read(buffer, ctx=ctx)
		biomes = BiomeContainer.read(buffer, ctx=ctx)
		return (
			block_count,
			block_states,
			biomes
		)

class OldChunkSectionType(Type):
	pytype : type

	def write(self, data, buffer:io.BytesIO, ctx:Context):
		raise NotImplementedError

	def read(self, buffer:io.BytesIO, ctx:Context):
		block_states = BlockStateContainer.read(buffer, ctx=ctx)
		block_light = BlockLightSection.read(buffer, ctx=ctx)
		if ctx.overworld:
			sky_light = SkyLightSection.read(buffer, ctx=ctx)
		else:
			sky_light = np.empty((16, 16, 16), dtype='int32')
		return (
			block_states,
			block_light,
			sky_light
		)

ChunkSection = OldChunkSectionType()

class Chunk(Type):
	x : int
	z : int
	bitmask : int
	ground_up_continuous : bool
	blocks : np.ndarray
	block_light : np.ndarray
	sky_light : np.ndarray
	biomes: bytes

	def __init__(self, x:int, z:int, bitmask:int, ground_up_continuous:bool):
		self.x = x
		self.z = z
		self.bitmask = bitmask
		self.blocks = np.zeros((16, 256, 16), dtype='int32')
		self.block_light = np.zeros((16, 256, 16), dtype='int32')
		self.sky_light = np.zeros((16, 256, 16), dtype='int32')
		self.ground_up_continuous = ground_up_continuous

	def __getitem__(self, item:Any):
		return self.blocks[item]

	def read(self, buffer:io.BytesIO, ctx:Context):
		ctx.x = self.x
		ctx.z = self.z
		for i in range(16):
			if (self.bitmask >> i) & 1:
				ctx.sec = i
				block_states, block_light, sky_light = ChunkSection.read(buffer, ctx=ctx)
				self.blocks[:, i*16 : (i+1)*16, :] = block_states
				self.block_light[:, i*16 : (i+1)*16, :] = block_light
				self.sky_light[:, i*16 : (i+1)*16, :] = sky_light
		if self.ground_up_continuous:
			self.biomes = buffer.read(256) # 16x16
		if buffer.read():
			logging.warning("Leftover data in chunk buffer")
		return self

class World:
	chunks : Dict[Tuple[int, int], Chunk]

	def __init__(self):
		self.chunks = {}

	def __getitem__(self, item:Tuple[int, int, int]):
		return self.get(*item)

	def get(self, x:int, y:int, z:int) -> int:
		coord = (x//16, z//16)
		if coord not in self.chunks:
			raise KeyError(f"Chunk {coord} not loaded")
		return self.chunks[coord][int(x%16), int(y), int(z%16)]

	def put(self, chunk:Chunk, x:int, z:int):
		self.chunks[(x,z)] = chunk
