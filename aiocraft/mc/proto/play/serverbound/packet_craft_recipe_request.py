"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketCraftRecipeRequest(Packet):
	__slots__ = ( 'id', 'windowId', 'recipe', 'makeAll' )
	
	windowId : int
	recipe : Union[str,int]
	makeAll : bool

	_state : int = 3

	_ids : Dict[int, int] = {
		338 : 18,
		340 : 18,
		351 : 18,
		393 : 22,
		401 : 22,
		402 : 22,
		403 : 22,
		404 : 22,
		477 : 24,
		480 : 24,
		490 : 24,
		498 : 24,
		573 : 24,
		575 : 24,
		578 : 24,
		709 : 24,
		734 : 25,
		735 : 25,
		736 : 25,
		751 : 25,
		755 : 24,
		756 : 24,
		757 : 24,
		1073741839 : 25
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		338 : [ ( 'windowId', Byte ), ( 'recipe', VarInt ), ( 'makeAll', Boolean ) ],
		340 : [ ( 'windowId', Byte ), ( 'recipe', VarInt ), ( 'makeAll', Boolean ) ],
		351 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		393 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		401 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		402 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		403 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		404 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		477 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		480 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		490 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		498 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		573 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		575 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		578 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		709 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		734 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		735 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		736 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		751 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		755 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		756 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		757 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ],
		1073741839 : [ ( 'windowId', Byte ), ( 'recipe', String ), ( 'makeAll', Boolean ) ]
	}
