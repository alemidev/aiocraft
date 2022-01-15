"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketLegacyServerListPing(Packet):
	__slots__ = ( 'id', 'payload' )
	
	payload : int

	def __init__(self, proto:int,
		payload:int=None,
		**kwargs
	):
		super().__init__(proto,
			payload=payload
		)

	_state : int = 0

	_ids : Dict[int, int] = {
		47 : 254,
		76 : 254,
		107 : 254,
		108 : 254,
		109 : 254,
		110 : 254,
		201 : 254,
		210 : 254,
		304 : 254,
		315 : 254,
		321 : 254,
		327 : 254,
		331 : 254,
		335 : 254,
		338 : 254,
		340 : 254,
		351 : 254,
		393 : 254,
		401 : 254,
		402 : 254,
		403 : 254,
		404 : 254,
		477 : 254,
		480 : 254,
		490 : 254,
		498 : 254,
		573 : 254,
		575 : 254,
		578 : 254,
		709 : 254,
		734 : 254,
		735 : 254,
		736 : 254,
		751 : 254,
		755 : 254,
		756 : 254,
		757 : 254
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'payload', Byte ) ],
		76 : [ ( 'payload', Byte ) ],
		107 : [ ( 'payload', Byte ) ],
		108 : [ ( 'payload', Byte ) ],
		109 : [ ( 'payload', Byte ) ],
		110 : [ ( 'payload', Byte ) ],
		201 : [ ( 'payload', Byte ) ],
		210 : [ ( 'payload', Byte ) ],
		304 : [ ( 'payload', Byte ) ],
		315 : [ ( 'payload', Byte ) ],
		321 : [ ( 'payload', Byte ) ],
		327 : [ ( 'payload', Byte ) ],
		331 : [ ( 'payload', Byte ) ],
		335 : [ ( 'payload', Byte ) ],
		338 : [ ( 'payload', Byte ) ],
		340 : [ ( 'payload', Byte ) ],
		351 : [ ( 'payload', Byte ) ],
		393 : [ ( 'payload', Byte ) ],
		401 : [ ( 'payload', Byte ) ],
		402 : [ ( 'payload', Byte ) ],
		403 : [ ( 'payload', Byte ) ],
		404 : [ ( 'payload', Byte ) ],
		477 : [ ( 'payload', Byte ) ],
		480 : [ ( 'payload', Byte ) ],
		490 : [ ( 'payload', Byte ) ],
		498 : [ ( 'payload', Byte ) ],
		573 : [ ( 'payload', Byte ) ],
		575 : [ ( 'payload', Byte ) ],
		578 : [ ( 'payload', Byte ) ],
		709 : [ ( 'payload', Byte ) ],
		734 : [ ( 'payload', Byte ) ],
		735 : [ ( 'payload', Byte ) ],
		736 : [ ( 'payload', Byte ) ],
		751 : [ ( 'payload', Byte ) ],
		755 : [ ( 'payload', Byte ) ],
		756 : [ ( 'payload', Byte ) ],
		757 : [ ( 'payload', Byte ) ]
	}
