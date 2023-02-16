"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketCraftRecipeResponse(Packet):
	__slots__ = ( 'id', 'recipe', 'windowId' )
	
	recipe : Union[int,str]
	windowId : int

	def __init__(self, proto:int,
		recipe:Union[int,str]=None,
		windowId:int=None,
		**kwargs
	):
		super().__init__(proto,
			recipe=recipe,
			windowId=windowId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		338 : 43,
		340 : 43,
		351 : 44,
		393 : 45,
		401 : 45,
		402 : 45,
		403 : 45,
		404 : 45,
		477 : 48,
		480 : 48,
		490 : 48,
		498 : 48,
		573 : 49,
		575 : 49,
		578 : 49,
		709 : 49,
		734 : 48,
		735 : 48,
		736 : 48,
		751 : 47,
		755 : 49,
		756 : 49,
		757 : 49,
		758 : 49,
		759 : 46,
		760 : 48,
		761 : 47
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		338 : [ ( 'windowId', Byte ), ( 'recipe', VarInt ) ],
		340 : [ ( 'windowId', Byte ), ( 'recipe', VarInt ) ],
		351 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		393 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		401 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		402 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		403 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		404 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		477 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		480 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		490 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		498 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		573 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		575 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		578 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		709 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		734 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		735 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		736 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		751 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		755 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		756 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		757 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		758 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		759 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		760 : [ ( 'windowId', Byte ), ( 'recipe', String ) ],
		761 : [ ( 'windowId', Byte ), ( 'recipe', String ) ]
	}
