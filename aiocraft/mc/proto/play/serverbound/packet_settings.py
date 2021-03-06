"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketSettings(Packet):
	__slots__ = ( 'id', 'chatColors', 'chatFlags', 'disableTextFiltering', 'enableServerListing', 'enableTextFiltering', 'locale', 'mainHand', 'skinParts', 'viewDistance' )
	
	chatColors : bool
	chatFlags : int
	disableTextFiltering : bool
	enableServerListing : bool
	enableTextFiltering : bool
	locale : str
	mainHand : int
	skinParts : int
	viewDistance : int

	def __init__(self, proto:int,
		chatColors:bool=None,
		chatFlags:int=None,
		disableTextFiltering:bool=None,
		enableServerListing:bool=None,
		enableTextFiltering:bool=None,
		locale:str=None,
		mainHand:int=None,
		skinParts:int=None,
		viewDistance:int=None,
		**kwargs
	):
		super().__init__(proto,
			chatColors=chatColors,
			chatFlags=chatFlags,
			disableTextFiltering=disableTextFiltering,
			enableServerListing=enableServerListing,
			enableTextFiltering=enableTextFiltering,
			locale=locale,
			mainHand=mainHand,
			skinParts=skinParts,
			viewDistance=viewDistance
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 21,
		76 : 3,
		107 : 4,
		108 : 4,
		109 : 4,
		110 : 4,
		201 : 4,
		210 : 4,
		304 : 4,
		315 : 4,
		321 : 5,
		327 : 5,
		331 : 5,
		335 : 5,
		338 : 4,
		340 : 4,
		351 : 3,
		393 : 4,
		401 : 4,
		402 : 4,
		403 : 4,
		404 : 4,
		477 : 5,
		480 : 5,
		490 : 5,
		498 : 5,
		573 : 5,
		575 : 5,
		578 : 5,
		709 : 5,
		734 : 5,
		735 : 5,
		736 : 5,
		751 : 5,
		755 : 5,
		756 : 5,
		757 : 5
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', Byte ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ) ],
		76 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		107 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		108 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		109 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		110 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		201 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		210 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		304 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		315 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		321 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		327 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		331 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		335 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		338 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		340 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		351 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		393 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		401 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		402 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		403 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		404 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		477 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		480 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		490 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		498 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		573 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		575 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		578 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		709 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		734 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		735 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		736 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		751 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ) ],
		755 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ), ( 'disableTextFiltering', Boolean ) ],
		756 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ), ( 'disableTextFiltering', Boolean ) ],
		757 : [ ( 'locale', String ), ( 'viewDistance', Byte ), ( 'chatFlags', VarInt ), ( 'chatColors', Boolean ), ( 'skinParts', Byte ), ( 'mainHand', VarInt ), ( 'enableTextFiltering', Boolean ), ( 'enableServerListing', Boolean ) ]
	}
