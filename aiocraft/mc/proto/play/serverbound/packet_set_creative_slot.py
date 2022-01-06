"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketSetCreativeSlot(Packet):
	__slots__ = ( 'id', 'item', 'slot' )
	
	item : dict
	slot : int

	def __init__(self, proto:int,
		item:dict=None,
		slot:int=None
	):
		super().__init__(proto,
			item=item,
			slot=slot
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 16,
		76 : 21,
		107 : 24,
		108 : 24,
		109 : 24,
		110 : 24,
		201 : 24,
		210 : 24,
		304 : 24,
		315 : 24,
		321 : 26,
		327 : 26,
		331 : 26,
		335 : 27,
		338 : 27,
		340 : 27,
		351 : 27,
		393 : 36,
		401 : 36,
		402 : 36,
		403 : 36,
		404 : 36,
		477 : 38,
		480 : 38,
		490 : 38,
		498 : 38,
		573 : 38,
		575 : 38,
		578 : 38,
		709 : 38,
		734 : 39,
		735 : 39,
		736 : 39,
		751 : 40,
		755 : 40,
		756 : 40,
		757 : 40
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		76 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		107 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		108 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		109 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		110 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		201 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		210 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		304 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		315 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		321 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		327 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		331 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		335 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		338 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		340 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		351 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		393 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		401 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		402 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		403 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		404 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		477 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		480 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		490 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		498 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		573 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		575 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		578 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		709 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		734 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		735 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		736 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		751 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		755 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		756 : [ ( 'slot', Short ), ( 'item', Slot ) ],
		757 : [ ( 'slot', Short ), ( 'item', Slot ) ]
	}
