"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketClearTitles(Packet):
	__slots__ = ( 'id', 'reset' )
	
	reset : bool

	def __init__(self, proto:int,
		reset:bool=None,
		**kwargs
	):
		super().__init__(proto,
			reset=reset
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		755 : 16,
		756 : 16,
		757 : 16
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		755 : [ ( 'reset', Boolean ) ],
		756 : [ ( 'reset', Boolean ) ],
		757 : [ ( 'reset', Boolean ) ]
	}