"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketExplosion(Packet):
	__slots__ = ( 'id', 'affectedBlockOffsets', 'playerMotionX', 'playerMotionY', 'playerMotionZ', 'radius', 'x', 'y', 'z' )
	
	affectedBlockOffsets : list
	playerMotionX : float
	playerMotionY : float
	playerMotionZ : float
	radius : float
	x : float
	y : float
	z : float

	def __init__(self, proto:int,
		affectedBlockOffsets:list=None,
		playerMotionX:float=None,
		playerMotionY:float=None,
		playerMotionZ:float=None,
		radius:float=None,
		x:float=None,
		y:float=None,
		z:float=None,
		**kwargs
	):
		super().__init__(proto,
			affectedBlockOffsets=affectedBlockOffsets,
			playerMotionX=playerMotionX,
			playerMotionY=playerMotionY,
			playerMotionZ=playerMotionZ,
			radius=radius,
			x=x,
			y=y,
			z=z
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 39,
		76 : 27,
		107 : 28,
		108 : 28,
		109 : 28,
		110 : 28,
		201 : 28,
		210 : 28,
		304 : 28,
		315 : 28,
		321 : 29,
		327 : 29,
		331 : 29,
		335 : 28,
		338 : 28,
		340 : 28,
		351 : 29,
		393 : 30,
		401 : 30,
		402 : 30,
		403 : 30,
		404 : 30,
		477 : 28,
		480 : 28,
		490 : 28,
		498 : 28,
		573 : 29,
		575 : 29,
		578 : 29,
		709 : 29,
		734 : 28,
		735 : 28,
		736 : 28,
		751 : 27,
		755 : 28,
		756 : 28,
		757 : 28
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		76 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		107 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		108 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		109 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		110 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		201 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		210 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		304 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		315 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		321 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		327 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		331 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		335 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		338 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		340 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		351 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		393 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		401 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		402 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		403 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		404 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		477 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		480 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		490 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		498 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		573 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		575 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		578 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		709 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		734 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		735 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		736 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		751 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), Int, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		755 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), VarInt, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		756 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), VarInt, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ],
		757 : [ ( 'x', Float ), ( 'y', Float ), ( 'z', Float ), ( 'radius', Float ), ( 'affectedBlockOffsets', ArrayType(StructType(( 'x', Byte ), ( 'y', Byte ), ( 'z', Byte ), ), VarInt, ) ), ( 'playerMotionX', Float ), ( 'playerMotionY', Float ), ( 'playerMotionZ', Float ) ]
	}