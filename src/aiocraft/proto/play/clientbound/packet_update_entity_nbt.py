"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketUpdateEntityNbt(Packet):
	__slots__ = ( 'id', 'entityId', 'tag' )
	
	entityId : int
	tag : dict

	def __init__(self, 
		entityId:int | None = None,
		tag:dict | None = None,
		**kwargs
	):
		super().__init__(
			entityId=entityId,
			tag=tag
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 73
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', VarInt ), ( 'tag', NBTTag ) ]
	}
