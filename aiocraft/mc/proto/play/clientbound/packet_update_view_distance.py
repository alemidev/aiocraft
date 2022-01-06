"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketUpdateViewDistance(Packet):
	__slots__ = ( 'id', 'viewDistance' )
	
	viewDistance : int

	def __init__(self, proto:int,
		viewDistance:int=None
	):
		super().__init__(proto,
			viewDistance=viewDistance
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		477 : 65,
		480 : 65,
		490 : 65,
		498 : 65,
		573 : 66,
		575 : 66,
		578 : 66,
		709 : 66,
		734 : 65,
		735 : 65,
		736 : 65,
		751 : 65,
		755 : 74,
		756 : 74,
		757 : 74
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		477 : [ ( 'viewDistance', VarInt ) ],
		480 : [ ( 'viewDistance', VarInt ) ],
		490 : [ ( 'viewDistance', VarInt ) ],
		498 : [ ( 'viewDistance', VarInt ) ],
		573 : [ ( 'viewDistance', VarInt ) ],
		575 : [ ( 'viewDistance', VarInt ) ],
		578 : [ ( 'viewDistance', VarInt ) ],
		709 : [ ( 'viewDistance', VarInt ) ],
		734 : [ ( 'viewDistance', VarInt ) ],
		735 : [ ( 'viewDistance', VarInt ) ],
		736 : [ ( 'viewDistance', VarInt ) ],
		751 : [ ( 'viewDistance', VarInt ) ],
		755 : [ ( 'viewDistance', VarInt ) ],
		756 : [ ( 'viewDistance', VarInt ) ],
		757 : [ ( 'viewDistance', VarInt ) ]
	}
