"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketCraftingBookData(Packet):
	__slots__ = ( 'id', 'type' )
	
	type : int

	def __init__(self, 
		type:int | None = None,
		**kwargs
	):
		super().__init__(
			type=type
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		321 : 23,
		327 : 23,
		331 : 23,
		335 : 23,
		338 : 23,
		340 : 23,
		351 : 23,
		393 : 27,
		401 : 27,
		402 : 27,
		403 : 27,
		404 : 27,
		477 : 29,
		480 : 29,
		490 : 29,
		498 : 29,
		573 : 29,
		575 : 29,
		578 : 29,
		709 : 29,
		734 : 30,
		735 : 30,
		736 : 30
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		321 : [ ( 'type', Int ) ],
		327 : [ ( 'type', Int ) ],
		331 : [ ( 'type', Int ) ],
		335 : [ ( 'type', VarInt ) ],
		338 : [ ( 'type', VarInt ) ],
		340 : [ ( 'type', VarInt ) ],
		351 : [ ( 'type', VarInt ) ],
		393 : [ ( 'type', VarInt ) ],
		401 : [ ( 'type', VarInt ) ],
		402 : [ ( 'type', VarInt ) ],
		403 : [ ( 'type', VarInt ) ],
		404 : [ ( 'type', VarInt ) ],
		477 : [ ( 'type', VarInt ) ],
		480 : [ ( 'type', VarInt ) ],
		490 : [ ( 'type', VarInt ) ],
		498 : [ ( 'type', VarInt ) ],
		573 : [ ( 'type', VarInt ) ],
		575 : [ ( 'type', VarInt ) ],
		578 : [ ( 'type', VarInt ) ],
		709 : [ ( 'type', VarInt ) ],
		734 : [ ( 'type', VarInt ) ],
		735 : [ ( 'type', VarInt ) ],
		736 : [ ( 'type', VarInt ) ]
	}
