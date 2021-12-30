"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketActionBar(Packet):
	__slots__ = ( 'id', 'text' )
	
	text : str

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
