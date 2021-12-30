"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketUpdateSign(Packet):
	__slots__ = ( 'id', 'text2', 'text1', 'text3', 'text4', 'location' )
	
	text2 : str
	text1 : str
	text3 : str
	text4 : str
	location : Union[tuple,bytes]

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 51,
		47 : 51,
		76 : 69,
		107 : 70,
		108 : 70,
		109 : 70
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'location', TrailingData ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		47 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		76 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		107 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		108 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		109 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ]
	}
