"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketPingStart(Packet):
	__slots__ = ( 'id' )
	
	

	def __init__(self, proto:int,
		**kwargs
	):
		super().__init__(proto,
			
		)

	_state : int = 1

	_ids : Dict[int, int] = {
		47 : 0,
		76 : 0,
		107 : 0,
		108 : 0,
		109 : 0,
		110 : 0,
		201 : 0,
		210 : 0,
		304 : 0,
		315 : 0,
		321 : 0,
		327 : 0,
		331 : 0,
		335 : 0,
		338 : 0,
		340 : 0,
		351 : 0,
		393 : 0,
		401 : 0,
		402 : 0,
		403 : 0,
		404 : 0,
		477 : 0,
		480 : 0,
		490 : 0,
		498 : 0,
		573 : 0,
		575 : 0,
		578 : 0,
		709 : 0,
		734 : 0,
		735 : 0,
		736 : 0,
		751 : 0,
		755 : 0,
		756 : 0,
		757 : 0
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [  ],
		76 : [  ],
		107 : [  ],
		108 : [  ],
		109 : [  ],
		110 : [  ],
		201 : [  ],
		210 : [  ],
		304 : [  ],
		315 : [  ],
		321 : [  ],
		327 : [  ],
		331 : [  ],
		335 : [  ],
		338 : [  ],
		340 : [  ],
		351 : [  ],
		393 : [  ],
		401 : [  ],
		402 : [  ],
		403 : [  ],
		404 : [  ],
		477 : [  ],
		480 : [  ],
		490 : [  ],
		498 : [  ],
		573 : [  ],
		575 : [  ],
		578 : [  ],
		709 : [  ],
		734 : [  ],
		735 : [  ],
		736 : [  ],
		751 : [  ],
		755 : [  ],
		756 : [  ],
		757 : [  ]
	}