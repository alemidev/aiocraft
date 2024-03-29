"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketPlayerlistHeader(Packet):
	__slots__ = ( 'id', 'footer', 'header' )
	
	footer : str
	header : str

	def __init__(self, 
		footer:str | None = None,
		header:str | None = None,
		**kwargs
	):
		super().__init__(
			footer=footer,
			header=header
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 71,
		76 : 70,
		107 : 72,
		108 : 72,
		109 : 72,
		110 : 71,
		201 : 71,
		210 : 71,
		304 : 71,
		315 : 71,
		321 : 73,
		327 : 73,
		331 : 73,
		335 : 73,
		338 : 74,
		340 : 74,
		351 : 76,
		393 : 78,
		401 : 78,
		402 : 78,
		403 : 78,
		404 : 78,
		477 : 83,
		480 : 83,
		490 : 83,
		498 : 83,
		573 : 84,
		575 : 84,
		578 : 84,
		709 : 84,
		734 : 83,
		735 : 83,
		736 : 83,
		751 : 83,
		755 : 94,
		756 : 94,
		757 : 95,
		758 : 95,
		759 : 96,
		760 : 99,
		761 : 97
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'header', String ), ( 'footer', String ) ],
		76 : [ ( 'header', String ), ( 'footer', String ) ],
		107 : [ ( 'header', String ), ( 'footer', String ) ],
		108 : [ ( 'header', String ), ( 'footer', String ) ],
		109 : [ ( 'header', String ), ( 'footer', String ) ],
		110 : [ ( 'header', String ), ( 'footer', String ) ],
		201 : [ ( 'header', String ), ( 'footer', String ) ],
		210 : [ ( 'header', String ), ( 'footer', String ) ],
		304 : [ ( 'header', String ), ( 'footer', String ) ],
		315 : [ ( 'header', String ), ( 'footer', String ) ],
		321 : [ ( 'header', String ), ( 'footer', String ) ],
		327 : [ ( 'header', String ), ( 'footer', String ) ],
		331 : [ ( 'header', String ), ( 'footer', String ) ],
		335 : [ ( 'header', String ), ( 'footer', String ) ],
		338 : [ ( 'header', String ), ( 'footer', String ) ],
		340 : [ ( 'header', String ), ( 'footer', String ) ],
		351 : [ ( 'header', String ), ( 'footer', String ) ],
		393 : [ ( 'header', String ), ( 'footer', String ) ],
		401 : [ ( 'header', String ), ( 'footer', String ) ],
		402 : [ ( 'header', String ), ( 'footer', String ) ],
		403 : [ ( 'header', String ), ( 'footer', String ) ],
		404 : [ ( 'header', String ), ( 'footer', String ) ],
		477 : [ ( 'header', String ), ( 'footer', String ) ],
		480 : [ ( 'header', String ), ( 'footer', String ) ],
		490 : [ ( 'header', String ), ( 'footer', String ) ],
		498 : [ ( 'header', String ), ( 'footer', String ) ],
		573 : [ ( 'header', String ), ( 'footer', String ) ],
		575 : [ ( 'header', String ), ( 'footer', String ) ],
		578 : [ ( 'header', String ), ( 'footer', String ) ],
		709 : [ ( 'header', String ), ( 'footer', String ) ],
		734 : [ ( 'header', String ), ( 'footer', String ) ],
		735 : [ ( 'header', String ), ( 'footer', String ) ],
		736 : [ ( 'header', String ), ( 'footer', String ) ],
		751 : [ ( 'header', String ), ( 'footer', String ) ],
		755 : [ ( 'header', String ), ( 'footer', String ) ],
		756 : [ ( 'header', String ), ( 'footer', String ) ],
		757 : [ ( 'header', String ), ( 'footer', String ) ],
		758 : [ ( 'header', String ), ( 'footer', String ) ],
		759 : [ ( 'header', String ), ( 'footer', String ) ],
		760 : [ ( 'header', String ), ( 'footer', String ) ],
		761 : [ ( 'header', String ), ( 'footer', String ) ]
	}
