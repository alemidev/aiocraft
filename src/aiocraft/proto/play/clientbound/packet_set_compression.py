"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketSetCompression(Packet):
	__slots__ = ( 'id', 'threshold' )
	
	threshold : int

	def __init__(self, 
		threshold:int | None = None,
		**kwargs
	):
		super().__init__(
			threshold=threshold
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 70,
		76 : 29
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'threshold', VarInt ) ],
		76 : [ ( 'threshold', VarInt ) ]
	}
