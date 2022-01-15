"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketBlockBreakAnimation(Packet):
	__slots__ = ( 'id', 'destroyStage', 'entityId', 'location' )
	
	destroyStage : int
	entityId : int
	location : tuple

	def __init__(self, proto:int,
		destroyStage:int=None,
		entityId:int=None,
		location:tuple=None,
		**kwargs
	):
		super().__init__(proto,
			destroyStage=destroyStage,
			entityId=entityId,
			location=location
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 37,
		76 : 8,
		107 : 8,
		108 : 8,
		109 : 8,
		110 : 8,
		201 : 8,
		210 : 8,
		304 : 8,
		315 : 8,
		321 : 9,
		327 : 9,
		331 : 9,
		335 : 8,
		338 : 8,
		340 : 8,
		351 : 8,
		393 : 8,
		401 : 8,
		402 : 8,
		403 : 8,
		404 : 8,
		477 : 8,
		480 : 8,
		490 : 8,
		498 : 8,
		573 : 9,
		575 : 9,
		578 : 9,
		709 : 9,
		734 : 8,
		735 : 8,
		736 : 8,
		751 : 8,
		755 : 9,
		756 : 9,
		757 : 9
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		76 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		107 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		108 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		109 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		110 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		201 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		210 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		304 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		315 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		321 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		327 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		331 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		335 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		338 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		340 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		351 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		393 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		401 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		402 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		403 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		404 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		477 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		480 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		490 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		498 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		573 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		575 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		578 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		709 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		734 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		735 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		736 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		751 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		755 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		756 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ],
		757 : [ ( 'entityId', VarInt ), ( 'location', Position ), ( 'destroyStage', Byte ) ]
	}
