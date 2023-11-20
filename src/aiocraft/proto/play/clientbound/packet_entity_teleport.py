"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketEntityTeleport(Packet):
	__slots__ = ( 'id', 'entityId', 'onGround', 'pitch', 'x', 'y', 'yaw', 'z' )
	
	entityId : int
	onGround : bool
	pitch : int
	x : Union[float,int]
	y : Union[float,int]
	yaw : int
	z : Union[float,int]

	def __init__(self, 
		entityId:int | None = None,
		onGround:bool | None = None,
		pitch:int | None = None,
		x:Union[float,int] | None = None,
		y:Union[float,int] | None = None,
		yaw:int | None = None,
		z:Union[float,int] | None = None,
		**kwargs
	):
		super().__init__(
			entityId=entityId,
			onGround=onGround,
			pitch=pitch,
			x=x,
			y=y,
			yaw=yaw,
			z=z
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 24,
		76 : 72,
		107 : 74,
		108 : 74,
		109 : 74,
		110 : 73,
		201 : 73,
		210 : 73,
		304 : 73,
		315 : 73,
		321 : 75,
		327 : 75,
		331 : 75,
		335 : 75,
		338 : 76,
		340 : 76,
		351 : 78,
		393 : 80,
		401 : 80,
		402 : 80,
		403 : 80,
		404 : 80,
		477 : 86,
		480 : 86,
		490 : 86,
		498 : 86,
		573 : 87,
		575 : 87,
		578 : 87,
		709 : 87,
		734 : 86,
		735 : 86,
		736 : 86,
		751 : 86,
		755 : 97,
		756 : 97,
		757 : 98,
		758 : 98,
		759 : 99,
		760 : 102,
		761 : 100
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'entityId', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		76 : [ ( 'entityId', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		107 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		108 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		109 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		110 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		201 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		210 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		304 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		315 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		321 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		327 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		331 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		335 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		338 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		340 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		351 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		393 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		401 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		402 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		403 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		404 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		477 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		480 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		490 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		498 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		573 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		575 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		578 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		709 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		734 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		735 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		736 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		751 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		755 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		756 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		757 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		758 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		759 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		760 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ],
		761 : [ ( 'entityId', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Byte ), ( 'pitch', Byte ), ( 'onGround', Boolean ) ]
	}