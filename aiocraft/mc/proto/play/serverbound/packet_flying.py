"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketFlying(Packet):
	__slots__ = ( 'id', 'onGround' )
	
	onGround : bool

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 3,
		47 : 3,
		76 : 14,
		107 : 15,
		108 : 15,
		109 : 15,
		110 : 15,
		201 : 15,
		210 : 15,
		304 : 15,
		315 : 15,
		321 : 16,
		327 : 16,
		331 : 16,
		335 : 13,
		338 : 12,
		340 : 12,
		351 : 12,
		393 : 15,
		401 : 15,
		402 : 15,
		403 : 15,
		404 : 15,
		477 : 20,
		480 : 20,
		490 : 20,
		498 : 20,
		573 : 20,
		575 : 20,
		578 : 20,
		709 : 20,
		734 : 21,
		735 : 21,
		736 : 21,
		751 : 21,
		755 : 20,
		756 : 20,
		757 : 20,
		1073741839 : 21
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'onGround', Boolean ) ],
		47 : [ ( 'onGround', Boolean ) ],
		76 : [ ( 'onGround', Boolean ) ],
		107 : [ ( 'onGround', Boolean ) ],
		108 : [ ( 'onGround', Boolean ) ],
		109 : [ ( 'onGround', Boolean ) ],
		110 : [ ( 'onGround', Boolean ) ],
		201 : [ ( 'onGround', Boolean ) ],
		210 : [ ( 'onGround', Boolean ) ],
		304 : [ ( 'onGround', Boolean ) ],
		315 : [ ( 'onGround', Boolean ) ],
		321 : [ ( 'onGround', Boolean ) ],
		327 : [ ( 'onGround', Boolean ) ],
		331 : [ ( 'onGround', Boolean ) ],
		335 : [ ( 'onGround', Boolean ) ],
		338 : [ ( 'onGround', Boolean ) ],
		340 : [ ( 'onGround', Boolean ) ],
		351 : [ ( 'onGround', Boolean ) ],
		393 : [ ( 'onGround', Boolean ) ],
		401 : [ ( 'onGround', Boolean ) ],
		402 : [ ( 'onGround', Boolean ) ],
		403 : [ ( 'onGround', Boolean ) ],
		404 : [ ( 'onGround', Boolean ) ],
		477 : [ ( 'onGround', Boolean ) ],
		480 : [ ( 'onGround', Boolean ) ],
		490 : [ ( 'onGround', Boolean ) ],
		498 : [ ( 'onGround', Boolean ) ],
		573 : [ ( 'onGround', Boolean ) ],
		575 : [ ( 'onGround', Boolean ) ],
		578 : [ ( 'onGround', Boolean ) ],
		709 : [ ( 'onGround', Boolean ) ],
		734 : [ ( 'onGround', Boolean ) ],
		735 : [ ( 'onGround', Boolean ) ],
		736 : [ ( 'onGround', Boolean ) ],
		751 : [ ( 'onGround', Boolean ) ],
		755 : [ ( 'onGround', Boolean ) ],
		756 : [ ( 'onGround', Boolean ) ],
		757 : [ ( 'onGround', Boolean ) ],
		1073741839 : [ ( 'onGround', Boolean ) ]
	}
