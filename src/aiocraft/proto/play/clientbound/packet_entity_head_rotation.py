"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketEntityHeadRotation(Packet):
	__slots__ = ( 'id', 'entityId', 'headYaw' )
	
	entityId : int
	headYaw : int

	def __init__(self, 
		entityId:int | None = None,
		headYaw:int | None = None,
		**kwargs
	):
		super().__init__(
			entityId=entityId,
			headYaw=headYaw
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 25,
		76 : 52,
		107 : 52,
		108 : 52,
		109 : 52,
		110 : 52,
		201 : 52,
		210 : 52,
		304 : 52,
		315 : 52,
		321 : 54,
		327 : 54,
		331 : 54,
		335 : 53,
		338 : 54,
		340 : 54,
		351 : 55,
		393 : 57,
		401 : 57,
		402 : 57,
		403 : 57,
		404 : 57,
		477 : 59,
		480 : 59,
		490 : 59,
		498 : 59,
		573 : 60,
		575 : 60,
		578 : 60,
		709 : 60,
		734 : 59,
		735 : 59,
		736 : 59,
		751 : 58,
		755 : 62,
		756 : 62,
		757 : 62,
		758 : 62,
		759 : 60,
		760 : 63,
		761 : 62
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		76 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		107 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		108 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		109 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		110 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		201 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		210 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		304 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		315 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		321 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		327 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		331 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		335 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		338 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		340 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		351 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		393 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		401 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		402 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		403 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		404 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		477 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		480 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		490 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		498 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		573 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		575 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		578 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		709 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		734 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		735 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		736 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		751 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		755 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		756 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		757 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		758 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		759 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		760 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ],
		761 : [ ( 'entityId', VarInt ), ( 'headYaw', Byte ) ]
	}
