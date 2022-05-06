"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketAcknowledgePlayerDigging(Packet):
	__slots__ = ( 'id', 'block', 'location', 'status', 'successful' )
	
	block : int
	location : tuple
	status : int
	successful : bool

	def __init__(self, proto:int,
		block:int=None,
		location:tuple=None,
		status:int=None,
		successful:bool=None,
		**kwargs
	):
		super().__init__(proto,
			block=block,
			location=location,
			status=status,
			successful=successful
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		498 : 92,
		573 : 8,
		575 : 8,
		578 : 8,
		709 : 8,
		734 : 7,
		735 : 7,
		736 : 7,
		751 : 7,
		755 : 8,
		756 : 8,
		757 : 8
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		498 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		573 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		575 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		578 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		709 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		734 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		735 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		736 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		751 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		755 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		756 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		757 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ]
	}