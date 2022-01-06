"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketUpdateAttributes(Packet):
	__slots__ = ( 'id', 'entityId', 'properties' )
	
	entityId : int
	properties : list

	def __init__(self, proto:int,
		entityId:int=None,
		properties:list=None
	):
		super().__init__(proto,
			entityId=entityId,
			properties=properties
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 32,
		76 : 73
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'UUID', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ],
		76 : [ ( 'entityId', VarInt ), ( 'properties', ArrayType(StructType(( 'key', String ), ( 'value', Double ), ( 'modifiers', ArrayType(StructType(( 'UUID', UUID ), ( 'amount', Double ), ( 'operation', Byte ), ), VarInt, ) ), ), Int, ) ) ]
	}
