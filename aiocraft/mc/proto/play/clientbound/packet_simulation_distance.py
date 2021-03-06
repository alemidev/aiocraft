"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketSimulationDistance(Packet):
	__slots__ = ( 'id', 'distance' )
	
	distance : int

	def __init__(self, proto:int,
		distance:int=None,
		**kwargs
	):
		super().__init__(proto,
			distance=distance
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		757 : 87
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		757 : [ ( 'distance', VarInt ) ]
	}
