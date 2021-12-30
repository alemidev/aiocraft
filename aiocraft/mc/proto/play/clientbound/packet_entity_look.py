"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketEntityLook(Packet):
	__slots__ = ( 'id', 'yaw', 'pitch', 'onGround', 'entityId' )
	
	yaw : int
	pitch : int
	onGround : bool
	entityId : int

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 22,
		47 : 22,
		76 : 40,
		107 : 39,
		108 : 39,
		109 : 39,
		110 : 39,
		201 : 39,
		210 : 39,
		304 : 39,
		315 : 39,
		321 : 40,
		327 : 40,
		331 : 40,
		335 : 40,
		338 : 40,
		340 : 40,
		351 : 41,
		393 : 42,
		401 : 42,
		402 : 42,
		403 : 42,
		404 : 42,
		477 : 42,
		480 : 42,
		490 : 42,
		498 : 42,
		573 : 43,
		575 : 43,
		578 : 43,
		709 : 43,
		734 : 42,
		735 : 42,
		736 : 42,
		751 : 41,
		755 : 43,
		756 : 43,
		757 : 43,
		1073741839 : 42
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'entityId', Int ), ( 'yaw', Byte ), ( 'pitch', Byte ) ],
		47 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		76 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		107 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		108 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		109 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		110 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		201 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		210 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		304 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		315 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		321 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		327 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		331 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		335 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		338 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		340 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		351 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		393 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		401 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		402 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		403 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		404 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		477 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		480 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		490 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		498 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		573 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		575 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		578 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		709 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		734 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		735 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		736 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		751 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		755 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		756 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		757 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		1073741839 : [ ( 'entityId', VarInt ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ]
	}
