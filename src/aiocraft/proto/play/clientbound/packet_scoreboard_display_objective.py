"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketScoreboardDisplayObjective(Packet):
	__slots__ = ( 'id', 'name', 'position' )
	
	name : str
	position : int

	def __init__(self, 
		name:str | None = None,
		position:int | None = None,
		**kwargs
	):
		super().__init__(
			name=name,
			position=position
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 61,
		76 : 56,
		107 : 56,
		108 : 56,
		109 : 56,
		110 : 56,
		201 : 56,
		210 : 56,
		304 : 56,
		315 : 56,
		321 : 58,
		327 : 58,
		331 : 58,
		335 : 58,
		338 : 59,
		340 : 59,
		351 : 60,
		393 : 62,
		401 : 62,
		402 : 62,
		403 : 62,
		404 : 62,
		477 : 66,
		480 : 66,
		490 : 66,
		498 : 66,
		573 : 67,
		575 : 67,
		578 : 67,
		709 : 68,
		734 : 67,
		735 : 67,
		736 : 67,
		751 : 67,
		755 : 76,
		756 : 76,
		757 : 76,
		758 : 76,
		759 : 76,
		760 : 79,
		761 : 77
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'position', Byte ), ( 'name', String ) ],
		76 : [ ( 'position', Byte ), ( 'name', String ) ],
		107 : [ ( 'position', Byte ), ( 'name', String ) ],
		108 : [ ( 'position', Byte ), ( 'name', String ) ],
		109 : [ ( 'position', Byte ), ( 'name', String ) ],
		110 : [ ( 'position', Byte ), ( 'name', String ) ],
		201 : [ ( 'position', Byte ), ( 'name', String ) ],
		210 : [ ( 'position', Byte ), ( 'name', String ) ],
		304 : [ ( 'position', Byte ), ( 'name', String ) ],
		315 : [ ( 'position', Byte ), ( 'name', String ) ],
		321 : [ ( 'position', Byte ), ( 'name', String ) ],
		327 : [ ( 'position', Byte ), ( 'name', String ) ],
		331 : [ ( 'position', Byte ), ( 'name', String ) ],
		335 : [ ( 'position', Byte ), ( 'name', String ) ],
		338 : [ ( 'position', Byte ), ( 'name', String ) ],
		340 : [ ( 'position', Byte ), ( 'name', String ) ],
		351 : [ ( 'position', Byte ), ( 'name', String ) ],
		393 : [ ( 'position', Byte ), ( 'name', String ) ],
		401 : [ ( 'position', Byte ), ( 'name', String ) ],
		402 : [ ( 'position', Byte ), ( 'name', String ) ],
		403 : [ ( 'position', Byte ), ( 'name', String ) ],
		404 : [ ( 'position', Byte ), ( 'name', String ) ],
		477 : [ ( 'position', Byte ), ( 'name', String ) ],
		480 : [ ( 'position', Byte ), ( 'name', String ) ],
		490 : [ ( 'position', Byte ), ( 'name', String ) ],
		498 : [ ( 'position', Byte ), ( 'name', String ) ],
		573 : [ ( 'position', Byte ), ( 'name', String ) ],
		575 : [ ( 'position', Byte ), ( 'name', String ) ],
		578 : [ ( 'position', Byte ), ( 'name', String ) ],
		709 : [ ( 'position', Byte ), ( 'name', String ) ],
		734 : [ ( 'position', Byte ), ( 'name', String ) ],
		735 : [ ( 'position', Byte ), ( 'name', String ) ],
		736 : [ ( 'position', Byte ), ( 'name', String ) ],
		751 : [ ( 'position', Byte ), ( 'name', String ) ],
		755 : [ ( 'position', Byte ), ( 'name', String ) ],
		756 : [ ( 'position', Byte ), ( 'name', String ) ],
		757 : [ ( 'position', Byte ), ( 'name', String ) ],
		758 : [ ( 'position', Byte ), ( 'name', String ) ],
		759 : [ ( 'position', Byte ), ( 'name', String ) ],
		760 : [ ( 'position', Byte ), ( 'name', String ) ],
		761 : [ ( 'position', Byte ), ( 'name', String ) ]
	}
