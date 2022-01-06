"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketWorldBorderLerpSize(Packet):
	__slots__ = ( 'id', 'newDiameter', 'oldDiameter', 'speed' )
	
	newDiameter : float
	oldDiameter : float
	speed : int

	def __init__(self, proto:int,
		newDiameter:float=None,
		oldDiameter:float=None,
		speed:int=None
	):
		super().__init__(proto,
			newDiameter=newDiameter,
			oldDiameter=oldDiameter,
			speed=speed
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		755 : 67,
		756 : 67,
		757 : 67
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		755 : [ ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarInt ) ],
		756 : [ ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarInt ) ],
		757 : [ ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarInt ) ]
	}
