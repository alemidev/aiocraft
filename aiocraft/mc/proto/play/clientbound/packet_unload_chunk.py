"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketUnloadChunk(Packet):
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
		76 : 28,
		107 : 29,
		108 : 29,
		109 : 29,
		110 : 29,
		201 : 29,
		210 : 29,
		304 : 29,
		315 : 29,
		321 : 30,
		327 : 30,
		331 : 30,
		335 : 29,
		338 : 29,
		340 : 29,
		351 : 30,
		393 : 31,
		401 : 31,
		402 : 31,
		403 : 31,
		404 : 31,
		477 : 29,
		480 : 29,
		490 : 29,
		498 : 29,
		573 : 30,
		575 : 30,
		578 : 30,
		709 : 30,
		734 : 29,
		735 : 29,
		736 : 29,
		751 : 28,
		755 : 29,
		756 : 29,
		757 : 29
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		76 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		107 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		108 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		109 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		110 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		201 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		210 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		304 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		315 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		321 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		327 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		331 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		335 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		338 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		340 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		351 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		393 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		401 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		402 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		403 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		404 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		477 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		480 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		490 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		498 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		573 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		575 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		578 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		709 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		734 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		735 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		736 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		751 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		755 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		756 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ],
		757 : [ ( 'chunkX', Int ), ( 'chunkZ', Int ) ]
	}
