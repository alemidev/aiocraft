"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketRemoveEntityEffect(Packet):
	__slots__ = ( 'id', 'effectId', 'entityId' )
	
	effectId : int
	entityId : int

	def __init__(self, proto:int,
		effectId:int=None,
		entityId:int=None,
		**kwargs
	):
		super().__init__(proto,
			effectId=effectId,
			entityId=entityId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 30,
		76 : 49,
		107 : 49,
		108 : 49,
		109 : 49,
		110 : 49,
		201 : 49,
		210 : 49,
		304 : 49,
		315 : 49,
		321 : 51,
		327 : 51,
		331 : 51,
		335 : 50,
		338 : 51,
		340 : 51,
		351 : 52,
		393 : 54,
		401 : 54,
		402 : 54,
		403 : 54,
		404 : 54,
		477 : 56,
		480 : 56,
		490 : 56,
		498 : 56,
		573 : 57,
		575 : 57,
		578 : 57,
		709 : 57,
		734 : 56,
		735 : 56,
		736 : 56,
		751 : 55,
		755 : 59,
		756 : 59,
		757 : 59,
		758 : 59,
		759 : 57,
		760 : 60,
		761 : 59
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		76 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		107 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		108 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		109 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		110 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		201 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		210 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		304 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		315 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		321 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		327 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		331 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		335 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		338 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		340 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		351 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		393 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		401 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		402 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		403 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		404 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		477 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		480 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		490 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		498 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		573 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		575 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		578 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		709 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		734 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		735 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		736 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		751 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		755 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		756 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		757 : [ ( 'entityId', VarInt ), ( 'effectId', Byte ) ],
		758 : [ ( 'entityId', VarInt ), ( 'effectId', VarInt ) ],
		759 : [ ( 'entityId', VarInt ), ( 'effectId', VarInt ) ],
		760 : [ ( 'entityId', VarInt ), ( 'effectId', VarInt ) ],
		761 : [ ( 'entityId', VarInt ), ( 'effectId', VarInt ) ]
	}
