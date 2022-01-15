"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketKeepAlive(Packet):
	__slots__ = ( 'id', 'keepAliveId' )
	
	keepAliveId : int

	def __init__(self, proto:int,
		keepAliveId:int=None,
		**kwargs
	):
		super().__init__(proto,
			keepAliveId=keepAliveId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 0,
		76 : 31,
		107 : 31,
		108 : 31,
		109 : 31,
		110 : 31,
		201 : 31,
		210 : 31,
		304 : 31,
		315 : 31,
		321 : 32,
		327 : 32,
		331 : 32,
		335 : 31,
		338 : 31,
		340 : 31,
		351 : 32,
		393 : 33,
		401 : 33,
		402 : 33,
		403 : 33,
		404 : 33,
		477 : 32,
		480 : 32,
		490 : 32,
		498 : 32,
		573 : 33,
		575 : 33,
		578 : 33,
		709 : 33,
		734 : 32,
		735 : 32,
		736 : 32,
		751 : 31,
		755 : 33,
		756 : 33,
		757 : 33
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'keepAliveId', VarInt ) ],
		76 : [ ( 'keepAliveId', VarInt ) ],
		107 : [ ( 'keepAliveId', VarInt ) ],
		108 : [ ( 'keepAliveId', VarInt ) ],
		109 : [ ( 'keepAliveId', VarInt ) ],
		110 : [ ( 'keepAliveId', VarInt ) ],
		201 : [ ( 'keepAliveId', VarInt ) ],
		210 : [ ( 'keepAliveId', VarInt ) ],
		304 : [ ( 'keepAliveId', VarInt ) ],
		315 : [ ( 'keepAliveId', VarInt ) ],
		321 : [ ( 'keepAliveId', VarInt ) ],
		327 : [ ( 'keepAliveId', VarInt ) ],
		331 : [ ( 'keepAliveId', VarInt ) ],
		335 : [ ( 'keepAliveId', VarInt ) ],
		338 : [ ( 'keepAliveId', VarInt ) ],
		340 : [ ( 'keepAliveId', Long ) ],
		351 : [ ( 'keepAliveId', Long ) ],
		393 : [ ( 'keepAliveId', Long ) ],
		401 : [ ( 'keepAliveId', Long ) ],
		402 : [ ( 'keepAliveId', Long ) ],
		403 : [ ( 'keepAliveId', Long ) ],
		404 : [ ( 'keepAliveId', Long ) ],
		477 : [ ( 'keepAliveId', Long ) ],
		480 : [ ( 'keepAliveId', Long ) ],
		490 : [ ( 'keepAliveId', Long ) ],
		498 : [ ( 'keepAliveId', Long ) ],
		573 : [ ( 'keepAliveId', Long ) ],
		575 : [ ( 'keepAliveId', Long ) ],
		578 : [ ( 'keepAliveId', Long ) ],
		709 : [ ( 'keepAliveId', Long ) ],
		734 : [ ( 'keepAliveId', Long ) ],
		735 : [ ( 'keepAliveId', Long ) ],
		736 : [ ( 'keepAliveId', Long ) ],
		751 : [ ( 'keepAliveId', Long ) ],
		755 : [ ( 'keepAliveId', Long ) ],
		756 : [ ( 'keepAliveId', Long ) ],
		757 : [ ( 'keepAliveId', Long ) ]
	}
