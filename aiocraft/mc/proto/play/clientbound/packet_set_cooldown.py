"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketSetCooldown(Packet):
	__slots__ = ( 'id', 'cooldownTicks', 'itemID' )
	
	cooldownTicks : int
	itemID : int

	def __init__(self, proto:int,
		cooldownTicks:int=None,
		itemID:int=None,
		**kwargs
	):
		super().__init__(proto,
			cooldownTicks=cooldownTicks,
			itemID=itemID
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		76 : 23,
		107 : 23,
		108 : 23,
		109 : 23,
		110 : 23,
		201 : 23,
		210 : 23,
		304 : 23,
		315 : 23,
		321 : 24,
		327 : 24,
		331 : 24,
		335 : 23,
		338 : 23,
		340 : 23,
		351 : 24,
		393 : 24,
		401 : 24,
		402 : 24,
		403 : 24,
		404 : 24,
		477 : 23,
		480 : 23,
		490 : 23,
		498 : 23,
		573 : 24,
		575 : 24,
		578 : 24,
		709 : 24,
		734 : 23,
		735 : 23,
		736 : 23,
		751 : 22,
		755 : 23,
		756 : 23,
		757 : 23
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		76 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		107 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		108 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		109 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		110 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		201 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		210 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		304 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		315 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		321 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		327 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		331 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		335 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		338 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		340 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		351 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		393 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		401 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		402 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		403 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		404 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		477 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		480 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		490 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		498 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		573 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		575 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		578 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		709 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		734 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		735 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		736 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		751 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		755 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		756 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ],
		757 : [ ( 'itemID', VarInt ), ( 'cooldownTicks', VarInt ) ]
	}
