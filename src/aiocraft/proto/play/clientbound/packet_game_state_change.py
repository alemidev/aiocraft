"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketGameStateChange(Packet):
	__slots__ = ( 'id', 'gameMode', 'reason' )
	
	gameMode : float
	reason : int

	def __init__(self, 
		gameMode:float | None = None,
		reason:int | None = None,
		**kwargs
	):
		super().__init__(
			gameMode=gameMode,
			reason=reason
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 43,
		76 : 30,
		107 : 30,
		108 : 30,
		109 : 30,
		110 : 30,
		201 : 30,
		210 : 30,
		304 : 30,
		315 : 30,
		321 : 31,
		327 : 31,
		331 : 31,
		335 : 30,
		338 : 30,
		340 : 30,
		351 : 31,
		393 : 32,
		401 : 32,
		402 : 32,
		403 : 32,
		404 : 32,
		477 : 30,
		480 : 30,
		490 : 30,
		498 : 30,
		573 : 31,
		575 : 31,
		578 : 31,
		709 : 31,
		734 : 30,
		735 : 30,
		736 : 30,
		751 : 29,
		755 : 30,
		756 : 30,
		757 : 30,
		758 : 30,
		759 : 27,
		760 : 29,
		761 : 28
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		76 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		107 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		108 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		109 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		110 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		201 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		210 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		304 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		315 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		321 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		327 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		331 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		335 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		338 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		340 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		351 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		393 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		401 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		402 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		403 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		404 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		477 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		480 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		490 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		498 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		573 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		575 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		578 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		709 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		734 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		735 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		736 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		751 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		755 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		756 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		757 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		758 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		759 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		760 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ],
		761 : [ ( 'reason', Byte ), ( 'gameMode', Float ) ]
	}
