"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketSuccess(Packet):
	__slots__ = ( 'id', 'username', 'uuid' )
	
	username : str
	uuid : str

	def __init__(self, proto:int,
		username:str=None,
		uuid:str=None,
		**kwargs
	):
		super().__init__(proto,
			username=username,
			uuid=uuid
		)

	_state : int = 2

	_ids : Dict[int, int] = {
		47 : 2,
		76 : 2,
		107 : 2,
		108 : 2,
		109 : 2,
		110 : 2,
		201 : 2,
		210 : 2,
		304 : 2,
		315 : 2,
		321 : 2,
		327 : 2,
		331 : 2,
		335 : 2,
		338 : 2,
		340 : 2,
		351 : 2,
		393 : 2,
		401 : 2,
		402 : 2,
		403 : 2,
		404 : 2,
		477 : 2,
		480 : 2,
		490 : 2,
		498 : 2,
		573 : 2,
		575 : 2,
		578 : 2,
		709 : 2,
		734 : 2,
		735 : 2,
		736 : 2,
		751 : 2,
		755 : 2,
		756 : 2,
		757 : 2
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'uuid', String ), ( 'username', String ) ],
		76 : [ ( 'uuid', String ), ( 'username', String ) ],
		107 : [ ( 'uuid', String ), ( 'username', String ) ],
		108 : [ ( 'uuid', String ), ( 'username', String ) ],
		109 : [ ( 'uuid', String ), ( 'username', String ) ],
		110 : [ ( 'uuid', String ), ( 'username', String ) ],
		201 : [ ( 'uuid', String ), ( 'username', String ) ],
		210 : [ ( 'uuid', String ), ( 'username', String ) ],
		304 : [ ( 'uuid', String ), ( 'username', String ) ],
		315 : [ ( 'uuid', String ), ( 'username', String ) ],
		321 : [ ( 'uuid', String ), ( 'username', String ) ],
		327 : [ ( 'uuid', String ), ( 'username', String ) ],
		331 : [ ( 'uuid', String ), ( 'username', String ) ],
		335 : [ ( 'uuid', String ), ( 'username', String ) ],
		338 : [ ( 'uuid', String ), ( 'username', String ) ],
		340 : [ ( 'uuid', String ), ( 'username', String ) ],
		351 : [ ( 'uuid', String ), ( 'username', String ) ],
		393 : [ ( 'uuid', String ), ( 'username', String ) ],
		401 : [ ( 'uuid', String ), ( 'username', String ) ],
		402 : [ ( 'uuid', String ), ( 'username', String ) ],
		403 : [ ( 'uuid', String ), ( 'username', String ) ],
		404 : [ ( 'uuid', String ), ( 'username', String ) ],
		477 : [ ( 'uuid', String ), ( 'username', String ) ],
		480 : [ ( 'uuid', String ), ( 'username', String ) ],
		490 : [ ( 'uuid', String ), ( 'username', String ) ],
		498 : [ ( 'uuid', String ), ( 'username', String ) ],
		573 : [ ( 'uuid', String ), ( 'username', String ) ],
		575 : [ ( 'uuid', String ), ( 'username', String ) ],
		578 : [ ( 'uuid', String ), ( 'username', String ) ],
		709 : [ ( 'uuid', UUID ), ( 'username', String ) ],
		734 : [ ( 'uuid', UUID ), ( 'username', String ) ],
		735 : [ ( 'uuid', UUID ), ( 'username', String ) ],
		736 : [ ( 'uuid', UUID ), ( 'username', String ) ],
		751 : [ ( 'uuid', UUID ), ( 'username', String ) ],
		755 : [ ( 'uuid', UUID ), ( 'username', String ) ],
		756 : [ ( 'uuid', UUID ), ( 'username', String ) ],
		757 : [ ( 'uuid', UUID ), ( 'username', String ) ]
	}