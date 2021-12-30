"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketCamera(Packet):
	__slots__ = ( 'id', 'cameraId' )
	
	cameraId : int

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 67,
		76 : 54,
		107 : 54,
		108 : 54,
		109 : 54,
		110 : 54,
		201 : 54,
		210 : 54,
		304 : 54,
		315 : 54,
		321 : 56,
		327 : 56,
		331 : 56,
		335 : 56,
		338 : 57,
		340 : 57,
		351 : 58,
		393 : 60,
		401 : 60,
		402 : 60,
		403 : 60,
		404 : 60,
		477 : 62,
		480 : 62,
		490 : 62,
		498 : 62,
		573 : 63,
		575 : 63,
		578 : 63,
		709 : 63,
		734 : 62,
		735 : 62,
		736 : 62,
		751 : 62,
		755 : 71,
		756 : 71,
		757 : 71,
		1073741839 : 63
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'cameraId', VarInt ) ],
		76 : [ ( 'cameraId', VarInt ) ],
		107 : [ ( 'cameraId', VarInt ) ],
		108 : [ ( 'cameraId', VarInt ) ],
		109 : [ ( 'cameraId', VarInt ) ],
		110 : [ ( 'cameraId', VarInt ) ],
		201 : [ ( 'cameraId', VarInt ) ],
		210 : [ ( 'cameraId', VarInt ) ],
		304 : [ ( 'cameraId', VarInt ) ],
		315 : [ ( 'cameraId', VarInt ) ],
		321 : [ ( 'cameraId', VarInt ) ],
		327 : [ ( 'cameraId', VarInt ) ],
		331 : [ ( 'cameraId', VarInt ) ],
		335 : [ ( 'cameraId', VarInt ) ],
		338 : [ ( 'cameraId', VarInt ) ],
		340 : [ ( 'cameraId', VarInt ) ],
		351 : [ ( 'cameraId', VarInt ) ],
		393 : [ ( 'cameraId', VarInt ) ],
		401 : [ ( 'cameraId', VarInt ) ],
		402 : [ ( 'cameraId', VarInt ) ],
		403 : [ ( 'cameraId', VarInt ) ],
		404 : [ ( 'cameraId', VarInt ) ],
		477 : [ ( 'cameraId', VarInt ) ],
		480 : [ ( 'cameraId', VarInt ) ],
		490 : [ ( 'cameraId', VarInt ) ],
		498 : [ ( 'cameraId', VarInt ) ],
		573 : [ ( 'cameraId', VarInt ) ],
		575 : [ ( 'cameraId', VarInt ) ],
		578 : [ ( 'cameraId', VarInt ) ],
		709 : [ ( 'cameraId', VarInt ) ],
		734 : [ ( 'cameraId', VarInt ) ],
		735 : [ ( 'cameraId', VarInt ) ],
		736 : [ ( 'cameraId', VarInt ) ],
		751 : [ ( 'cameraId', VarInt ) ],
		755 : [ ( 'cameraId', VarInt ) ],
		756 : [ ( 'cameraId', VarInt ) ],
		757 : [ ( 'cameraId', VarInt ) ],
		1073741839 : [ ( 'cameraId', VarInt ) ]
	}
