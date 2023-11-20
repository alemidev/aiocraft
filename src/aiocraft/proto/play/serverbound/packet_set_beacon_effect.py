"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketSetBeaconEffect(Packet):
	__slots__ = ( 'id', 'primary_effect', 'secondary_effect' )
	
	primary_effect : Union[int,tuple]
	secondary_effect : Union[int,tuple]

	def __init__(self, 
		primary_effect:Union[int,tuple] | None = None,
		secondary_effect:Union[int,tuple] | None = None,
		**kwargs
	):
		super().__init__(
			primary_effect=primary_effect,
			secondary_effect=secondary_effect
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		393 : 32,
		401 : 32,
		402 : 32,
		403 : 32,
		404 : 32,
		477 : 34,
		480 : 34,
		490 : 34,
		498 : 34,
		573 : 34,
		575 : 34,
		578 : 34,
		709 : 34,
		734 : 35,
		735 : 35,
		736 : 35,
		751 : 36,
		755 : 36,
		756 : 36,
		757 : 36,
		758 : 36,
		759 : 38,
		760 : 39,
		761 : 39
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		401 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		402 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		403 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		404 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		477 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		480 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		490 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		498 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		573 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		575 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		578 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		709 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		734 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		735 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		736 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		751 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		755 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		756 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		757 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		758 : [ ( 'primary_effect', VarInt ), ( 'secondary_effect', VarInt ) ],
		759 : [ ( 'primary_effect', OptionalType(VarInt, ) ), ( 'secondary_effect', OptionalType(VarInt, ) ) ],
		760 : [ ( 'primary_effect', OptionalType(VarInt, ) ), ( 'secondary_effect', OptionalType(VarInt, ) ) ],
		761 : [ ( 'primary_effect', OptionalType(VarInt, ) ), ( 'secondary_effect', OptionalType(VarInt, ) ) ]
	}