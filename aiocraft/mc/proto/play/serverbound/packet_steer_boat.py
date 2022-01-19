"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketSteerBoat(Packet):
	__slots__ = ( 'id', 'leftPaddle', 'rightPaddle' )
	
	leftPaddle : bool
	rightPaddle : bool

	def __init__(self, proto:int,
		leftPaddle:bool=None,
		rightPaddle:bool=None,
		**kwargs
	):
		super().__init__(proto,
			leftPaddle=leftPaddle,
			rightPaddle=rightPaddle
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		107 : 17,
		108 : 17,
		109 : 17,
		110 : 17,
		201 : 17,
		210 : 17,
		304 : 17,
		315 : 17,
		321 : 18,
		327 : 18,
		331 : 18,
		335 : 18,
		338 : 17,
		340 : 17,
		351 : 17,
		393 : 20,
		401 : 20,
		402 : 20,
		403 : 20,
		404 : 20,
		477 : 22,
		480 : 22,
		490 : 22,
		498 : 22,
		573 : 22,
		575 : 22,
		578 : 22,
		709 : 22,
		734 : 23,
		735 : 23,
		736 : 23,
		751 : 23,
		755 : 22,
		756 : 22,
		757 : 22
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		107 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		108 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		109 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		110 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		201 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		210 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		304 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		315 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		321 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		327 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		331 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		335 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		338 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		340 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		351 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		393 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		401 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		402 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		403 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		404 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		477 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		480 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		490 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		498 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		573 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		575 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		578 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		709 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		734 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		735 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		736 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		751 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		755 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		756 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ],
		757 : [ ( 'leftPaddle', Boolean ), ( 'rightPaddle', Boolean ) ]
	}
