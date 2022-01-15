"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketNamedSoundEffect(Packet):
	__slots__ = ( 'id', 'pitch', 'soundCategory', 'soundName', 'volume', 'x', 'y', 'z' )
	
	pitch : Union[int,float]
	soundCategory : int
	soundName : str
	volume : float
	x : int
	y : int
	z : int

	def __init__(self, proto:int,
		pitch:Union[int,float]=None,
		soundCategory:int=None,
		soundName:str=None,
		volume:float=None,
		x:int=None,
		y:int=None,
		z:int=None,
		**kwargs
	):
		super().__init__(proto,
			pitch=pitch,
			soundCategory=soundCategory,
			soundName=soundName,
			volume=volume,
			x=x,
			y=y,
			z=z
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 41,
		76 : 35,
		107 : 25,
		108 : 25,
		109 : 25,
		110 : 25,
		201 : 25,
		210 : 25,
		304 : 25,
		315 : 25,
		321 : 26,
		327 : 26,
		331 : 26,
		335 : 25,
		338 : 25,
		340 : 25,
		351 : 26,
		393 : 26,
		401 : 26,
		402 : 26,
		403 : 26,
		404 : 26,
		477 : 25,
		480 : 25,
		490 : 25,
		498 : 25,
		573 : 26,
		575 : 26,
		578 : 26,
		709 : 26,
		734 : 25,
		735 : 25,
		736 : 25,
		751 : 24,
		755 : 25,
		756 : 25,
		757 : 25
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'soundName', String ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Byte ) ],
		76 : [ ( 'soundName', String ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Byte ) ],
		107 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Byte ) ],
		108 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Byte ) ],
		109 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Byte ) ],
		110 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Byte ) ],
		201 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		210 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		304 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		315 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		321 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		327 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		331 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		335 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		338 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		340 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		351 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		393 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		401 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		402 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		403 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		404 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		477 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		480 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		490 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		498 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		573 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		575 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		578 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		709 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		734 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		735 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		736 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		751 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		755 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		756 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ],
		757 : [ ( 'soundName', String ), ( 'soundCategory', VarInt ), ( 'x', Int ), ( 'y', Int ), ( 'z', Int ), ( 'volume', Float ), ( 'pitch', Float ) ]
	}
