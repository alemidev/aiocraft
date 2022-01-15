"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketLoginPluginRequest(Packet):
	__slots__ = ( 'id', 'channel', 'data', 'messageId' )
	
	channel : str
	data : bytes
	messageId : int

	def __init__(self, proto:int,
		channel:str=None,
		data:bytes=None,
		messageId:int=None,
		**kwargs
	):
		super().__init__(proto,
			channel=channel,
			data=data,
			messageId=messageId
		)

	_state : int = 2

	_ids : Dict[int, int] = {
		393 : 4,
		401 : 4,
		402 : 4,
		403 : 4,
		404 : 4,
		477 : 4,
		480 : 4,
		490 : 4,
		498 : 4,
		573 : 4,
		575 : 4,
		578 : 4,
		709 : 4,
		734 : 4,
		735 : 4,
		736 : 4,
		751 : 4,
		755 : 4,
		756 : 4,
		757 : 4
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		401 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		402 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		403 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		404 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		477 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		480 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		490 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		498 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		573 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		575 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		578 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		709 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		734 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		735 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		736 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		751 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		755 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		756 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ],
		757 : [ ( 'messageId', VarInt ), ( 'channel', String ), ( 'data', TrailingData ) ]
	}
