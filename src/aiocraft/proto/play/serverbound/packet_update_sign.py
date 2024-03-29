"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketUpdateSign(Packet):
	__slots__ = ( 'id', 'location', 'text1', 'text2', 'text3', 'text4' )
	
	location : tuple
	text1 : str
	text2 : str
	text3 : str
	text4 : str

	def __init__(self, 
		location:tuple | None = None,
		text1:str | None = None,
		text2:str | None = None,
		text3:str | None = None,
		text4:str | None = None,
		**kwargs
	):
		super().__init__(
			location=location,
			text1=text1,
			text2=text2,
			text3=text3,
			text4=text4
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 18,
		76 : 22,
		107 : 25,
		108 : 25,
		109 : 25,
		110 : 25,
		201 : 25,
		210 : 25,
		304 : 25,
		315 : 25,
		321 : 27,
		327 : 27,
		331 : 27,
		335 : 28,
		338 : 28,
		340 : 28,
		351 : 28,
		393 : 38,
		401 : 38,
		402 : 38,
		403 : 38,
		404 : 38,
		477 : 41,
		480 : 41,
		490 : 41,
		498 : 41,
		573 : 41,
		575 : 41,
		578 : 41,
		709 : 41,
		734 : 42,
		735 : 42,
		736 : 42,
		751 : 43,
		755 : 43,
		756 : 43,
		757 : 43,
		758 : 43,
		759 : 45,
		760 : 46,
		761 : 46
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		76 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		107 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		108 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		109 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		110 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		201 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		210 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		304 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		315 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		321 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		327 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		331 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		335 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		338 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		340 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		351 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		393 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		401 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		402 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		403 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		404 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		477 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		480 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		490 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		498 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		573 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		575 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		578 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		709 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		734 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		735 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		736 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		751 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		755 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		756 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		757 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		758 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		759 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		760 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ],
		761 : [ ( 'location', Position ), ( 'text1', String ), ( 'text2', String ), ( 'text3', String ), ( 'text4', String ) ]
	}
