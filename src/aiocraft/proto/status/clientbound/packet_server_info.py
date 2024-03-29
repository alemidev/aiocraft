"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketServerInfo(Packet):
	__slots__ = ( 'id', 'response' )
	
	response : str

	def __init__(self, 
		response:str | None = None,
		**kwargs
	):
		super().__init__(
			response=response
		)

	_state : int = 1

	_ids : Dict[int, int] = {
		47 : 0,
		76 : 0,
		107 : 0,
		108 : 0,
		109 : 0,
		110 : 0,
		201 : 0,
		210 : 0,
		304 : 0,
		315 : 0,
		321 : 0,
		327 : 0,
		331 : 0,
		335 : 0,
		338 : 0,
		340 : 0,
		351 : 0,
		393 : 0,
		401 : 0,
		402 : 0,
		403 : 0,
		404 : 0,
		477 : 0,
		480 : 0,
		490 : 0,
		498 : 0,
		573 : 0,
		575 : 0,
		578 : 0,
		709 : 0,
		734 : 0,
		735 : 0,
		736 : 0,
		751 : 0,
		755 : 0,
		756 : 0,
		757 : 0,
		758 : 0,
		759 : 0,
		760 : 0,
		761 : 0
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'response', String ) ],
		76 : [ ( 'response', String ) ],
		107 : [ ( 'response', String ) ],
		108 : [ ( 'response', String ) ],
		109 : [ ( 'response', String ) ],
		110 : [ ( 'response', String ) ],
		201 : [ ( 'response', String ) ],
		210 : [ ( 'response', String ) ],
		304 : [ ( 'response', String ) ],
		315 : [ ( 'response', String ) ],
		321 : [ ( 'response', String ) ],
		327 : [ ( 'response', String ) ],
		331 : [ ( 'response', String ) ],
		335 : [ ( 'response', String ) ],
		338 : [ ( 'response', String ) ],
		340 : [ ( 'response', String ) ],
		351 : [ ( 'response', String ) ],
		393 : [ ( 'response', String ) ],
		401 : [ ( 'response', String ) ],
		402 : [ ( 'response', String ) ],
		403 : [ ( 'response', String ) ],
		404 : [ ( 'response', String ) ],
		477 : [ ( 'response', String ) ],
		480 : [ ( 'response', String ) ],
		490 : [ ( 'response', String ) ],
		498 : [ ( 'response', String ) ],
		573 : [ ( 'response', String ) ],
		575 : [ ( 'response', String ) ],
		578 : [ ( 'response', String ) ],
		709 : [ ( 'response', String ) ],
		734 : [ ( 'response', String ) ],
		735 : [ ( 'response', String ) ],
		736 : [ ( 'response', String ) ],
		751 : [ ( 'response', String ) ],
		755 : [ ( 'response', String ) ],
		756 : [ ( 'response', String ) ],
		757 : [ ( 'response', String ) ],
		758 : [ ( 'response', String ) ],
		759 : [ ( 'response', String ) ],
		760 : [ ( 'response', String ) ],
		761 : [ ( 'response', String ) ]
	}
