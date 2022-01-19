"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketSpawnEntityExperienceOrb(Packet):
	__slots__ = ( 'id', 'count', 'entityId', 'x', 'y', 'z' )
	
	count : int
	entityId : int
	x : Union[float,int]
	y : Union[float,int]
	z : Union[float,int]

	def __init__(self, proto:int,
		count:int=None,
		entityId:int=None,
		x:Union[float,int]=None,
		y:Union[float,int]=None,
		z:Union[float,int]=None,
		**kwargs
	):
		super().__init__(proto,
			count=count,
			entityId=entityId,
			x=x,
			y=y,
			z=z
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 17,
		76 : 1,
		107 : 1,
		108 : 1,
		109 : 1,
		110 : 1,
		201 : 1,
		210 : 1,
		304 : 1,
		315 : 1,
		321 : 1,
		327 : 1,
		331 : 1,
		335 : 1,
		338 : 1,
		340 : 1,
		351 : 1,
		393 : 1,
		401 : 1,
		402 : 1,
		403 : 1,
		404 : 1,
		477 : 1,
		480 : 1,
		490 : 1,
		498 : 1,
		573 : 1,
		575 : 1,
		578 : 1,
		709 : 1,
		734 : 1,
		735 : 1,
		736 : 1,
		751 : 1,
		755 : 1,
		756 : 1,
		757 : 1
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'count', Short ) ],
		76 : [ ( 'entityId', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'count', Short ) ],
		107 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		108 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		109 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		110 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		201 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		210 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		304 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		315 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		321 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		327 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		331 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		335 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		338 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		340 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		351 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		393 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		401 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		402 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		403 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		404 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		477 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		480 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		490 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		498 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		573 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		575 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		578 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		709 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		734 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		735 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		736 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		751 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		755 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		756 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ],
		757 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'count', Short ) ]
	}
