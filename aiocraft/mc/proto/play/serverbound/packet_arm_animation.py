"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketArmAnimation(Packet):
	__slots__ = ( 'id', 'hand' )
	
	hand : int

	def __init__(self, proto:int,
		hand:int=None,
		**kwargs
	):
		super().__init__(proto,
			hand=hand
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 10,
		76 : 23,
		107 : 26,
		108 : 26,
		109 : 26,
		110 : 26,
		201 : 26,
		210 : 26,
		304 : 26,
		315 : 26,
		321 : 28,
		327 : 28,
		331 : 28,
		335 : 29,
		338 : 29,
		340 : 29,
		351 : 29,
		393 : 39,
		401 : 39,
		402 : 39,
		403 : 39,
		404 : 39,
		477 : 42,
		480 : 42,
		490 : 42,
		498 : 42,
		573 : 42,
		575 : 42,
		578 : 42,
		709 : 42,
		734 : 43,
		735 : 43,
		736 : 43,
		751 : 44,
		755 : 44,
		756 : 44,
		757 : 44
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [  ],
		76 : [ ( 'hand', VarInt ) ],
		107 : [ ( 'hand', VarInt ) ],
		108 : [ ( 'hand', VarInt ) ],
		109 : [ ( 'hand', VarInt ) ],
		110 : [ ( 'hand', VarInt ) ],
		201 : [ ( 'hand', VarInt ) ],
		210 : [ ( 'hand', VarInt ) ],
		304 : [ ( 'hand', VarInt ) ],
		315 : [ ( 'hand', VarInt ) ],
		321 : [ ( 'hand', VarInt ) ],
		327 : [ ( 'hand', VarInt ) ],
		331 : [ ( 'hand', VarInt ) ],
		335 : [ ( 'hand', VarInt ) ],
		338 : [ ( 'hand', VarInt ) ],
		340 : [ ( 'hand', VarInt ) ],
		351 : [ ( 'hand', VarInt ) ],
		393 : [ ( 'hand', VarInt ) ],
		401 : [ ( 'hand', VarInt ) ],
		402 : [ ( 'hand', VarInt ) ],
		403 : [ ( 'hand', VarInt ) ],
		404 : [ ( 'hand', VarInt ) ],
		477 : [ ( 'hand', VarInt ) ],
		480 : [ ( 'hand', VarInt ) ],
		490 : [ ( 'hand', VarInt ) ],
		498 : [ ( 'hand', VarInt ) ],
		573 : [ ( 'hand', VarInt ) ],
		575 : [ ( 'hand', VarInt ) ],
		578 : [ ( 'hand', VarInt ) ],
		709 : [ ( 'hand', VarInt ) ],
		734 : [ ( 'hand', VarInt ) ],
		735 : [ ( 'hand', VarInt ) ],
		736 : [ ( 'hand', VarInt ) ],
		751 : [ ( 'hand', VarInt ) ],
		755 : [ ( 'hand', VarInt ) ],
		756 : [ ( 'hand', VarInt ) ],
		757 : [ ( 'hand', VarInt ) ]
	}
