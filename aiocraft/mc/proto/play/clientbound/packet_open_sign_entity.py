"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketOpenSignEntity(Packet):
	__slots__ = ( 'id', 'location' )
	
	location : Union[bytes,tuple]

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 54,
		47 : 54,
		76 : 42,
		107 : 42,
		108 : 42,
		109 : 42,
		110 : 42,
		201 : 42,
		210 : 42,
		304 : 42,
		315 : 42,
		321 : 43,
		327 : 43,
		331 : 43,
		335 : 42,
		338 : 42,
		340 : 42,
		351 : 43,
		393 : 44,
		401 : 44,
		402 : 44,
		403 : 44,
		404 : 44,
		477 : 47,
		480 : 47,
		490 : 47,
		498 : 47,
		573 : 48,
		575 : 48,
		578 : 48,
		709 : 48,
		734 : 47,
		735 : 47,
		736 : 47,
		751 : 46,
		755 : 47,
		756 : 47,
		757 : 47,
		1073741839 : 47
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'location', TrailingData ) ],
		47 : [ ( 'location', Position ) ],
		76 : [ ( 'location', Position ) ],
		107 : [ ( 'location', Position ) ],
		108 : [ ( 'location', Position ) ],
		109 : [ ( 'location', Position ) ],
		110 : [ ( 'location', Position ) ],
		201 : [ ( 'location', Position ) ],
		210 : [ ( 'location', Position ) ],
		304 : [ ( 'location', Position ) ],
		315 : [ ( 'location', Position ) ],
		321 : [ ( 'location', Position ) ],
		327 : [ ( 'location', Position ) ],
		331 : [ ( 'location', Position ) ],
		335 : [ ( 'location', Position ) ],
		338 : [ ( 'location', Position ) ],
		340 : [ ( 'location', Position ) ],
		351 : [ ( 'location', Position ) ],
		393 : [ ( 'location', Position ) ],
		401 : [ ( 'location', Position ) ],
		402 : [ ( 'location', Position ) ],
		403 : [ ( 'location', Position ) ],
		404 : [ ( 'location', Position ) ],
		477 : [ ( 'location', Position ) ],
		480 : [ ( 'location', Position ) ],
		490 : [ ( 'location', Position ) ],
		498 : [ ( 'location', Position ) ],
		573 : [ ( 'location', Position ) ],
		575 : [ ( 'location', Position ) ],
		578 : [ ( 'location', Position ) ],
		709 : [ ( 'location', Position ) ],
		734 : [ ( 'location', Position ) ],
		735 : [ ( 'location', Position ) ],
		736 : [ ( 'location', Position ) ],
		751 : [ ( 'location', Position ) ],
		755 : [ ( 'location', Position ) ],
		756 : [ ( 'location', Position ) ],
		757 : [ ( 'location', Position ) ],
		1073741839 : [ ( 'location', Position ) ]
	}
