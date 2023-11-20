"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketWorldBorder(Packet):
	__slots__ = ( 'id', 'action', 'new_radius', 'old_radius', 'portalBoundary', 'radius', 'speed', 'warning_blocks', 'warning_time', 'x', 'z' )
	
	action : int
	new_radius : Union[None, float]
	old_radius : Union[None, float]
	portalBoundary : Union[None, int]
	radius : Union[None, float]
	speed : Union[None, int]
	warning_blocks : Union[None, int]
	warning_time : Union[None, int]
	x : Union[None, float]
	z : Union[None, float]

	def __init__(self, 
		action:int | None = None,
		new_radius:Union[None, float] | None = None,
		old_radius:Union[None, float] | None = None,
		portalBoundary:Union[None, int] | None = None,
		radius:Union[None, float] | None = None,
		speed:Union[None, int] | None = None,
		warning_blocks:Union[None, int] | None = None,
		warning_time:Union[None, int] | None = None,
		x:Union[None, float] | None = None,
		z:Union[None, float] | None = None,
		**kwargs
	):
		super().__init__(
			action=action,
			new_radius=new_radius,
			old_radius=old_radius,
			portalBoundary=portalBoundary,
			radius=radius,
			speed=speed,
			warning_blocks=warning_blocks,
			warning_time=warning_time,
			x=x,
			z=z
		)

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
		751 : 61
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		76 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		107 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		108 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		109 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		110 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		201 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		210 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		304 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		315 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		321 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		327 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		331 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		335 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		338 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		340 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		351 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		393 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		401 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		402 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		403 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		404 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		477 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		480 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		490 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		498 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		573 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		575 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		578 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		709 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		734 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		735 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		736 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ],
		751 : [ ( 'action', VarInt ), ( 'radius', SwitchType('action', { 0 : Double }, None, ) ), ( 'x', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'z', SwitchType('action', { 2 : Double, 3 : Double }, None, ) ), ( 'old_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'new_radius', SwitchType('action', { 1 : Double, 3 : Double }, None, ) ), ( 'speed', SwitchType('action', { 1 : VarLong, 3 : VarLong }, None, ) ), ( 'portalBoundary', SwitchType('action', { 3 : VarInt }, None, ) ), ( 'warning_time', SwitchType('action', { 3 : VarInt, 4 : VarInt }, None, ) ), ( 'warning_blocks', SwitchType('action', { 3 : VarInt, 5 : VarInt }, None, ) ) ]
	}