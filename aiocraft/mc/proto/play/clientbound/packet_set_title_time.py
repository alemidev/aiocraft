"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketSetTitleTime(Packet):
	__slots__ = ( 'id', 'fadeIn', 'fadeOut', 'stay' )
	
	fadeIn : int
	fadeOut : int
	stay : int

	def __init__(self, proto:int,
		fadeIn:int=None,
		fadeOut:int=None,
		stay:int=None,
		**kwargs
	):
		super().__init__(proto,
			fadeIn=fadeIn,
			fadeOut=fadeOut,
			stay=stay
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		755 : 90,
		756 : 90,
		757 : 91
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		755 : [ ( 'fadeIn', Int ), ( 'stay', Int ), ( 'fadeOut', Int ) ],
		756 : [ ( 'fadeIn', Int ), ( 'stay', Int ), ( 'fadeOut', Int ) ],
		757 : [ ( 'fadeIn', Int ), ( 'stay', Int ), ( 'fadeOut', Int ) ]
	}
