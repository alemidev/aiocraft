"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketWorldBorderLerpSize(Packet):
	__slots__ = ( 'id', 'newDiameter', 'oldDiameter', 'speed' )
	
	newDiameter : float
	oldDiameter : float
	speed : int

	def __init__(self, 
		newDiameter:float | None = None,
		oldDiameter:float | None = None,
		speed:int | None = None,
		**kwargs
	):
		super().__init__(
			newDiameter=newDiameter,
			oldDiameter=oldDiameter,
			speed=speed
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		755 : 67,
		756 : 67,
		757 : 67,
		758 : 67,
		759 : 66,
		760 : 69,
		761 : 68
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		755 : [ ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarLong ) ],
		756 : [ ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarLong ) ],
		757 : [ ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarLong ) ],
		758 : [ ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarLong ) ],
		759 : [ ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarInt ) ],
		760 : [ ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarInt ) ],
		761 : [ ( 'oldDiameter', Double ), ( 'newDiameter', Double ), ( 'speed', VarInt ) ]
	}
