"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketChatPreview(Packet):
	__slots__ = ( 'id', 'message', 'query' )
	
	message : str
	query : int

	def __init__(self, 
		message:str | None = None,
		query:int | None = None,
		**kwargs
	):
		super().__init__(
			message=message,
			query=query
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		759 : 5,
		760 : 6
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		759 : [ ( 'query', Int ), ( 'message', String ) ],
		760 : [ ( 'query', Int ), ( 'message', String ) ]
	}
