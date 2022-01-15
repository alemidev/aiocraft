"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketTabComplete(Packet):
	__slots__ = ( 'id', 'assumeCommand', 'block', 'lookedAtBlock', 'text', 'transactionId' )
	
	assumeCommand : bool
	block : tuple
	lookedAtBlock : tuple
	text : str
	transactionId : int

	def __init__(self, proto:int,
		assumeCommand:bool=None,
		block:tuple=None,
		lookedAtBlock:tuple=None,
		text:str=None,
		transactionId:int=None,
		**kwargs
	):
		super().__init__(proto,
			assumeCommand=assumeCommand,
			block=block,
			lookedAtBlock=lookedAtBlock,
			text=text,
			transactionId=transactionId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 20,
		76 : 0,
		107 : 1,
		108 : 1,
		109 : 1,
		110 : 1,
		201 : 1,
		210 : 1,
		304 : 1,
		315 : 1,
		321 : 2,
		327 : 2,
		331 : 2,
		335 : 2,
		338 : 1,
		340 : 1,
		351 : 4,
		393 : 5,
		401 : 5,
		402 : 5,
		403 : 5,
		404 : 5,
		477 : 6,
		480 : 6,
		490 : 6,
		498 : 6,
		573 : 6,
		575 : 6,
		578 : 6,
		709 : 6,
		734 : 6,
		735 : 6,
		736 : 6,
		751 : 6,
		755 : 6,
		756 : 6,
		757 : 6
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'text', String ), ( 'block', OptionalType(Position, ) ) ],
		76 : [ ( 'text', String ), ( 'block', OptionalType(Position, ) ) ],
		107 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		108 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		109 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		110 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		201 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		210 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		304 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		315 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		321 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		327 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		331 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		335 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		338 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		340 : [ ( 'text', String ), ( 'assumeCommand', Boolean ), ( 'lookedAtBlock', OptionalType(Position, ) ) ],
		351 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		393 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		401 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		402 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		403 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		404 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		477 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		480 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		490 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		498 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		573 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		575 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		578 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		709 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		734 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		735 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		736 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		751 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		755 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		756 : [ ( 'transactionId', VarInt ), ( 'text', String ) ],
		757 : [ ( 'transactionId', VarInt ), ( 'text', String ) ]
	}
