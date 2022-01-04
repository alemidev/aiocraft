"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketStopSound(Packet):
	__slots__ = ( 'id', 'sound', 'flags', 'source' )
	
	sound : bytes
	flags : int
	source : bytes

	_state : int = 3

	_ids : Dict[int, int] = {
		351 : 74,
		393 : 76,
		401 : 76,
		402 : 76,
		403 : 76,
		404 : 76,
		477 : 82,
		480 : 82,
		490 : 82,
		498 : 82,
		573 : 83,
		575 : 83,
		578 : 83,
		709 : 83,
		734 : 82,
		735 : 82,
		736 : 82,
		751 : 82,
		755 : 93,
		756 : 93,
		757 : 94,
		1073741839 : 83
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		351 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		393 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		401 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		402 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		403 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		404 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		477 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		480 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		490 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		498 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		573 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		575 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		578 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		709 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		734 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		735 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		736 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		751 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		755 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		756 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		757 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ],
		1073741839 : [ ( 'flags', Byte ), ( 'source', SwitchType('flags', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'sound', SwitchType('flags', { 2 : String, 3 : String }, None, ) ) ]
	}
