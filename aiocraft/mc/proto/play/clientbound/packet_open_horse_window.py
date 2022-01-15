"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketOpenHorseWindow(Packet):
	__slots__ = ( 'id', 'entityId', 'nbSlots', 'windowId' )
	
	entityId : int
	nbSlots : int
	windowId : int

	def __init__(self, proto:int,
		entityId:int=None,
		nbSlots:int=None,
		windowId:int=None,
		**kwargs
	):
		super().__init__(proto,
			entityId=entityId,
			nbSlots=nbSlots,
			windowId=windowId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		477 : 31,
		480 : 31,
		490 : 31,
		498 : 31,
		573 : 32,
		575 : 32,
		578 : 32,
		709 : 32,
		734 : 31,
		735 : 31,
		736 : 31,
		751 : 30,
		755 : 31,
		756 : 31,
		757 : 31
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		477 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		480 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		490 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		498 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		573 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		575 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		578 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		709 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		734 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		735 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		736 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		751 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		755 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		756 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ],
		757 : [ ( 'windowId', Byte ), ( 'nbSlots', VarInt ), ( 'entityId', Int ) ]
	}
