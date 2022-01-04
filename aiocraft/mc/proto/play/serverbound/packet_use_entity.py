"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketUseEntity(Packet):
	__slots__ = ( 'id', 'hand', 'mouse', 'x', 'sneaking', 'z', 'y', 'target' )
	
	hand : bytes
	mouse : int
	x : bytes
	sneaking : bool
	z : bytes
	y : bytes
	target : int

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 2,
		47 : 2,
		76 : 9,
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
		335 : 11,
		338 : 10,
		340 : 10,
		351 : 10,
		393 : 13,
		401 : 13,
		402 : 13,
		403 : 13,
		404 : 13,
		477 : 14,
		480 : 14,
		490 : 14,
		498 : 14,
		573 : 14,
		575 : 14,
		578 : 14,
		709 : 14,
		734 : 14,
		735 : 14,
		736 : 14,
		751 : 14,
		755 : 13,
		756 : 13,
		757 : 13,
		1073741839 : 14
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'target', Int ), ( 'mouse', Byte ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ) ],
		47 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ) ],
		76 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		107 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		108 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		109 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		110 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		201 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		210 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		304 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		315 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		321 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		327 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		331 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		335 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		338 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		340 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		351 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		393 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		401 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		402 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		403 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		404 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		477 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		480 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		490 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		498 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		573 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		575 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		578 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		709 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		734 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'sneaking', Boolean ) ],
		735 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'sneaking', Boolean ) ],
		736 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'sneaking', Boolean ) ],
		751 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'sneaking', Boolean ) ],
		755 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'sneaking', Boolean ) ],
		756 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'sneaking', Boolean ) ],
		757 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'sneaking', Boolean ) ],
		1073741839 : [ ( 'target', VarInt ), ( 'mouse', VarInt ), ( 'x', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'y', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'z', SwitchType('mouse', { 2 : Float }, None, ) ), ( 'hand', SwitchType('mouse', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'sneaking', Boolean ) ]
	}
