"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketPong(Packet):
	__slots__ = ( 'id', 'id' )
	
	id : int

	def __init__(self, proto:int,
		id:int=None,
		**kwargs
	):
		super().__init__(proto,
			id=id
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		755 : 29,
		756 : 29,
		757 : 29
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		755 : [ ( 'id', Int ) ],
		756 : [ ( 'id', Int ) ],
		757 : [ ( 'id', Int ) ]
	}