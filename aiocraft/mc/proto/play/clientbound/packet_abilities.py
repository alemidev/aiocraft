"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
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
		47 : 57,
		76 : 43,
		107 : 43,
		108 : 43,
		109 : 43,
		110 : 43,
		201 : 43,
		210 : 43,
		304 : 43,
		315 : 43,
		321 : 44,
		327 : 44,
		331 : 44,
		335 : 43,
		338 : 44,
		340 : 44,
		351 : 45,
		393 : 46,
		401 : 46,
		402 : 46,
		403 : 46,
		404 : 46,
		477 : 49,
		480 : 49,
		490 : 49,
		498 : 49,
		573 : 50,
		575 : 50,
		578 : 50,
		709 : 50,
		734 : 49,
		735 : 49,
		736 : 49,
		751 : 48,
		755 : 50,
		756 : 50,
		757 : 50
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
		734 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		735 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		736 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		751 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		755 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		756 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ],
		757 : [ ( 'flags', Byte ), ( 'flyingSpeed', Float ), ( 'walkingSpeed', Float ) ]
	}
