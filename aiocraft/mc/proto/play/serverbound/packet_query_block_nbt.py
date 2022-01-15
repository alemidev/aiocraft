"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketQueryBlockNbt(Packet):
	__slots__ = ( 'id', 'location', 'transactionId' )
	
	location : tuple
	transactionId : int

	def __init__(self, proto:int,
		location:tuple=None,
		transactionId:int=None,
		**kwargs
	):
		super().__init__(proto,
			location=location,
			transactionId=transactionId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		393 : 1,
		401 : 1,
		402 : 1,
		403 : 1,
		404 : 1,
		477 : 1,
		480 : 1,
		490 : 1,
		498 : 1,
		573 : 1,
		575 : 1,
		578 : 1,
		709 : 1,
		734 : 1,
		735 : 1,
		736 : 1,
		751 : 1,
		755 : 1,
		756 : 1,
		757 : 1
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		401 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		402 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		403 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		404 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		477 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		480 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		490 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		498 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		573 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		575 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		578 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		709 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		734 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		735 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		736 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		751 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		755 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		756 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ],
		757 : [ ( 'transactionId', VarInt ), ( 'location', Position ) ]
	}
