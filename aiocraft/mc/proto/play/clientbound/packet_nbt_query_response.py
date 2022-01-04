"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketNbtQueryResponse(Packet):
	__slots__ = ( 'id', 'transactionId', 'nbt' )
	
	transactionId : int
	nbt : bytes

	_state : int = 3

	_ids : Dict[int, int] = {
		393 : 29,
		401 : 29,
		402 : 29,
		403 : 29,
		404 : 29,
		477 : 84,
		480 : 84,
		490 : 84,
		498 : 84,
		573 : 85,
		575 : 85,
		578 : 85,
		709 : 85,
		734 : 84,
		735 : 84,
		736 : 84,
		751 : 84,
		755 : 95,
		756 : 95,
		757 : 96,
		1073741839 : 85
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		401 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		402 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		403 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		404 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		477 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		480 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		490 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		498 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		573 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		575 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		578 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		709 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		734 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		735 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		736 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		751 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		755 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		756 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		757 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ],
		1073741839 : [ ( 'transactionId', VarInt ), ( 'nbt', OptionalType(NBTTag) ) ]
	}
