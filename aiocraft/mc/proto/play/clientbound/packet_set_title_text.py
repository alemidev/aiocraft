"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketSetTitleText(Packet):
	__slots__ = ( 'id', 'text' )
	
	text : str

	def __init__(self, proto:int,
		text:str=None,
		**kwargs
	):
		super().__init__(proto,
			text=text
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		755 : 89,
		756 : 89,
		757 : 90,
		758 : 90,
		759 : 90,
		760 : 93,
		761 : 91
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		755 : [ ( 'text', String ) ],
		756 : [ ( 'text', String ) ],
		757 : [ ( 'text', String ) ],
		758 : [ ( 'text', String ) ],
		759 : [ ( 'text', String ) ],
		760 : [ ( 'text', String ) ],
		761 : [ ( 'text', String ) ]
	}
