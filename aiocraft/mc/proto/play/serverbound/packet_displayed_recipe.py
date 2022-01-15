"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketDisplayedRecipe(Packet):
	__slots__ = ( 'id', 'recipeId' )
	
	recipeId : str

	def __init__(self, proto:int,
		recipeId:str=None,
		**kwargs
	):
		super().__init__(proto,
			recipeId=recipeId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		751 : 31,
		755 : 31,
		756 : 31,
		757 : 31
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		751 : [ ( 'recipeId', String ) ],
		755 : [ ( 'recipeId', String ) ],
		756 : [ ( 'recipeId', String ) ],
		757 : [ ( 'recipeId', String ) ]
	}
