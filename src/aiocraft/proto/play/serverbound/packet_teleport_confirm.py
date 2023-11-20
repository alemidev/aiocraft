"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketTeleportConfirm(Packet):
	__slots__ = ( 'id', 'teleportId' )
	
	teleportId : int

	def __init__(self, 
		teleportId:int | None = None,
		**kwargs
	):
		super().__init__(
			teleportId=teleportId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
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
		107 : [ ( 'teleportId', VarInt ) ],
		108 : [ ( 'teleportId', VarInt ) ],
		109 : [ ( 'teleportId', VarInt ) ],
		110 : [ ( 'teleportId', VarInt ) ],
		201 : [ ( 'teleportId', VarInt ) ],
		210 : [ ( 'teleportId', VarInt ) ],
		304 : [ ( 'teleportId', VarInt ) ],
		315 : [ ( 'teleportId', VarInt ) ],
		321 : [ ( 'teleportId', VarInt ) ],
		327 : [ ( 'teleportId', VarInt ) ],
		331 : [ ( 'teleportId', VarInt ) ],
		335 : [ ( 'teleportId', VarInt ) ],
		338 : [ ( 'teleportId', VarInt ) ],
		340 : [ ( 'teleportId', VarInt ) ],
		351 : [ ( 'teleportId', VarInt ) ],
		393 : [ ( 'teleportId', VarInt ) ],
		401 : [ ( 'teleportId', VarInt ) ],
		402 : [ ( 'teleportId', VarInt ) ],
		403 : [ ( 'teleportId', VarInt ) ],
		404 : [ ( 'teleportId', VarInt ) ],
		477 : [ ( 'teleportId', VarInt ) ],
		480 : [ ( 'teleportId', VarInt ) ],
		490 : [ ( 'teleportId', VarInt ) ],
		498 : [ ( 'teleportId', VarInt ) ],
		573 : [ ( 'teleportId', VarInt ) ],
		575 : [ ( 'teleportId', VarInt ) ],
		578 : [ ( 'teleportId', VarInt ) ],
		709 : [ ( 'teleportId', VarInt ) ],
		734 : [ ( 'teleportId', VarInt ) ],
		735 : [ ( 'teleportId', VarInt ) ],
		736 : [ ( 'teleportId', VarInt ) ],
		751 : [ ( 'teleportId', VarInt ) ],
		755 : [ ( 'teleportId', VarInt ) ],
		756 : [ ( 'teleportId', VarInt ) ],
		757 : [ ( 'teleportId', VarInt ) ],
		758 : [ ( 'teleportId', VarInt ) ],
		759 : [ ( 'teleportId', VarInt ) ],
		760 : [ ( 'teleportId', VarInt ) ],
		761 : [ ( 'teleportId', VarInt ) ]
	}