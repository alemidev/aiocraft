"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketAnimation(Packet):
	__slots__ = ( 'id', 'animation', 'entityId' )
	
	animation : int
	entityId : int

	def __init__(self, 
		animation:int | None = None,
		entityId:int | None = None,
		**kwargs
	):
		super().__init__(
			animation=animation,
			entityId=entityId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 11,
		76 : 6,
		107 : 6,
		108 : 6,
		109 : 6,
		110 : 6,
		201 : 6,
		210 : 6,
		304 : 6,
		315 : 6,
		321 : 6,
		327 : 6,
		331 : 6,
		335 : 6,
		338 : 6,
		340 : 6,
		351 : 6,
		393 : 6,
		401 : 6,
		402 : 6,
		403 : 6,
		404 : 6,
		477 : 6,
		480 : 6,
		490 : 6,
		498 : 6,
		573 : 6,
		575 : 6,
		578 : 6,
		709 : 6,
		734 : 5,
		735 : 5,
		736 : 5,
		751 : 5,
		755 : 6,
		756 : 6,
		757 : 6,
		758 : 6,
		759 : 3,
		760 : 3,
		761 : 3
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		76 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		107 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		108 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		109 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		110 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		201 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		210 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		304 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		315 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		321 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		327 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		331 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		335 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		338 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		340 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		351 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		393 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		401 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		402 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		403 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		404 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		477 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		480 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		490 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		498 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		573 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		575 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		578 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		709 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		734 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		735 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		736 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		751 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		755 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		756 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		757 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		758 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		759 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		760 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ],
		761 : [ ( 'entityId', VarInt ), ( 'animation', Byte ) ]
	}
