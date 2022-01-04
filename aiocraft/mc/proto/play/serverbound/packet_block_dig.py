"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketBlockDig(Packet):
	__slots__ = ( 'id', 'location', 'status', 'face' )
	
	location : Union[bytes,tuple]
	status : int
	face : int

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 7,
		47 : 7,
		76 : 16,
		107 : 19,
		108 : 19,
		109 : 19,
		110 : 19,
		201 : 19,
		210 : 19,
		304 : 19,
		315 : 19,
		321 : 20,
		327 : 20,
		331 : 20,
		335 : 20,
		338 : 20,
		340 : 20,
		351 : 20,
		393 : 24,
		401 : 24,
		402 : 24,
		403 : 24,
		404 : 24,
		477 : 26,
		480 : 26,
		490 : 26,
		498 : 26,
		573 : 26,
		575 : 26,
		578 : 26,
		709 : 26,
		734 : 27,
		735 : 27,
		736 : 27,
		751 : 27,
		755 : 26,
		756 : 26,
		757 : 26,
		1073741839 : 27
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'status', Byte ), ( 'location', TrailingData ), ( 'face', Byte ) ],
		47 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		76 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		107 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		108 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		109 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		110 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		201 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		210 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		304 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		315 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		321 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		327 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		331 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		335 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		338 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		340 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		351 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		393 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		401 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		402 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		403 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		404 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		477 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		480 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		490 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		498 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		573 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		575 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		578 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		709 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		734 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		735 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		736 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		751 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		755 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		756 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		757 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ],
		1073741839 : [ ( 'status', Byte ), ( 'location', Position ), ( 'face', Byte ) ]
	}
