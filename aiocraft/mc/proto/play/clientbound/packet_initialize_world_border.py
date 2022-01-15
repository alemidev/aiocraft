"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketInitializeWorldBorder(Packet):
	__slots__ = ( 'id', 'newDiameter', 'oldDiameter', 'portalTeleportBoundary', 'speed', 'warningBlocks', 'warningTime', 'x', 'z' )
	
	newDiameter : float
	oldDiameter : float
	portalTeleportBoundary : int
	speed : int
	warningBlocks : int
	warningTime : int
	x : float
	z : float

	def __init__(self, proto:int,
		newDiameter:float=None,
		oldDiameter:float=None,
		portalTeleportBoundary:int=None,
		speed:int=None,
		warningBlocks:int=None,
		warningTime:int=None,
		x:float=None,
		z:float=None,
		**kwargs
	):
		super().__init__(proto,
			newDiameter=newDiameter,
			oldDiameter=oldDiameter,
			portalTeleportBoundary=portalTeleportBoundary,
			speed=speed,
			warningBlocks=warningBlocks,
			warningTime=warningTime,
			x=x,
			z=z
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		755 : 32,
		756 : 32,
		757 : 32
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		755 : [ ( 'x', Double ), ( 'z', Double ), ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarInt ), ( 'portalTeleportBoundary', VarInt ), ( 'warningBlocks', VarInt ), ( 'warningTime', VarInt ) ],
		756 : [ ( 'x', Double ), ( 'z', Double ), ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarInt ), ( 'portalTeleportBoundary', VarInt ), ( 'warningBlocks', VarInt ), ( 'warningTime', VarInt ) ],
		757 : [ ( 'x', Double ), ( 'z', Double ), ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarInt ), ( 'portalTeleportBoundary', VarInt ), ( 'warningBlocks', VarInt ), ( 'warningTime', VarInt ) ]
	}