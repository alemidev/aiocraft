"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketAbilities(Packet):
	__slots__ = ( 'id', 'flags', 'flyingSpeed', 'walkingSpeed' )
	
	flags : int
	flyingSpeed : float
	walkingSpeed : float

	def __init__(self, proto:int,
		flags:int=None,
		flyingSpeed:float=None,
		walkingSpeed:float=None,
		**kwargs
	):
		super().__init__(proto,
			flags=flags,
			flyingSpeed=flyingSpeed,
			walkingSpeed=walkingSpeed
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 19,
		76 : 15,
		107 : 18,
		108 : 18,
		109 : 18,
		110 : 18,
		201 : 18,
		210 : 18,
		304 : 18,
		315 : 18,
		321 : 19,
		327 : 19,
		331 : 19,
		335 : 19,
		338 : 19,
		340 : 19,
		351 : 19,
		393 : 23,
		401 : 23,
		402 : 23,
		403 : 23,
		404 : 23,
		477 : 25,
		480 : 25,
		490 : 25,
		498 : 25,
		573 : 25,
		575 : 25,
		578 : 25,
		709 : 25,
		734 : 26,
		735 : 26,
		736 : 26,
		751 : 26,
		755 : 25,
		756 : 25,
		757 : 25
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		76 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		107 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		108 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		109 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		110 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		201 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		210 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		304 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		315 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		321 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		327 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		331 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		335 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		338 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		340 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		351 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		393 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		401 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		402 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		403 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		404 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		477 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		480 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		490 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		498 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		573 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		575 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		578 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		709 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		734 : [ ( 'flags', Byte ) ],
		735 : [ ( 'flags', Byte ) ],
		736 : [ ( 'flags', Byte ) ],
		751 : [ ( 'flags', Byte ) ],
		755 : [ ( 'flags', Byte ) ],
		756 : [ ( 'flags', Byte ) ],
		757 : [ ( 'flags', Byte ) ]
	}
