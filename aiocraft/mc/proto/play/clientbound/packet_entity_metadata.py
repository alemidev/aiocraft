"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketEntityMetadata(Packet):
	__slots__ = ( 'id', 'entityId', 'metadata' )
	
	entityId : int
	metadata : dict

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 28,
		47 : 28,
		76 : 57,
		107 : 57,
		108 : 57,
		109 : 57,
		110 : 57,
		201 : 57,
		210 : 57,
		304 : 57,
		315 : 57,
		321 : 59,
		327 : 59,
		331 : 59,
		335 : 59,
		338 : 60,
		340 : 60,
		351 : 61,
		393 : 63,
		401 : 63,
		402 : 63,
		403 : 63,
		404 : 63,
		477 : 67,
		480 : 67,
		490 : 67,
		498 : 67,
		573 : 68,
		575 : 68,
		578 : 68,
		709 : 69,
		734 : 68,
		735 : 68,
		736 : 68,
		751 : 68,
		755 : 77,
		756 : 77,
		757 : 77,
		1073741839 : 69
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'entityId', Int ), ( 'metadata', EntityMetadata ) ],
		47 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		76 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		107 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		108 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		109 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		110 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		201 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		210 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		304 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		315 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		321 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		327 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		331 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		335 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		338 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		340 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		351 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		393 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		401 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		402 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		403 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		404 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		477 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		480 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		490 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		498 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		573 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		575 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		578 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		709 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		734 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		735 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		736 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		751 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		755 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		756 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		757 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ],
		1073741839 : [ ( 'entityId', VarInt ), ( 'metadata', EntityMetadata ) ]
	}
