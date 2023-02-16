"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketEntityUpdateAttributes(Packet):
	__slots__ = ( 'id', 'entityId', 'properties' )
	
	entityId : int
	properties : list

	def __init__(self, proto:int,
		entityId:int=None,
		properties:list=None,
		**kwargs
	):
		super().__init__(proto,
			entityId=entityId,
			properties=properties
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		107 : 75,
		108 : 75,
		109 : 75,
		110 : 74,
		201 : 74,
		210 : 74,
		304 : 74,
		315 : 74,
		321 : 76,
		327 : 76,
		331 : 76,
		335 : 77,
		338 : 78,
		340 : 78,
		351 : 80,
		393 : 82,
		401 : 82,
		402 : 82,
		403 : 82,
		404 : 82,
		477 : 88,
		480 : 88,
		490 : 88,
		498 : 88,
		573 : 89,
		575 : 89,
		578 : 89,
		709 : 89,
		734 : 88,
		735 : 88,
		736 : 88,
		751 : 88,
		755 : 99,
		756 : 99,
		757 : 100,
		758 : 100,
		759 : 101,
		760 : 104,
		761 : 102
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		107 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		108 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		109 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		110 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		201 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		210 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		304 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		315 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		321 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		327 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		331 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		335 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		338 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		340 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		351 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		393 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		401 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		402 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		403 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		404 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		477 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		480 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		490 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		498 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		573 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		575 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		578 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		709 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		734 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		735 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		736 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		751 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		755 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), VarInt, ) ) ],
		756 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), VarInt, ) ) ],
		757 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), VarInt, ) ) ],
		758 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), VarInt, ) ) ],
		759 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), VarInt, ) ) ],
		760 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), VarInt, ) ) ],
		761 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'uuid', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), VarInt, ) ) ]
	}
