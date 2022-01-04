"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketSpawnEntityWeather(Packet):
	__slots__ = ( 'id', 'type', 'x', 'z', 'y', 'entityId' )
	
	type : int
	x : Union[int,float]
	z : Union[int,float]
	y : Union[int,float]
	entityId : int

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 44,
		47 : 44,
		76 : 2,
		107 : 2,
		108 : 2,
		109 : 2,
		110 : 2,
		201 : 2,
		210 : 2,
		304 : 2,
		315 : 2,
		321 : 2,
		327 : 2,
		331 : 2,
		335 : 2,
		338 : 2,
		340 : 2,
		351 : 2,
		393 : 2,
		401 : 2,
		402 : 2,
		403 : 2,
		404 : 2,
		477 : 2,
		480 : 2,
		490 : 2,
		498 : 2,
		573 : 2,
		575 : 2,
		578 : 2,
		709 : 2
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ) ],
		47 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ) ],
		76 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ) ],
		107 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		108 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		109 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		110 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		201 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		210 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		304 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		315 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		321 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		327 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		331 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		335 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		338 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		340 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		351 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		393 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		401 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		402 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		403 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		404 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		477 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		480 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		490 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		498 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		573 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		575 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		578 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ],
		709 : [ ( 'entityId', VarInt ), ( 'type', Byte ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ) ]
	}
