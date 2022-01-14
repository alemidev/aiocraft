"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketExperience(Packet):
	__slots__ = ( 'id', 'experienceBar', 'level', 'totalExperience' )
	
	experienceBar : float
	level : int
	totalExperience : int

	def __init__(self, proto:int,
		experienceBar:float=None,
		level:int=None,
		totalExperience:int=None
	):
		super().__init__(proto,
			experienceBar=experienceBar,
			level=level,
			totalExperience=totalExperience
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 31,
		76 : 61,
		107 : 61,
		108 : 61,
		109 : 61,
		110 : 61,
		201 : 61,
		210 : 61,
		304 : 61,
		315 : 61,
		321 : 63,
		327 : 63,
		331 : 63,
		335 : 63,
		338 : 64,
		340 : 64,
		351 : 65,
		393 : 67,
		401 : 67,
		402 : 67,
		403 : 67,
		404 : 67,
		477 : 71,
		480 : 71,
		490 : 71,
		498 : 71,
		573 : 72,
		575 : 72,
		578 : 72,
		709 : 73,
		734 : 72,
		735 : 72,
		736 : 72,
		751 : 72,
		755 : 81,
		756 : 81,
		757 : 81
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		76 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		107 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		108 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		109 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		110 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		201 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		210 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		304 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		315 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		321 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		327 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		331 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		335 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		338 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		340 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		351 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		393 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		401 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		402 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		403 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		404 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		477 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		480 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		490 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		498 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		573 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		575 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		578 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		709 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		734 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		735 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		736 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		751 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		755 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		756 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ],
		757 : [ ( 'experienceBar', Float ), ( 'level', VarInt ), ( 'totalExperience', VarInt ) ]
	}
