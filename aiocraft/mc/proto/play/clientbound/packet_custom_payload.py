"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketCustomPayload(Packet):
	__slots__ = ( 'id', 'channel', 'data' )
	
	channel : str
	data : bytes

	def __init__(self, proto:int,
		channel:str=None,
		data:bytes=None,
		**kwargs
	):
		super().__init__(proto,
			channel=channel,
			data=data
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 63,
		76 : 24,
		107 : 24,
		108 : 24,
		109 : 24,
		110 : 24,
		201 : 24,
		210 : 24,
		304 : 24,
		315 : 24,
		321 : 25,
		327 : 25,
		331 : 25,
		335 : 24,
		338 : 24,
		340 : 24,
		351 : 25,
		393 : 25,
		401 : 25,
		402 : 25,
		403 : 25,
		404 : 25,
		477 : 24,
		480 : 24,
		490 : 24,
		498 : 24,
		573 : 25,
		575 : 25,
		578 : 25,
		709 : 25,
		734 : 24,
		735 : 24,
		736 : 24,
		751 : 23,
		755 : 24,
		756 : 24,
		757 : 24
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
		757 : [ ( 'channel', String ), ( 'data', TrailingData ) ]
	}
