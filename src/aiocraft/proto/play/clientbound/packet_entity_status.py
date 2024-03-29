"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketEntityStatus(Packet):
	__slots__ = ( 'id', 'entityId', 'entityStatus' )
	
	entityId : int
	entityStatus : int

	def __init__(self, 
		entityId:int | None = None,
		entityStatus:int | None = None,
		**kwargs
	):
		super().__init__(
			entityId=entityId,
			entityStatus=entityStatus
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 26,
		76 : 26,
		107 : 27,
		108 : 27,
		109 : 27,
		110 : 27,
		201 : 27,
		210 : 27,
		304 : 27,
		315 : 27,
		321 : 28,
		327 : 28,
		331 : 28,
		335 : 27,
		338 : 27,
		340 : 27,
		351 : 28,
		393 : 28,
		401 : 28,
		402 : 28,
		403 : 28,
		404 : 28,
		477 : 27,
		480 : 27,
		490 : 27,
		498 : 27,
		573 : 28,
		575 : 28,
		578 : 28,
		709 : 28,
		734 : 27,
		735 : 27,
		736 : 27,
		751 : 26,
		755 : 27,
		756 : 27,
		757 : 27,
		758 : 27,
		759 : 24,
		760 : 26,
		761 : 25
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		76 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		107 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		108 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		109 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		110 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		201 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		210 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		304 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		315 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		321 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		327 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		331 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		335 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		338 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		340 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		351 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		393 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		401 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		402 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		403 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		404 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		477 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		480 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		490 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		498 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		573 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		575 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		578 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		709 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		734 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		735 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		736 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		751 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		755 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		756 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		757 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		758 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		759 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		760 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ],
		761 : [ ( 'entityId', Int ), ( 'entityStatus', Byte ) ]
	}
