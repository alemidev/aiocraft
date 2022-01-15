"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketEnterCombatEvent(Packet):
	__slots__ = ( 'id' )
	
	

	def __init__(self, proto:int,
		**kwargs
	):
		super().__init__(proto,
			
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		755 : 52,
		756 : 52,
		757 : 52
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		755 : [  ],
		756 : [  ],
		757 : [  ]
	}
