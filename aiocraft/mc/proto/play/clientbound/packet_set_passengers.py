"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketSetPassengers(Packet):
	__slots__ = ( 'id', 'entityId', 'passengers' )
	
	entityId : int
	passengers : list

	def __init__(self, proto:int,
		entityId:int=None,
		passengers:list=None,
		**kwargs
	):
		super().__init__(proto,
			entityId=entityId,
			passengers=passengers
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		107 : 64,
		108 : 64,
		109 : 64,
		110 : 64,
		201 : 64,
		210 : 64,
		304 : 64,
		315 : 64,
		321 : 66,
		327 : 66,
		331 : 66,
		335 : 66,
		338 : 67,
		340 : 67,
		351 : 68,
		393 : 70,
		401 : 70,
		402 : 70,
		403 : 70,
		404 : 70,
		477 : 74,
		480 : 74,
		490 : 74,
		498 : 74,
		573 : 75,
		575 : 75,
		578 : 75,
		709 : 76,
		734 : 75,
		735 : 75,
		736 : 75,
		751 : 75,
		755 : 84,
		756 : 84,
		757 : 84
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		107 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		108 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		109 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		110 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		201 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		210 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		304 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		315 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		321 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		327 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		331 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		335 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		338 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		340 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		351 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		393 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		401 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		402 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		403 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		404 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		477 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		480 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		490 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		498 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		573 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		575 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		578 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		709 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		734 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		735 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		736 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		751 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		755 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		756 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ],
		757 : [ ( 'entityId', VarInt ), ( 'passengers', ArrayType(VarInt, VarInt, ) ) ]
	}
