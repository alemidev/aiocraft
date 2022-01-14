"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketPing(Packet):
	__slots__ = ( 'id', 'id' )
	
	id : int

	def __init__(self, proto:int,
		id:int=None
	):
		super().__init__(proto,
			id=id
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		755 : 48,
		756 : 48,
		757 : 48
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		755 : [ ( 'id', Int ) ],
		756 : [ ( 'id', Int ) ],
		757 : [ ( 'id', Int ) ]
	}
