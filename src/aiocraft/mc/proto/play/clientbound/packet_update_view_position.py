"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketUpdateViewPosition(Packet):
	__slots__ = ( 'id', 'chunkX', 'chunkZ' )
	
	chunkX : int
	chunkZ : int

	def __init__(self, proto:int,
		chunkX:int=None,
		chunkZ:int=None,
		**kwargs
	):
		super().__init__(proto,
			chunkX=chunkX,
			chunkZ=chunkZ
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		477 : 64,
		480 : 64,
		490 : 64,
		498 : 64,
		573 : 65,
		575 : 65,
		578 : 65,
		709 : 65,
		734 : 64,
		735 : 64,
		736 : 64,
		751 : 64,
		755 : 73,
		756 : 73,
		757 : 73
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		477 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		480 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		490 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		498 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		573 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		575 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		578 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		709 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		734 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		735 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		736 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		751 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		755 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		756 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ],
		757 : [ ( 'chunkX', VarInt ), ( 'chunkZ', VarInt ) ]
	}