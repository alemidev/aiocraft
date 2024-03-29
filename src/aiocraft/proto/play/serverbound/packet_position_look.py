"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketPositionLook(Packet):
	__slots__ = ( 'id', 'onGround', 'pitch', 'x', 'y', 'yaw', 'z' )
	
	onGround : bool
	pitch : float
	x : float
	y : float
	yaw : float
	z : float

	def __init__(self, 
		onGround:bool | None = None,
		pitch:float | None = None,
		x:float | None = None,
		y:float | None = None,
		yaw:float | None = None,
		z:float | None = None,
		**kwargs
	):
		super().__init__(
			onGround=onGround,
			pitch=pitch,
			x=x,
			y=y,
			yaw=yaw,
			z=z
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 6,
		76 : 12,
		107 : 13,
		108 : 13,
		109 : 13,
		110 : 13,
		201 : 13,
		210 : 13,
		304 : 13,
		315 : 13,
		321 : 14,
		327 : 14,
		331 : 14,
		335 : 15,
		338 : 14,
		340 : 14,
		351 : 14,
		393 : 17,
		401 : 17,
		402 : 17,
		403 : 17,
		404 : 17,
		477 : 18,
		480 : 18,
		490 : 18,
		498 : 18,
		573 : 18,
		575 : 18,
		578 : 18,
		709 : 18,
		734 : 19,
		735 : 19,
		736 : 19,
		751 : 19,
		755 : 18,
		756 : 18,
		757 : 18,
		758 : 18,
		759 : 20,
		760 : 21,
		761 : 20
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		76 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		107 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		108 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		109 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		110 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		201 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		210 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		304 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		315 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		321 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		327 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		331 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		335 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		338 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		340 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		351 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		393 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		401 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		402 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		403 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		404 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		477 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		480 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		490 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		498 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		573 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		575 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		578 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		709 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		734 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		735 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		736 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		751 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		755 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		756 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		757 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		758 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		759 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		760 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ],
		761 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'onGround', Boolean ) ]
	}
