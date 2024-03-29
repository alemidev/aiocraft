"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketPlayerRemove(Packet):
	__slots__ = ( 'id', 'players' )
	
	players : list

	def __init__(self, 
		players:list | None = None,
		**kwargs
	):
		super().__init__(
			players=players
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		761 : 53
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		761 : [ ( 'players', ArrayType(UUID, VarInt, ) ) ]
	}
