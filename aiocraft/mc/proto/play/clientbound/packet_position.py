"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketPosition(Packet):
	__slots__ = ( 'id', 'dismountVehicle', 'flags', 'pitch', 'teleportId', 'x', 'y', 'yaw', 'z' )
	
	dismountVehicle : bool
	flags : int
	pitch : float
	teleportId : int
	x : float
	y : float
	yaw : float
	z : float

	def __init__(self, proto:int,
		dismountVehicle:bool=None,
		flags:int=None,
		pitch:float=None,
		teleportId:int=None,
		x:float=None,
		y:float=None,
		yaw:float=None,
		z:float=None
	):
		super().__init__(proto,
			dismountVehicle=dismountVehicle,
			flags=flags,
			pitch=pitch,
			teleportId=teleportId,
			x=x,
			y=y,
			yaw=yaw,
			z=z
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 8,
		76 : 46,
		107 : 46,
		108 : 46,
		109 : 46,
		110 : 46,
		201 : 46,
		210 : 46,
		304 : 46,
		315 : 46,
		321 : 47,
		327 : 47,
		331 : 47,
		335 : 46,
		338 : 47,
		340 : 47,
		351 : 48,
		393 : 50,
		401 : 50,
		402 : 50,
		403 : 50,
		404 : 50,
		477 : 53,
		480 : 53,
		490 : 53,
		498 : 53,
		573 : 54,
		575 : 54,
		578 : 54,
		709 : 54,
		734 : 53,
		735 : 53,
		736 : 53,
		751 : 52,
		755 : 56,
		756 : 56,
		757 : 56
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ) ],
		76 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ) ],
		107 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		108 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		109 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		110 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		201 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		210 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		304 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		315 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		321 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		327 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		331 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		335 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		338 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		340 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		351 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		393 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		401 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		402 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		403 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		404 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		477 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		480 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		490 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		498 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		573 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		575 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		578 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		709 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		734 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		735 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		736 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		751 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ) ],
		755 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ), ( 'dismountVehicle', Boolean ) ],
		756 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ), ( 'dismountVehicle', Boolean ) ],
		757 : [ ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'yaw', Float ), ( 'pitch', Float ), ( 'flags', Byte ), ( 'teleportId', VarInt ), ( 'dismountVehicle', Boolean ) ]
	}
