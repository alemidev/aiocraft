"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketNameItem(Packet):
	__slots__ = ( 'id', 'name' )
	
	name : str

	def __init__(self, proto:int,
		name:str=None,
		**kwargs
	):
		super().__init__(proto,
			name=name
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		393 : 28,
		401 : 28,
		402 : 28,
		403 : 28,
		404 : 28,
		477 : 30,
		480 : 30,
		490 : 30,
		498 : 30,
		573 : 30,
		575 : 30,
		578 : 30,
		709 : 30,
		734 : 31,
		735 : 31,
		736 : 31,
		751 : 32,
		755 : 32,
		756 : 32,
		757 : 32
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'name', String ) ],
		401 : [ ( 'name', String ) ],
		402 : [ ( 'name', String ) ],
		403 : [ ( 'name', String ) ],
		404 : [ ( 'name', String ) ],
		477 : [ ( 'name', String ) ],
		480 : [ ( 'name', String ) ],
		490 : [ ( 'name', String ) ],
		498 : [ ( 'name', String ) ],
		573 : [ ( 'name', String ) ],
		575 : [ ( 'name', String ) ],
		578 : [ ( 'name', String ) ],
		709 : [ ( 'name', String ) ],
		734 : [ ( 'name', String ) ],
		735 : [ ( 'name', String ) ],
		736 : [ ( 'name', String ) ],
		751 : [ ( 'name', String ) ],
		755 : [ ( 'name', String ) ],
		756 : [ ( 'name', String ) ],
		757 : [ ( 'name', String ) ]
	}