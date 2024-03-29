"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketEntity(Packet):
	__slots__ = ( 'id', 'entityId' )
	
	entityId : int

	def __init__(self, 
		entityId:int | None = None,
		**kwargs
	):
		super().__init__(
			entityId=entityId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 20,
		76 : 41,
		107 : 40,
		108 : 40,
		109 : 40,
		110 : 40,
		201 : 40,
		210 : 40,
		304 : 40,
		315 : 40,
		321 : 41,
		327 : 41,
		331 : 41,
		335 : 37,
		338 : 37,
		340 : 37,
		351 : 38,
		393 : 39,
		401 : 39,
		402 : 39,
		403 : 39,
		404 : 39,
		477 : 43,
		480 : 43,
		490 : 43,
		498 : 43,
		573 : 44,
		575 : 44,
		578 : 44,
		709 : 44,
		734 : 43,
		735 : 43,
		736 : 43,
		751 : 42
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', VarInt ) ],
		76 : [ ( 'entityId', VarInt ) ],
		107 : [ ( 'entityId', VarInt ) ],
		108 : [ ( 'entityId', VarInt ) ],
		109 : [ ( 'entityId', VarInt ) ],
		110 : [ ( 'entityId', VarInt ) ],
		201 : [ ( 'entityId', VarInt ) ],
		210 : [ ( 'entityId', VarInt ) ],
		304 : [ ( 'entityId', VarInt ) ],
		315 : [ ( 'entityId', VarInt ) ],
		321 : [ ( 'entityId', VarInt ) ],
		327 : [ ( 'entityId', VarInt ) ],
		331 : [ ( 'entityId', VarInt ) ],
		335 : [ ( 'entityId', VarInt ) ],
		338 : [ ( 'entityId', VarInt ) ],
		340 : [ ( 'entityId', VarInt ) ],
		351 : [ ( 'entityId', VarInt ) ],
		393 : [ ( 'entityId', VarInt ) ],
		401 : [ ( 'entityId', VarInt ) ],
		402 : [ ( 'entityId', VarInt ) ],
		403 : [ ( 'entityId', VarInt ) ],
		404 : [ ( 'entityId', VarInt ) ],
		477 : [ ( 'entityId', VarInt ) ],
		480 : [ ( 'entityId', VarInt ) ],
		490 : [ ( 'entityId', VarInt ) ],
		498 : [ ( 'entityId', VarInt ) ],
		573 : [ ( 'entityId', VarInt ) ],
		575 : [ ( 'entityId', VarInt ) ],
		578 : [ ( 'entityId', VarInt ) ],
		709 : [ ( 'entityId', VarInt ) ],
		734 : [ ( 'entityId', VarInt ) ],
		735 : [ ( 'entityId', VarInt ) ],
		736 : [ ( 'entityId', VarInt ) ],
		751 : [ ( 'entityId', VarInt ) ]
	}
