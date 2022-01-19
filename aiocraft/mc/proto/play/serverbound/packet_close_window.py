"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketCloseWindow(Packet):
	__slots__ = ( 'id', 'windowId' )
	
	windowId : int

	def __init__(self, proto:int,
		windowId:int=None,
		**kwargs
	):
		super().__init__(proto,
			windowId=windowId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 13,
		76 : 7,
		107 : 8,
		108 : 8,
		109 : 8,
		110 : 8,
		201 : 8,
		210 : 8,
		304 : 8,
		315 : 8,
		321 : 9,
		327 : 9,
		331 : 9,
		335 : 9,
		338 : 8,
		340 : 8,
		351 : 8,
		393 : 9,
		401 : 9,
		402 : 9,
		403 : 9,
		404 : 9,
		477 : 10,
		480 : 10,
		490 : 10,
		498 : 10,
		573 : 10,
		575 : 10,
		578 : 10,
		709 : 10,
		734 : 10,
		735 : 10,
		736 : 10,
		751 : 10,
		755 : 9,
		756 : 9,
		757 : 9
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'windowId', Byte ) ],
		76 : [ ( 'windowId', Byte ) ],
		107 : [ ( 'windowId', Byte ) ],
		108 : [ ( 'windowId', Byte ) ],
		109 : [ ( 'windowId', Byte ) ],
		110 : [ ( 'windowId', Byte ) ],
		201 : [ ( 'windowId', Byte ) ],
		210 : [ ( 'windowId', Byte ) ],
		304 : [ ( 'windowId', Byte ) ],
		315 : [ ( 'windowId', Byte ) ],
		321 : [ ( 'windowId', Byte ) ],
		327 : [ ( 'windowId', Byte ) ],
		331 : [ ( 'windowId', Byte ) ],
		335 : [ ( 'windowId', Byte ) ],
		338 : [ ( 'windowId', Byte ) ],
		340 : [ ( 'windowId', Byte ) ],
		351 : [ ( 'windowId', Byte ) ],
		393 : [ ( 'windowId', Byte ) ],
		401 : [ ( 'windowId', Byte ) ],
		402 : [ ( 'windowId', Byte ) ],
		403 : [ ( 'windowId', Byte ) ],
		404 : [ ( 'windowId', Byte ) ],
		477 : [ ( 'windowId', Byte ) ],
		480 : [ ( 'windowId', Byte ) ],
		490 : [ ( 'windowId', Byte ) ],
		498 : [ ( 'windowId', Byte ) ],
		573 : [ ( 'windowId', Byte ) ],
		575 : [ ( 'windowId', Byte ) ],
		578 : [ ( 'windowId', Byte ) ],
		709 : [ ( 'windowId', Byte ) ],
		734 : [ ( 'windowId', Byte ) ],
		735 : [ ( 'windowId', Byte ) ],
		736 : [ ( 'windowId', Byte ) ],
		751 : [ ( 'windowId', Byte ) ],
		755 : [ ( 'windowId', Byte ) ],
		756 : [ ( 'windowId', Byte ) ],
		757 : [ ( 'windowId', Byte ) ]
	}
