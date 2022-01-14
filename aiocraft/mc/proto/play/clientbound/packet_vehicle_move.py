"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketVehicleMove(Packet):
	__slots__ = ( 'id', 'pitch', 'x', 'y', 'yaw', 'z' )
	
	pitch : float
	x : float
	y : float
	yaw : float
	z : float

	def __init__(self, proto:int,
		pitch:float=None,
		x:float=None,
		y:float=None,
		yaw:float=None,
		z:float=None
	):
		super().__init__(proto,
			pitch=pitch,
			x=x,
			y=y,
			yaw=yaw,
			z=z
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		107 : 41,
		108 : 41,
		109 : 41,
		110 : 41,
		201 : 41,
		210 : 41,
		304 : 41,
		315 : 41,
		321 : 42,
		327 : 42,
		331 : 42,
		335 : 41,
		338 : 41,
		340 : 41,
		351 : 42,
		393 : 43,
		401 : 43,
		402 : 43,
		403 : 43,
		404 : 43,
		477 : 44,
		480 : 44,
		490 : 44,
		498 : 44,
		573 : 45,
		575 : 45,
		578 : 45,
		709 : 45,
		734 : 44,
		735 : 44,
		736 : 44,
		751 : 43,
		755 : 44,
		756 : 44,
		757 : 44
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		107 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		108 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		109 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		110 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		201 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		210 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		304 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		315 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		321 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		327 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		331 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		335 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		338 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		340 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		351 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		393 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		401 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		402 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		403 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		404 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		477 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		480 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		490 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		498 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		573 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		575 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		578 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		709 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		734 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		735 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		736 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		751 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		755 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		756 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ],
		757 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ) ]
	}
