"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketEntityDestroy(Packet):
	__slots__ = ( 'id', 'entityIds' )
	
	entityIds : list

	def __init__(self, proto:int,
		entityIds:list=None
	):
		super().__init__(proto,
			entityIds=entityIds
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 19,
		76 : 48,
		107 : 48,
		108 : 48,
		109 : 48,
		110 : 48,
		201 : 48,
		210 : 48,
		304 : 48,
		315 : 48,
		321 : 50,
		327 : 50,
		331 : 50,
		335 : 49,
		338 : 50,
		340 : 50,
		351 : 51,
		393 : 53,
		401 : 53,
		402 : 53,
		403 : 53,
		404 : 53,
		477 : 55,
		480 : 55,
		490 : 55,
		498 : 55,
		573 : 56,
		575 : 56,
		578 : 56,
		709 : 56,
		734 : 55,
		735 : 55,
		736 : 55,
		751 : 54,
		756 : 58,
		757 : 58
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		76 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		107 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		108 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		109 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		110 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		201 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		210 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		304 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		315 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		321 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		327 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		331 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		335 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		338 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		340 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		351 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		393 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		401 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		402 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		403 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		404 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		477 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		480 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		490 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		498 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		573 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		575 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		578 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		709 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		734 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		735 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		736 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		751 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		756 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ],
		757 : [ ( 'entityIds', ArrayType(VarInt, VarInt, ) ) ]
	}
