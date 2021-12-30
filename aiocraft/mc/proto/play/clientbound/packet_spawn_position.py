"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketSpawnPosition(Packet):
	__slots__ = ( 'id', 'angle', 'location' )
	
	angle : float
	location : Union[tuple,bytes]

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 5,
		47 : 5,
		76 : 66,
		107 : 67,
		108 : 67,
		109 : 67,
		110 : 67,
		201 : 67,
		210 : 67,
		304 : 67,
		315 : 67,
		321 : 69,
		327 : 69,
		331 : 69,
		335 : 69,
		338 : 70,
		340 : 70,
		351 : 71,
		393 : 73,
		401 : 73,
		402 : 73,
		403 : 73,
		404 : 73,
		477 : 77,
		480 : 77,
		490 : 77,
		498 : 77,
		573 : 78,
		575 : 78,
		578 : 78,
		709 : 67,
		734 : 66,
		735 : 66,
		736 : 66,
		751 : 66,
		755 : 75,
		756 : 75,
		757 : 75,
		1073741839 : 67
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
		755 : [ ( 'location', Position ), ( 'angle', Float ) ],
		756 : [ ( 'location', Position ), ( 'angle', Float ) ],
		757 : [ ( 'location', Position ), ( 'angle', Float ) ],
		1073741839 : [ ( 'location', Position ) ]
	}
