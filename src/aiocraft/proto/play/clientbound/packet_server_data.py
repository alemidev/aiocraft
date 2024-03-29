"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketServerData(Packet):
	__slots__ = ( 'id', 'enforcesSecureChat', 'icon', 'motd', 'previewsChat' )
	
	enforcesSecureChat : bool
	icon : tuple
	motd : tuple
	previewsChat : bool

	def __init__(self, 
		enforcesSecureChat:bool | None = None,
		icon:tuple | None = None,
		motd:tuple | None = None,
		previewsChat:bool | None = None,
		**kwargs
	):
		super().__init__(
			enforcesSecureChat=enforcesSecureChat,
			icon=icon,
			motd=motd,
			previewsChat=previewsChat
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		759 : 63,
		760 : 66,
		761 : 65
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		759 : [ ( 'motd', OptionalType(String, ) ), ( 'icon', OptionalType(String, ) ), ( 'previewsChat', Boolean ) ],
		760 : [ ( 'motd', OptionalType(String, ) ), ( 'icon', OptionalType(String, ) ), ( 'previewsChat', Boolean ), ( 'enforcesSecureChat', Boolean ) ],
		761 : [ ( 'motd', OptionalType(String, ) ), ( 'icon', OptionalType(String, ) ), ( 'enforcesSecureChat', Boolean ) ]
	}
