"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketSpectate(Packet):
	__slots__ = ( 'id', 'target' )
	
	target : str

	def __init__(self, 
		target:str | None = None,
		**kwargs
	):
		super().__init__(
			target=target
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 24,
		76 : 24,
		107 : 27,
		108 : 27,
		109 : 27,
		110 : 27,
		201 : 27,
		210 : 27,
		304 : 27,
		315 : 27,
		321 : 29,
		327 : 29,
		331 : 29,
		335 : 30,
		338 : 30,
		340 : 30,
		351 : 30,
		393 : 40,
		401 : 40,
		402 : 40,
		403 : 40,
		404 : 40,
		477 : 43,
		480 : 43,
		490 : 43,
		498 : 43,
		573 : 43,
		575 : 43,
		578 : 43,
		709 : 43,
		734 : 44,
		735 : 44,
		736 : 44,
		751 : 45,
		755 : 45,
		756 : 45,
		757 : 45,
		758 : 45,
		759 : 47,
		760 : 48,
		761 : 48
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'target', UUID ) ],
		76 : [ ( 'target', UUID ) ],
		107 : [ ( 'target', UUID ) ],
		108 : [ ( 'target', UUID ) ],
		109 : [ ( 'target', UUID ) ],
		110 : [ ( 'target', UUID ) ],
		201 : [ ( 'target', UUID ) ],
		210 : [ ( 'target', UUID ) ],
		304 : [ ( 'target', UUID ) ],
		315 : [ ( 'target', UUID ) ],
		321 : [ ( 'target', UUID ) ],
		327 : [ ( 'target', UUID ) ],
		331 : [ ( 'target', UUID ) ],
		335 : [ ( 'target', UUID ) ],
		338 : [ ( 'target', UUID ) ],
		340 : [ ( 'target', UUID ) ],
		351 : [ ( 'target', UUID ) ],
		393 : [ ( 'target', UUID ) ],
		401 : [ ( 'target', UUID ) ],
		402 : [ ( 'target', UUID ) ],
		403 : [ ( 'target', UUID ) ],
		404 : [ ( 'target', UUID ) ],
		477 : [ ( 'target', UUID ) ],
		480 : [ ( 'target', UUID ) ],
		490 : [ ( 'target', UUID ) ],
		498 : [ ( 'target', UUID ) ],
		573 : [ ( 'target', UUID ) ],
		575 : [ ( 'target', UUID ) ],
		578 : [ ( 'target', UUID ) ],
		709 : [ ( 'target', UUID ) ],
		734 : [ ( 'target', UUID ) ],
		735 : [ ( 'target', UUID ) ],
		736 : [ ( 'target', UUID ) ],
		751 : [ ( 'target', UUID ) ],
		755 : [ ( 'target', UUID ) ],
		756 : [ ( 'target', UUID ) ],
		757 : [ ( 'target', UUID ) ],
		758 : [ ( 'target', UUID ) ],
		759 : [ ( 'target', UUID ) ],
		760 : [ ( 'target', UUID ) ],
		761 : [ ( 'target', UUID ) ]
	}
