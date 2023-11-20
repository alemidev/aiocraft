"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketChat(Packet):
	__slots__ = ( 'id', 'message' )
	
	message : str

	def __init__(self, 
		message:str | None = None,
		**kwargs
	):
		super().__init__(
			message=message
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 1,
		76 : 1,
		107 : 2,
		108 : 2,
		109 : 2,
		110 : 2,
		201 : 2,
		210 : 2,
		304 : 2,
		315 : 2,
		321 : 3,
		327 : 3,
		331 : 3,
		335 : 3,
		338 : 2,
		340 : 2,
		351 : 1,
		393 : 2,
		401 : 2,
		402 : 2,
		403 : 2,
		404 : 2,
		477 : 3,
		480 : 3,
		490 : 3,
		498 : 3,
		573 : 3,
		575 : 3,
		578 : 3,
		709 : 3,
		734 : 3,
		735 : 3,
		736 : 3,
		751 : 3,
		755 : 3,
		756 : 3,
		757 : 3,
		758 : 3
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'message', String ) ],
		76 : [ ( 'message', String ) ],
		107 : [ ( 'message', String ) ],
		108 : [ ( 'message', String ) ],
		109 : [ ( 'message', String ) ],
		110 : [ ( 'message', String ) ],
		201 : [ ( 'message', String ) ],
		210 : [ ( 'message', String ) ],
		304 : [ ( 'message', String ) ],
		315 : [ ( 'message', String ) ],
		321 : [ ( 'message', String ) ],
		327 : [ ( 'message', String ) ],
		331 : [ ( 'message', String ) ],
		335 : [ ( 'message', String ) ],
		338 : [ ( 'message', String ) ],
		340 : [ ( 'message', String ) ],
		351 : [ ( 'message', String ) ],
		393 : [ ( 'message', String ) ],
		401 : [ ( 'message', String ) ],
		402 : [ ( 'message', String ) ],
		403 : [ ( 'message', String ) ],
		404 : [ ( 'message', String ) ],
		477 : [ ( 'message', String ) ],
		480 : [ ( 'message', String ) ],
		490 : [ ( 'message', String ) ],
		498 : [ ( 'message', String ) ],
		573 : [ ( 'message', String ) ],
		575 : [ ( 'message', String ) ],
		578 : [ ( 'message', String ) ],
		709 : [ ( 'message', String ) ],
		734 : [ ( 'message', String ) ],
		735 : [ ( 'message', String ) ],
		736 : [ ( 'message', String ) ],
		751 : [ ( 'message', String ) ],
		755 : [ ( 'message', String ) ],
		756 : [ ( 'message', String ) ],
		757 : [ ( 'message', String ) ],
		758 : [ ( 'message', String ) ]
	}