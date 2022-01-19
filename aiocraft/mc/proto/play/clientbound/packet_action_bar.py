"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketActionBar(Packet):
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
		755 : 65,
		756 : 65,
		757 : 65
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		755 : [ ( 'text', String ) ],
		756 : [ ( 'text', String ) ],
		757 : [ ( 'text', String ) ]
	}
