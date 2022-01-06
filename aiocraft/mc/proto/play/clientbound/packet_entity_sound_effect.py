"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketEntitySoundEffect(Packet):
	__slots__ = ( 'id', 'entityId', 'pitch', 'soundCategory', 'soundId', 'volume' )
	
	entityId : int
	pitch : float
	soundCategory : int
	soundId : int
	volume : float

	def __init__(self, proto:int,
		entityId:int=None,
		pitch:float=None,
		soundCategory:int=None,
		soundId:int=None,
		volume:float=None
	):
		super().__init__(proto,
			entityId=entityId,
			pitch=pitch,
			soundCategory=soundCategory,
			soundId=soundId,
			volume=volume
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		477 : 80,
		480 : 80,
		490 : 80,
		498 : 80,
		573 : 81,
		575 : 81,
		578 : 81,
		709 : 81,
		734 : 80,
		735 : 80,
		736 : 80,
		751 : 80,
		755 : 91,
		756 : 91,
		757 : 92
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		477 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		480 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		490 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		498 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		573 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		575 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		578 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		709 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		734 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		735 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		736 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		751 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		755 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		756 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ],
		757 : [ ( 'soundId', VarInt ), ( 'soundCategory', VarInt ), ( 'entityId', VarInt ), ( 'volume', Float ), ( 'pitch', Float ) ]
	}
