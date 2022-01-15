"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketWorldBorderWarningReach(Packet):
	__slots__ = ( 'id', 'warningBlocks' )
	
	warningBlocks : int

	def __init__(self, proto:int,
		warningBlocks:int=None,
		**kwargs
	):
		super().__init__(proto,
			warningBlocks=warningBlocks
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		755 : 70,
		756 : 70,
		757 : 70
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		755 : [ ( 'warningBlocks', VarInt ) ],
		756 : [ ( 'warningBlocks', VarInt ) ],
		757 : [ ( 'warningBlocks', VarInt ) ]
	}
