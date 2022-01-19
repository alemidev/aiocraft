"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketTransaction(Packet):
	__slots__ = ( 'id', 'accepted', 'action', 'windowId' )
	
	accepted : bool
	action : int
	windowId : int

	def __init__(self, proto:int,
		accepted:bool=None,
		action:int=None,
		windowId:int=None,
		**kwargs
	):
		super().__init__(proto,
			accepted=accepted,
			action=action,
			windowId=windowId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 15,
		76 : 4,
		107 : 5,
		108 : 5,
		109 : 5,
		110 : 5,
		201 : 5,
		210 : 5,
		304 : 5,
		315 : 5,
		321 : 6,
		327 : 6,
		331 : 6,
		335 : 6,
		338 : 5,
		340 : 5,
		351 : 5,
		393 : 6,
		401 : 6,
		402 : 6,
		403 : 6,
		404 : 6,
		477 : 7,
		480 : 7,
		490 : 7,
		498 : 7,
		573 : 7,
		575 : 7,
		578 : 7,
		709 : 7,
		734 : 7,
		735 : 7,
		736 : 7,
		751 : 7
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		76 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		107 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		108 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		109 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		110 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		201 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		210 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		304 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		315 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		321 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		327 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		331 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		335 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		338 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		340 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		351 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		393 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		401 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		402 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		403 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		404 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		477 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		480 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		490 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		498 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		573 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		575 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		578 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		709 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		734 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		735 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		736 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ],
		751 : [ ( 'windowId', Byte ), ( 'action', Short ), ( 'accepted', Boolean ) ]
	}
