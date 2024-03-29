"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketAcknowledgePlayerDigging(Packet):
	__slots__ = ( 'id', 'block', 'location', 'sequenceId', 'status', 'successful' )
	
	block : int
	location : tuple
	sequenceId : int
	status : int
	successful : bool

	def __init__(self, 
		block:int | None = None,
		location:tuple | None = None,
		sequenceId:int | None = None,
		status:int | None = None,
		successful:bool | None = None,
		**kwargs
	):
		super().__init__(
			block=block,
			location=location,
			sequenceId=sequenceId,
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
		757 : 8,
		758 : 8,
		759 : 5,
		760 : 5,
		761 : 5
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
		757 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		758 : [ ( 'location', Position ), ( 'block', VarInt ), ( 'status', VarInt ), ( 'successful', Boolean ) ],
		759 : [ ( 'sequenceId', VarInt ) ],
		760 : [ ( 'sequenceId', VarInt ) ],
		761 : [ ( 'sequenceId', VarInt ) ]
	}
