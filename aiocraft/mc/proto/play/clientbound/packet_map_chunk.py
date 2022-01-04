"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketMapChunk(Packet):
	__slots__ = ( 'id', 'skyLightMask', 'z', 'blockLight', 'emptySkyLightMask', 'x', 'compressedChunkData', 'primaryBitMask', 'blockEntities', 'chunkData', 'groundUp', 'emptyBlockLightMask', 'bitMap', 'addBitMap', 'ignoreOldData', 'skyLight', 'biomes', 'blockLightMask', 'trustEdges', 'heightmaps' )
	
	skyLightMask : list
	z : int
	blockLight : list
	emptySkyLightMask : list
	x : int
	compressedChunkData : bytes
	primaryBitMask : list
	blockEntities : list
	chunkData : bytes
	groundUp : bool
	emptyBlockLightMask : list
	bitMap : Union[int,list]
	addBitMap : int
	ignoreOldData : bool
	skyLight : list
	biomes : Union[bytes,list]
	blockLightMask : list
	trustEdges : bool
	heightmaps : bytes

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 33,
		47 : 33,
		76 : 32,
		107 : 32,
		108 : 32,
		109 : 32,
		110 : 32,
		201 : 32,
		210 : 32,
		304 : 32,
		315 : 32,
		321 : 33,
		327 : 33,
		331 : 33,
		335 : 32,
		338 : 32,
		340 : 32,
		351 : 33,
		393 : 34,
		401 : 34,
		402 : 34,
		403 : 34,
		404 : 34,
		477 : 33,
		480 : 33,
		490 : 33,
		498 : 33,
		573 : 34,
		575 : 34,
		578 : 34,
		709 : 34,
		734 : 33,
		735 : 33,
		736 : 33,
		751 : 32,
		755 : 34,
		756 : 34,
		757 : 34,
		1073741839 : 33
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', UnsignedShort ), ( 'addBitMap', UnsignedShort ), ( 'compressedChunkData', ByteArray ) ],
		47 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', UnsignedShort ), ( 'chunkData', ByteArray ) ],
		76 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ) ],
		107 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ) ],
		108 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ) ],
		109 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ) ],
		110 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		201 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		210 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		304 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		315 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		321 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		327 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		331 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		335 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		338 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		340 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		351 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		393 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		401 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		402 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		403 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		404 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		477 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		480 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		490 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		498 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		573 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'biomes', SwitchType('groundUp', { 'false' : Void, 'true' : ArrayType(Int, 1024, ) }, None, ) ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		575 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'biomes', SwitchType('groundUp', { 'false' : Void, 'true' : ArrayType(Int, 1024, ) }, None, ) ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		578 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'biomes', SwitchType('groundUp', { 'false' : Void, 'true' : ArrayType(Int, 1024, ) }, None, ) ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		709 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'biomes', SwitchType('groundUp', { 'false' : Void, 'true' : ArrayType(Int, 1024, ) }, None, ) ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		734 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'ignoreOldData', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'biomes', SwitchType('groundUp', { 'false' : Void, 'true' : ArrayType(Int, 1024, ) }, None, ) ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		735 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'ignoreOldData', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'biomes', SwitchType('groundUp', { 'false' : Void, 'true' : ArrayType(Int, 1024, ) }, None, ) ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		736 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'ignoreOldData', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'biomes', SwitchType('groundUp', { 'false' : Void, 'true' : ArrayType(Int, 1024, ) }, None, ) ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		751 : [ ( 'x', Int ), ( 'z', Int ), ( 'groundUp', Boolean ), ( 'bitMap', VarInt ), ( 'heightmaps', NBTTag ), ( 'biomes', SwitchType('groundUp', { 'false' : Void, 'true' : ArrayType(VarInt, VarInt, ) }, None, ) ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		755 : [ ( 'x', Int ), ( 'z', Int ), ( 'bitMap', ArrayType(Long, VarInt, ) ), ( 'heightmaps', NBTTag ), ( 'biomes', ArrayType(VarInt, VarInt, ) ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		756 : [ ( 'x', Int ), ( 'z', Int ), ( 'bitMap', ArrayType(Long, VarInt, ) ), ( 'heightmaps', NBTTag ), ( 'biomes', ArrayType(VarInt, VarInt, ) ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ],
		757 : [ ( 'x', Int ), ( 'z', Int ), ( 'heightmaps', NBTTag ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(TrailingData, VarInt, ) ), ( 'trustEdges', Boolean ), ( 'skyLightMask', ArrayType(Long, VarInt, ) ), ( 'blockLightMask', ArrayType(Long, VarInt, ) ), ( 'emptySkyLightMask', ArrayType(Long, VarInt, ) ), ( 'emptyBlockLightMask', ArrayType(Long, VarInt, ) ), ( 'skyLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ), ( 'blockLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ) ],
		1073741839 : [ ( 'x', Int ), ( 'z', Int ), ( 'primaryBitMask', ArrayType(Long, VarInt, ) ), ( 'heightmaps', NBTTag ), ( 'biomes', ArrayType(VarInt, VarInt, ) ), ( 'chunkData', ByteArray ), ( 'blockEntities', ArrayType(NBTTag, VarInt, ) ) ]
	}
