"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketUpdateCommandBlockMinecart(Packet):
	__slots__ = ( 'id', 'command', 'entityId', 'track_output' )
	
	command : str
	entityId : int
	track_output : bool

	def __init__(self, 
		command:str | None = None,
		entityId:int | None = None,
		track_output:bool | None = None,
		**kwargs
	):
		super().__init__(
			command=command,
			entityId=entityId,
			track_output=track_output
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		393 : 35,
		401 : 35,
		402 : 35,
		403 : 35,
		404 : 35,
		477 : 37,
		480 : 37,
		490 : 37,
		498 : 37,
		573 : 37,
		575 : 37,
		578 : 37,
		709 : 37,
		734 : 38,
		735 : 38,
		736 : 38,
		751 : 39,
		755 : 39,
		756 : 39,
		757 : 39,
		758 : 39,
		759 : 41,
		760 : 42,
		761 : 42
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		401 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		402 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		403 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		404 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		477 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		480 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		490 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		498 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		573 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		575 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		578 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		709 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		734 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		735 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		736 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		751 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		755 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		756 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		757 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		758 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		759 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		760 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ],
		761 : [ ( 'entityId', VarInt ), ( 'command', String ), ( 'track_output', Boolean ) ]
	}
