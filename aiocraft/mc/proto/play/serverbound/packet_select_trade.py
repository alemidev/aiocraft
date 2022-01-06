"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketSelectTrade(Packet):
	__slots__ = ( 'id', 'slot' )
	
	slot : int

	def __init__(self, proto:int,
		slot:int=None
	):
		super().__init__(proto,
			slot=slot
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		393 : 31,
		401 : 31,
		402 : 31,
		403 : 31,
		404 : 31,
		477 : 33,
		480 : 33,
		490 : 33,
		498 : 33,
		573 : 33,
		575 : 33,
		578 : 33,
		709 : 33,
		734 : 34,
		735 : 34,
		736 : 34,
		751 : 35,
		755 : 35,
		756 : 35,
		757 : 35
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'slot', VarInt ) ],
		401 : [ ( 'slot', VarInt ) ],
		402 : [ ( 'slot', VarInt ) ],
		403 : [ ( 'slot', VarInt ) ],
		404 : [ ( 'slot', VarInt ) ],
		477 : [ ( 'slot', VarInt ) ],
		480 : [ ( 'slot', VarInt ) ],
		490 : [ ( 'slot', VarInt ) ],
		498 : [ ( 'slot', VarInt ) ],
		573 : [ ( 'slot', VarInt ) ],
		575 : [ ( 'slot', VarInt ) ],
		578 : [ ( 'slot', VarInt ) ],
		709 : [ ( 'slot', VarInt ) ],
		734 : [ ( 'slot', VarInt ) ],
		735 : [ ( 'slot', VarInt ) ],
		736 : [ ( 'slot', VarInt ) ],
		751 : [ ( 'slot', VarInt ) ],
		755 : [ ( 'slot', VarInt ) ],
		756 : [ ( 'slot', VarInt ) ],
		757 : [ ( 'slot', VarInt ) ]
	}
