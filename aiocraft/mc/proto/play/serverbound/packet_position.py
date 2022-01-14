"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketPosition(Packet):
	__slots__ = ( 'id', 'onGround', 'x', 'y', 'z' )
	
	onGround : bool
	x : float
	y : float
	z : float

	def __init__(self, proto:int,
		onGround:bool=None,
		x:float=None,
		y:float=None,
		z:float=None
	):
		super().__init__(proto,
			onGround=onGround,
			x=x,
			y=y,
			z=z
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 4,
		76 : 11,
		107 : 12,
		108 : 12,
		109 : 12,
		110 : 12,
		201 : 12,
		210 : 12,
		304 : 12,
		315 : 12,
		321 : 13,
		327 : 13,
		331 : 13,
		335 : 14,
		338 : 13,
		340 : 13,
		351 : 13,
		393 : 16,
		401 : 16,
		402 : 16,
		403 : 16,
		404 : 16,
		477 : 17,
		480 : 17,
		490 : 17,
		498 : 17,
		573 : 17,
		575 : 17,
		578 : 17,
		709 : 17,
		734 : 18,
		735 : 18,
		736 : 18,
		751 : 18,
		755 : 17,
		756 : 17,
		757 : 17
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		76 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		107 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		108 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		109 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		110 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		201 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		210 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		304 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		315 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		321 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		327 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		331 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		335 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		338 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		340 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		351 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		393 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		401 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		402 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		403 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		404 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		477 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		480 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		490 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		498 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		573 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		575 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		578 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		709 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		734 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		735 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		736 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		751 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		755 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		756 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ],
		757 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'onGround', Boolean ) ]
	}
