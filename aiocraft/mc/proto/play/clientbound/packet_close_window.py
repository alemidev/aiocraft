"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
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
		47 : 46,
		76 : 18,
		107 : 18,
		108 : 18,
		109 : 18,
		110 : 18,
		201 : 18,
		210 : 18,
		304 : 18,
		315 : 18,
		321 : 19,
		327 : 19,
		331 : 19,
		335 : 18,
		338 : 18,
		340 : 18,
		351 : 19,
		393 : 19,
		401 : 19,
		402 : 19,
		403 : 19,
		404 : 19,
		477 : 19,
		480 : 19,
		490 : 19,
		498 : 19,
		573 : 20,
		575 : 20,
		578 : 20,
		709 : 20,
		734 : 19,
		735 : 19,
		736 : 19,
		751 : 18,
		755 : 19,
		756 : 19,
		757 : 19
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
