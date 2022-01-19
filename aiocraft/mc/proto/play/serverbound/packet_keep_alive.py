"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
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
		76 : 10,
		107 : 11,
		108 : 11,
		109 : 11,
		110 : 11,
		201 : 11,
		210 : 11,
		304 : 11,
		315 : 11,
		321 : 12,
		327 : 12,
		331 : 12,
		335 : 12,
		338 : 11,
		340 : 11,
		351 : 11,
		393 : 14,
		401 : 14,
		402 : 14,
		403 : 14,
		404 : 14,
		477 : 15,
		480 : 15,
		490 : 15,
		498 : 15,
		573 : 15,
		575 : 15,
		578 : 15,
		709 : 15,
		734 : 16,
		735 : 16,
		736 : 16,
		751 : 16,
		755 : 15,
		756 : 15,
		757 : 15
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
