"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketClientCommand(Packet):
	__slots__ = ( 'id', 'actionId', 'payload' )
	
	actionId : int
	payload : int

	def __init__(self, 
		actionId:int | None = None,
		payload:int | None = None,
		**kwargs
	):
		super().__init__(
			actionId=actionId,
			payload=payload
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 22,
		76 : 2,
		107 : 3,
		108 : 3,
		109 : 3,
		110 : 3,
		201 : 3,
		210 : 3,
		304 : 3,
		315 : 3,
		321 : 4,
		327 : 4,
		331 : 4,
		335 : 4,
		338 : 3,
		340 : 3,
		351 : 2,
		393 : 3,
		401 : 3,
		402 : 3,
		403 : 3,
		404 : 3,
		477 : 4,
		480 : 4,
		490 : 4,
		498 : 4,
		573 : 4,
		575 : 4,
		578 : 4,
		709 : 4,
		734 : 4,
		735 : 4,
		736 : 4,
		751 : 4,
		755 : 4,
		756 : 4,
		757 : 4,
		758 : 4,
		759 : 6,
		760 : 7,
		761 : 6
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'payload', VarInt ) ],
		76 : [ ( 'payload', VarInt ) ],
		107 : [ ( 'actionId', VarInt ) ],
		108 : [ ( 'actionId', VarInt ) ],
		109 : [ ( 'actionId', VarInt ) ],
		110 : [ ( 'actionId', VarInt ) ],
		201 : [ ( 'actionId', VarInt ) ],
		210 : [ ( 'actionId', VarInt ) ],
		304 : [ ( 'actionId', VarInt ) ],
		315 : [ ( 'actionId', VarInt ) ],
		321 : [ ( 'actionId', VarInt ) ],
		327 : [ ( 'actionId', VarInt ) ],
		331 : [ ( 'actionId', VarInt ) ],
		335 : [ ( 'actionId', VarInt ) ],
		338 : [ ( 'actionId', VarInt ) ],
		340 : [ ( 'actionId', VarInt ) ],
		351 : [ ( 'actionId', VarInt ) ],
		393 : [ ( 'actionId', VarInt ) ],
		401 : [ ( 'actionId', VarInt ) ],
		402 : [ ( 'actionId', VarInt ) ],
		403 : [ ( 'actionId', VarInt ) ],
		404 : [ ( 'actionId', VarInt ) ],
		477 : [ ( 'actionId', VarInt ) ],
		480 : [ ( 'actionId', VarInt ) ],
		490 : [ ( 'actionId', VarInt ) ],
		498 : [ ( 'actionId', VarInt ) ],
		573 : [ ( 'actionId', VarInt ) ],
		575 : [ ( 'actionId', VarInt ) ],
		578 : [ ( 'actionId', VarInt ) ],
		709 : [ ( 'actionId', VarInt ) ],
		734 : [ ( 'actionId', VarInt ) ],
		735 : [ ( 'actionId', VarInt ) ],
		736 : [ ( 'actionId', VarInt ) ],
		751 : [ ( 'actionId', VarInt ) ],
		755 : [ ( 'actionId', VarInt ) ],
		756 : [ ( 'actionId', VarInt ) ],
		757 : [ ( 'actionId', VarInt ) ],
		758 : [ ( 'actionId', VarInt ) ],
		759 : [ ( 'actionId', VarInt ) ],
		760 : [ ( 'actionId', VarInt ) ],
		761 : [ ( 'actionId', VarInt ) ]
	}
