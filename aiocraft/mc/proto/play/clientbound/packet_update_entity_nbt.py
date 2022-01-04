"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketUpdateEntityNbt(Packet):
	__slots__ = ( 'id', 'tag', 'entityId' )
	
	tag : bytes
	entityId : int

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 73
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', VarInt ), ( 'tag', NBTTag ) ]
	}
