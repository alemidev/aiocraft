"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketBlockAction(Packet):
	__slots__ = ( 'id', 'location', 'byte2', 'byte1', 'blockId' )
	
	location : Union[bytes,tuple]
	byte2 : int
	byte1 : int
	blockId : int

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 36,
		47 : 36,
		76 : 10,
		107 : 10,
		108 : 10,
		109 : 10,
		110 : 10,
		201 : 10,
		210 : 10,
		304 : 10,
		315 : 10,
		321 : 11,
		327 : 11,
		331 : 11,
		335 : 10,
		338 : 10,
		340 : 10,
		351 : 10,
		393 : 10,
		401 : 10,
		402 : 10,
		403 : 10,
		404 : 10,
		477 : 10,
		480 : 10,
		490 : 10,
		498 : 10,
		573 : 11,
		575 : 11,
		578 : 11,
		709 : 11,
		734 : 10,
		735 : 10,
		736 : 10,
		751 : 10,
		755 : 11,
		756 : 11,
		757 : 11,
		1073741839 : 11
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'location', TrailingData ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		47 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		76 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		107 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		108 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		109 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		110 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		201 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		210 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		304 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		315 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		321 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		327 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		331 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		335 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		338 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		340 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		351 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		393 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		401 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		402 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		403 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		404 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		477 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		480 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		490 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		498 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		573 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		575 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		578 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		709 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		734 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		735 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		736 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		751 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		755 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		756 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		757 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ],
		1073741839 : [ ( 'location', Position ), ( 'byte1', Byte ), ( 'byte2', Byte ), ( 'blockId', VarInt ) ]
	}
