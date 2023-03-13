"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketMultiBlockChange(Packet):
	__slots__ = ( 'id', 'chunkCoordinates', 'chunkX', 'chunkZ', 'notTrustEdges', 'records', 'suppressLightUpdates' )
	
	chunkCoordinates : int
	chunkX : int
	chunkZ : int
	notTrustEdges : bool
	records : list
	suppressLightUpdates : bool

	def __init__(self, proto:int,
		chunkCoordinates:int=None,
		chunkX:int=None,
		chunkZ:int=None,
		notTrustEdges:bool=None,
		records:list=None,
		suppressLightUpdates:bool=None,
		**kwargs
	):
		super().__init__(proto,
			chunkCoordinates=chunkCoordinates,
			chunkX=chunkX,
			chunkZ=chunkZ,
			notTrustEdges=notTrustEdges,
			records=records,
			suppressLightUpdates=suppressLightUpdates
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 34,
		76 : 16,
		107 : 16,
		108 : 16,
		109 : 16,
		110 : 16,
		201 : 16,
		210 : 16,
		304 : 16,
		315 : 16,
		321 : 17,
		327 : 17,
		331 : 17,
		335 : 16,
		338 : 16,
		340 : 16,
		351 : 15,
		393 : 15,
		401 : 15,
		402 : 15,
		403 : 15,
		404 : 15,
		477 : 15,
		480 : 15,
		490 : 15,
		498 : 15,
		573 : 16,
		575 : 16,
		578 : 16,
		709 : 16,
		734 : 15,
		735 : 15,
		736 : 15,
		751 : 59,
		755 : 63,
		756 : 63,
		757 : 63,
		758 : 63,
		759 : 61,
		760 : 64,
		761 : 63
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		76 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		107 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		108 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		109 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		110 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		201 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		210 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		304 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		315 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		321 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		327 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		331 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		335 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		338 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		340 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		351 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		393 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		401 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		402 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		403 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		404 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		477 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		480 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		490 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		498 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		573 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		575 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		578 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		709 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		734 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		735 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		736 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ), ( 'records', ArrayType(StructType(( 'horizontalPos', Byte ), ( 'y', Byte ), ( 'blockId', VarInt ), ), VarInt, ) ) ],
		751 : [ ( 'chunkCoordinates', Long ), ( 'notTrustEdges', Boolean ), ( 'records', ArrayType(TrailingData, VarInt, ) ) ],
		755 : [ ( 'chunkCoordinates', Long ), ( 'notTrustEdges', Boolean ), ( 'records', ArrayType(TrailingData, VarInt, ) ) ],
		756 : [ ( 'chunkCoordinates', Long ), ( 'notTrustEdges', Boolean ), ( 'records', ArrayType(TrailingData, VarInt, ) ) ],
		757 : [ ( 'chunkCoordinates', Long ), ( 'notTrustEdges', Boolean ), ( 'records', ArrayType(TrailingData, VarInt, ) ) ],
		758 : [ ( 'chunkCoordinates', Long ), ( 'notTrustEdges', Boolean ), ( 'records', ArrayType(TrailingData, VarInt, ) ) ],
		759 : [ ( 'chunkCoordinates', Long ), ( 'notTrustEdges', Boolean ), ( 'records', ArrayType(VarInt, VarInt, ) ) ],
		760 : [ ( 'chunkCoordinates', Long ), ( 'suppressLightUpdates', Boolean ), ( 'records', ArrayType(VarInt, VarInt, ) ) ],
		761 : [ ( 'chunkCoordinates', Long ), ( 'suppressLightUpdates', Boolean ), ( 'records', ArrayType(VarInt, VarInt, ) ) ]
	}
