"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketWorldBorder(Packet):
	__slots__ = ( 'id', 'old_radius', 'new_radius', 'radius', 'portalBoundary', 'action', 'x', 'speed', 'warning_time', 'z', 'warning_blocks' )
	
	old_radius : bytes
	new_radius : bytes
	radius : bytes
	portalBoundary : bytes
	action : int
	x : bytes
	speed : bytes
	warning_time : bytes
	z : bytes
	warning_blocks : bytes

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 68,
		76 : 53,
		107 : 53,
		108 : 53,
		109 : 53,
		110 : 53,
		201 : 53,
		210 : 53,
		304 : 53,
		315 : 53,
		321 : 55,
		327 : 55,
		331 : 55,
		335 : 55,
		338 : 56,
		340 : 56,
		351 : 57,
		393 : 59,
		401 : 59,
		402 : 59,
		403 : 59,
		404 : 59,
		477 : 61,
		480 : 61,
		490 : 61,
		498 : 61,
		573 : 62,
		575 : 62,
		578 : 62,
		709 : 62,
		734 : 61,
		735 : 61,
		736 : 61,
		751 : 61,
		1073741839 : 62
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		76 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		107 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		108 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		109 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		110 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		201 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		210 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		304 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		315 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		321 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		327 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		331 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		335 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		338 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		340 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		351 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		393 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		401 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		402 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		403 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		404 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		477 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		480 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		490 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		498 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		573 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		575 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		578 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		709 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		734 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		735 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		736 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		751 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		1073741839 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarInt, 3 : VarInt }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ]
	}
