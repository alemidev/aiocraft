"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketUpdateCommandBlock(Packet):
	__slots__ = ( 'id', 'command', 'flags', 'location', 'mode' )
	
	command : str
	flags : int
	location : tuple
	mode : int

	def __init__(self, proto:int,
		command:str=None,
		flags:int=None,
		location:tuple=None,
		mode:int=None,
		**kwargs
	):
		super().__init__(proto,
			command=command,
			flags=flags,
			location=location,
			mode=mode
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		393 : 34,
		401 : 34,
		402 : 34,
		403 : 34,
		404 : 34,
		477 : 36,
		480 : 36,
		490 : 36,
		498 : 36,
		573 : 36,
		575 : 36,
		578 : 36,
		709 : 36,
		734 : 37,
		735 : 37,
		736 : 37,
		751 : 38,
		755 : 38,
		756 : 38,
		757 : 38
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		401 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		402 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		403 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		404 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		477 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		480 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		490 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		498 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		573 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		575 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		578 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		709 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		734 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		735 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		736 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		751 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		755 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		756 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ],
		757 : [ ( 'location', Position ), ( 'command', String ), ( 'mode', VarInt ), ( 'flags', Byte ) ]
	}
