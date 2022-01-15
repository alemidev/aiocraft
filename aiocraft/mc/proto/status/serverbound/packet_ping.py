"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketPing(Packet):
	__slots__ = ( 'id', 'time' )
	
	time : int

	def __init__(self, proto:int,
		time:int=None,
		**kwargs
	):
		super().__init__(proto,
			time=time
		)

	_state : int = 1

	_ids : Dict[int, int] = {
		47 : 1,
		76 : 1,
		107 : 1,
		108 : 1,
		109 : 1,
		110 : 1,
		201 : 1,
		210 : 1,
		304 : 1,
		315 : 1,
		321 : 1,
		327 : 1,
		331 : 1,
		335 : 1,
		338 : 1,
		340 : 1,
		351 : 1,
		393 : 1,
		401 : 1,
		402 : 1,
		403 : 1,
		404 : 1,
		477 : 1,
		480 : 1,
		490 : 1,
		498 : 1,
		573 : 1,
		575 : 1,
		578 : 1,
		709 : 1,
		734 : 1,
		735 : 1,
		736 : 1,
		751 : 1,
		755 : 1,
		756 : 1,
		757 : 1
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'time', Long ) ],
		76 : [ ( 'time', Long ) ],
		107 : [ ( 'time', Long ) ],
		108 : [ ( 'time', Long ) ],
		109 : [ ( 'time', Long ) ],
		110 : [ ( 'time', Long ) ],
		201 : [ ( 'time', Long ) ],
		210 : [ ( 'time', Long ) ],
		304 : [ ( 'time', Long ) ],
		315 : [ ( 'time', Long ) ],
		321 : [ ( 'time', Long ) ],
		327 : [ ( 'time', Long ) ],
		331 : [ ( 'time', Long ) ],
		335 : [ ( 'time', Long ) ],
		338 : [ ( 'time', Long ) ],
		340 : [ ( 'time', Long ) ],
		351 : [ ( 'time', Long ) ],
		393 : [ ( 'time', Long ) ],
		401 : [ ( 'time', Long ) ],
		402 : [ ( 'time', Long ) ],
		403 : [ ( 'time', Long ) ],
		404 : [ ( 'time', Long ) ],
		477 : [ ( 'time', Long ) ],
		480 : [ ( 'time', Long ) ],
		490 : [ ( 'time', Long ) ],
		498 : [ ( 'time', Long ) ],
		573 : [ ( 'time', Long ) ],
		575 : [ ( 'time', Long ) ],
		578 : [ ( 'time', Long ) ],
		709 : [ ( 'time', Long ) ],
		734 : [ ( 'time', Long ) ],
		735 : [ ( 'time', Long ) ],
		736 : [ ( 'time', Long ) ],
		751 : [ ( 'time', Long ) ],
		755 : [ ( 'time', Long ) ],
		756 : [ ( 'time', Long ) ],
		757 : [ ( 'time', Long ) ]
	}
