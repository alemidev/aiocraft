"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketWorldEvent(Packet):
	__slots__ = ( 'id', 'data', 'effectId', 'is_global', 'location' )
	
	data : int
	effectId : int
	is_global : bool
	location : tuple

	def __init__(self, 
		data:int | None = None,
		effectId:int | None = None,
		is_global:bool | None = None,
		location:tuple | None = None,
		**kwargs
	):
		super().__init__(
			data=data,
			effectId=effectId,
			is_global=is_global,
			location=location
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 40,
		76 : 33,
		107 : 33,
		108 : 33,
		109 : 33,
		110 : 33,
		201 : 33,
		210 : 33,
		304 : 33,
		315 : 33,
		321 : 34,
		327 : 34,
		331 : 34,
		335 : 33,
		338 : 33,
		340 : 33,
		351 : 34,
		393 : 35,
		401 : 35,
		402 : 35,
		403 : 35,
		404 : 35,
		477 : 34,
		480 : 34,
		490 : 34,
		498 : 34,
		573 : 35,
		575 : 35,
		578 : 35,
		709 : 35,
		734 : 34,
		735 : 34,
		736 : 34,
		751 : 33,
		755 : 35,
		756 : 35,
		757 : 35,
		758 : 35,
		759 : 32,
		760 : 34,
		761 : 33
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		76 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		107 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		108 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		109 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		110 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		201 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		210 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		304 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		315 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		321 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		327 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		331 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		335 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		338 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		340 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		351 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		393 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		401 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		402 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		403 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		404 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		477 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		480 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		490 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		498 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		573 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		575 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		578 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		709 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		734 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		735 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		736 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		751 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		755 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		756 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		757 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		758 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		759 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		760 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ],
		761 : [ ( 'effectId', Int ), ( 'location', Position ), ( 'data', Int ), ( 'is_global', Boolean ) ]
	}
