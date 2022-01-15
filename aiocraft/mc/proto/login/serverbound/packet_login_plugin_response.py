"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketLoginPluginResponse(Packet):
	__slots__ = ( 'id', 'data', 'messageId' )
	
	data : tuple
	messageId : int

	def __init__(self, proto:int,
		data:tuple=None,
		messageId:int=None,
		**kwargs
	):
		super().__init__(proto,
			data=data,
			messageId=messageId
		)

	_state : int = 2

	_ids : Dict[int, int] = {
		393 : 2,
		401 : 2,
		402 : 2,
		403 : 2,
		404 : 2,
		477 : 2,
		480 : 2,
		490 : 2,
		498 : 2,
		573 : 2,
		575 : 2,
		578 : 2,
		709 : 2,
		734 : 2,
		735 : 2,
		736 : 2,
		751 : 2,
		755 : 2,
		756 : 2,
		757 : 2
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		401 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		402 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		403 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		404 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		477 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		480 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		490 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		498 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		573 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		575 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		578 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		709 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		734 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		735 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		736 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		751 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		755 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		756 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ],
		757 : [ ( 'messageId', VarInt ), ( 'data', OptionalType(TrailingData, ) ) ]
	}