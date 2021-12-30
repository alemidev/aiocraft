"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketUpdateHealth(Packet):
	__slots__ = ( 'id', 'health', 'foodSaturation', 'food' )
	
	health : float
	foodSaturation : float
	food : int

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 6,
		47 : 6,
		76 : 62,
		107 : 62,
		108 : 62,
		109 : 62,
		110 : 62,
		201 : 62,
		210 : 62,
		304 : 62,
		315 : 62,
		321 : 64,
		327 : 64,
		331 : 64,
		335 : 64,
		338 : 65,
		340 : 65,
		351 : 66,
		393 : 68,
		401 : 68,
		402 : 68,
		403 : 68,
		404 : 68,
		477 : 72,
		480 : 72,
		490 : 72,
		498 : 72,
		573 : 73,
		575 : 73,
		578 : 73,
		709 : 74,
		734 : 73,
		735 : 73,
		736 : 73,
		751 : 73,
		755 : 82,
		756 : 82,
		757 : 82,
		1073741839 : 74
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'health', Float ), ( 'food', Short ), ( 'foodSaturation', Float ) ],
		47 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		76 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		107 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		108 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		109 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		110 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		201 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		210 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		304 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		315 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		321 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		327 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		331 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		335 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		338 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		340 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		351 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		393 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		401 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		402 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		403 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		404 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		477 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		480 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		490 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		498 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		573 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		575 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		578 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		709 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		734 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		735 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		736 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		751 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		755 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		756 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		757 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ],
		1073741839 : [ ( 'health', Float ), ( 'food', VarInt ), ( 'foodSaturation', Float ) ]
	}
