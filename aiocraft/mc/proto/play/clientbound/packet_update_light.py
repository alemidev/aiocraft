"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketUpdateLight(Packet):
	__slots__ = ( 'id', 'blockLight', 'blockLightMask', 'chunkX', 'chunkZ', 'data', 'emptyBlockLightMask', 'emptySkyLightMask', 'skyLight', 'skyLightMask', 'trustEdges' )
	
	blockLight : list
	blockLightMask : Union[int,list]
	chunkX : int
	chunkZ : int
	data : bytes
	emptyBlockLightMask : Union[int,list]
	emptySkyLightMask : Union[int,list]
	skyLight : list
	skyLightMask : Union[int,list]
	trustEdges : bool

	def __init__(self, proto:int,
		blockLight:list=None,
		blockLightMask:Union[int,list]=None,
		chunkX:int=None,
		chunkZ:int=None,
		data:bytes=None,
		emptyBlockLightMask:Union[int,list]=None,
		emptySkyLightMask:Union[int,list]=None,
		skyLight:list=None,
		skyLightMask:Union[int,list]=None,
		trustEdges:bool=None,
		**kwargs
	):
		super().__init__(proto,
			blockLight=blockLight,
			blockLightMask=blockLightMask,
			chunkX=chunkX,
			chunkZ=chunkZ,
			data=data,
			emptyBlockLightMask=emptyBlockLightMask,
			emptySkyLightMask=emptySkyLightMask,
			skyLight=skyLight,
			skyLightMask=skyLightMask,
			trustEdges=trustEdges
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		477 : 36,
		480 : 36,
		490 : 36,
		498 : 36,
		573 : 37,
		575 : 37,
		578 : 37,
		709 : 37,
		734 : 36,
		735 : 36,
		736 : 36,
		751 : 35,
		755 : 37,
		756 : 37,
		757 : 37,
		758 : 37,
		759 : 34,
		760 : 36,
		761 : 35
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		477 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		480 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		490 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		498 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		573 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		575 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		578 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		709 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		734 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'trustEdges', Boolean ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		735 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'trustEdges', Boolean ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		736 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'trustEdges', Boolean ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		751 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'trustEdges', Boolean ), ( 'skyLightMask', VarInt ), ( 'blockLightMask', VarInt ), ( 'emptySkyLightMask', VarInt ), ( 'emptyBlockLightMask', VarInt ), ( 'data', TrailingData ) ],
		755 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'trustEdges', Boolean ), ( 'skyLightMask', ArrayType(Long, VarInt, ) ), ( 'blockLightMask', ArrayType(Long, VarInt, ) ), ( 'emptySkyLightMask', ArrayType(Long, VarInt, ) ), ( 'emptyBlockLightMask', ArrayType(Long, VarInt, ) ), ( 'skyLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ), ( 'blockLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ) ],
		756 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'trustEdges', Boolean ), ( 'skyLightMask', ArrayType(Long, VarInt, ) ), ( 'blockLightMask', ArrayType(Long, VarInt, ) ), ( 'emptySkyLightMask', ArrayType(Long, VarInt, ) ), ( 'emptyBlockLightMask', ArrayType(Long, VarInt, ) ), ( 'skyLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ), ( 'blockLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ) ],
		757 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'trustEdges', Boolean ), ( 'skyLightMask', ArrayType(Long, VarInt, ) ), ( 'blockLightMask', ArrayType(Long, VarInt, ) ), ( 'emptySkyLightMask', ArrayType(Long, VarInt, ) ), ( 'emptyBlockLightMask', ArrayType(Long, VarInt, ) ), ( 'skyLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ), ( 'blockLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ) ],
		758 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'trustEdges', Boolean ), ( 'skyLightMask', ArrayType(Long, VarInt, ) ), ( 'blockLightMask', ArrayType(Long, VarInt, ) ), ( 'emptySkyLightMask', ArrayType(Long, VarInt, ) ), ( 'emptyBlockLightMask', ArrayType(Long, VarInt, ) ), ( 'skyLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ), ( 'blockLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ) ],
		759 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'trustEdges', Boolean ), ( 'skyLightMask', ArrayType(Long, VarInt, ) ), ( 'blockLightMask', ArrayType(Long, VarInt, ) ), ( 'emptySkyLightMask', ArrayType(Long, VarInt, ) ), ( 'emptyBlockLightMask', ArrayType(Long, VarInt, ) ), ( 'skyLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ), ( 'blockLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ) ],
		760 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'trustEdges', Boolean ), ( 'skyLightMask', ArrayType(Long, VarInt, ) ), ( 'blockLightMask', ArrayType(Long, VarInt, ) ), ( 'emptySkyLightMask', ArrayType(Long, VarInt, ) ), ( 'emptyBlockLightMask', ArrayType(Long, VarInt, ) ), ( 'skyLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ), ( 'blockLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ) ],
		761 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ), ( 'trustEdges', Boolean ), ( 'skyLightMask', ArrayType(Long, VarInt, ) ), ( 'blockLightMask', ArrayType(Long, VarInt, ) ), ( 'emptySkyLightMask', ArrayType(Long, VarInt, ) ), ( 'emptyBlockLightMask', ArrayType(Long, VarInt, ) ), ( 'skyLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ), ( 'blockLight', ArrayType(ArrayType(Byte, VarInt, ), VarInt, ) ) ]
	}
