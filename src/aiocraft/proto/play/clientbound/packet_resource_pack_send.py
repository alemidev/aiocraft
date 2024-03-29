"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketResourcePackSend(Packet):
	__slots__ = ( 'id', 'forced', 'hash', 'promptMessage', 'url' )
	
	forced : bool
	hash : str
	promptMessage : tuple
	url : str

	def __init__(self, 
		forced:bool | None = None,
		hash:str | None = None,
		promptMessage:tuple | None = None,
		url:str | None = None,
		**kwargs
	):
		super().__init__(
			forced=forced,
			hash=hash,
			promptMessage=promptMessage,
			url=url
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 72,
		76 : 50,
		107 : 50,
		108 : 50,
		109 : 50,
		110 : 50,
		201 : 50,
		210 : 50,
		304 : 50,
		315 : 50,
		321 : 52,
		327 : 52,
		331 : 52,
		335 : 51,
		338 : 52,
		340 : 52,
		351 : 53,
		393 : 55,
		401 : 55,
		402 : 55,
		403 : 55,
		404 : 55,
		477 : 57,
		480 : 57,
		490 : 57,
		498 : 57,
		573 : 58,
		575 : 58,
		578 : 58,
		709 : 58,
		734 : 57,
		735 : 57,
		736 : 57,
		751 : 56,
		755 : 60,
		756 : 60,
		757 : 60,
		758 : 60,
		759 : 58,
		760 : 61,
		761 : 60
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'url', String ), ( 'hash', String ) ],
		76 : [ ( 'url', String ), ( 'hash', String ) ],
		107 : [ ( 'url', String ), ( 'hash', String ) ],
		108 : [ ( 'url', String ), ( 'hash', String ) ],
		109 : [ ( 'url', String ), ( 'hash', String ) ],
		110 : [ ( 'url', String ), ( 'hash', String ) ],
		201 : [ ( 'url', String ), ( 'hash', String ) ],
		210 : [ ( 'url', String ), ( 'hash', String ) ],
		304 : [ ( 'url', String ), ( 'hash', String ) ],
		315 : [ ( 'url', String ), ( 'hash', String ) ],
		321 : [ ( 'url', String ), ( 'hash', String ) ],
		327 : [ ( 'url', String ), ( 'hash', String ) ],
		331 : [ ( 'url', String ), ( 'hash', String ) ],
		335 : [ ( 'url', String ), ( 'hash', String ) ],
		338 : [ ( 'url', String ), ( 'hash', String ) ],
		340 : [ ( 'url', String ), ( 'hash', String ) ],
		351 : [ ( 'url', String ), ( 'hash', String ) ],
		393 : [ ( 'url', String ), ( 'hash', String ) ],
		401 : [ ( 'url', String ), ( 'hash', String ) ],
		402 : [ ( 'url', String ), ( 'hash', String ) ],
		403 : [ ( 'url', String ), ( 'hash', String ) ],
		404 : [ ( 'url', String ), ( 'hash', String ) ],
		477 : [ ( 'url', String ), ( 'hash', String ) ],
		480 : [ ( 'url', String ), ( 'hash', String ) ],
		490 : [ ( 'url', String ), ( 'hash', String ) ],
		498 : [ ( 'url', String ), ( 'hash', String ) ],
		573 : [ ( 'url', String ), ( 'hash', String ) ],
		575 : [ ( 'url', String ), ( 'hash', String ) ],
		578 : [ ( 'url', String ), ( 'hash', String ) ],
		709 : [ ( 'url', String ), ( 'hash', String ) ],
		734 : [ ( 'url', String ), ( 'hash', String ) ],
		735 : [ ( 'url', String ), ( 'hash', String ) ],
		736 : [ ( 'url', String ), ( 'hash', String ) ],
		751 : [ ( 'url', String ), ( 'hash', String ) ],
		755 : [ ( 'url', String ), ( 'hash', String ), ( 'forced', Boolean ), ( 'promptMessage', OptionalType(String, ) ) ],
		756 : [ ( 'url', String ), ( 'hash', String ), ( 'forced', Boolean ), ( 'promptMessage', OptionalType(String, ) ) ],
		757 : [ ( 'url', String ), ( 'hash', String ), ( 'forced', Boolean ), ( 'promptMessage', OptionalType(String, ) ) ],
		758 : [ ( 'url', String ), ( 'hash', String ), ( 'forced', Boolean ), ( 'promptMessage', OptionalType(String, ) ) ],
		759 : [ ( 'url', String ), ( 'hash', String ), ( 'forced', Boolean ), ( 'promptMessage', OptionalType(String, ) ) ],
		760 : [ ( 'url', String ), ( 'hash', String ), ( 'forced', Boolean ), ( 'promptMessage', OptionalType(String, ) ) ],
		761 : [ ( 'url', String ), ( 'hash', String ), ( 'forced', Boolean ), ( 'promptMessage', OptionalType(String, ) ) ]
	}
