"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketEntityAction(Packet):
	__slots__ = ( 'id', 'actionId', 'entityId', 'jumpBoost' )
	
	actionId : int
	entityId : int
	jumpBoost : int

	def __init__(self, proto:int,
		actionId:int=None,
		entityId:int=None,
		jumpBoost:int=None,
		**kwargs
	):
		super().__init__(proto,
			actionId=actionId,
			entityId=entityId,
			jumpBoost=jumpBoost
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 11,
		76 : 17,
		107 : 20,
		108 : 20,
		109 : 20,
		110 : 20,
		201 : 20,
		210 : 20,
		304 : 20,
		315 : 20,
		321 : 21,
		327 : 21,
		331 : 21,
		335 : 21,
		338 : 21,
		340 : 21,
		351 : 21,
		393 : 25,
		401 : 25,
		402 : 25,
		403 : 25,
		404 : 25,
		477 : 27,
		480 : 27,
		490 : 27,
		498 : 27,
		573 : 27,
		575 : 27,
		578 : 27,
		709 : 27,
		734 : 28,
		735 : 28,
		736 : 28,
		751 : 28,
		755 : 27,
		756 : 27,
		757 : 27
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		76 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		107 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		108 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		109 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		110 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		201 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		210 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		304 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		315 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		321 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		327 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		331 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		335 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		338 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		340 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		351 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		393 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		401 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		402 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		403 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		404 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		477 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		480 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		490 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		498 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		573 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		575 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		578 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		709 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		734 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		735 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		736 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		751 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		755 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		756 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ],
		757 : [ ( 'entityId', VarInt ), ( 'actionId', VarInt ), ( 'jumpBoost', VarInt ) ]
	}
