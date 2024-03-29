"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketCustomPayload(Packet):
	__slots__ = ( 'id', 'channel', 'data' )
	
	channel : str
	data : bytes

	def __init__(self, 
		channel:str | None = None,
		data:bytes | None = None,
		**kwargs
	):
		super().__init__(
			channel=channel,
			data=data
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 23,
		76 : 8,
		107 : 9,
		108 : 9,
		109 : 9,
		110 : 9,
		201 : 9,
		210 : 9,
		304 : 9,
		315 : 9,
		321 : 10,
		327 : 10,
		331 : 10,
		335 : 10,
		338 : 9,
		340 : 9,
		351 : 9,
		393 : 10,
		401 : 10,
		402 : 10,
		403 : 10,
		404 : 10,
		477 : 11,
		480 : 11,
		490 : 11,
		498 : 11,
		573 : 11,
		575 : 11,
		578 : 11,
		709 : 11,
		734 : 11,
		735 : 11,
		736 : 11,
		751 : 11,
		755 : 10,
		756 : 10,
		757 : 10,
		758 : 10,
		759 : 12,
		760 : 13,
		761 : 12
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		76 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		107 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		108 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		109 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		110 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		201 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		210 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		304 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		315 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		321 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		327 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		331 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		335 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		338 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		340 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		351 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		393 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		401 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		402 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		403 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		404 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		477 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		480 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		490 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		498 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		573 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		575 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		578 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		709 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		734 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		735 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		736 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		751 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		755 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		756 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		757 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		758 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		759 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		760 : [ ( 'channel', String ), ( 'data', TrailingData ) ],
		761 : [ ( 'channel', String ), ( 'data', TrailingData ) ]
	}
