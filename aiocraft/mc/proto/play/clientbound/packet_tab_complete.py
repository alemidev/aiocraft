"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketTabComplete(Packet):
	__slots__ = ( 'id', 'length', 'matches', 'start', 'transactionId' )
	
	length : int
	matches : list
	start : int
	transactionId : int

	def __init__(self, proto:int,
		length:int=None,
		matches:list=None,
		start:int=None,
		transactionId:int=None,
		**kwargs
	):
		super().__init__(proto,
			length=length,
			matches=matches,
			start=start,
			transactionId=transactionId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 58,
		76 : 14,
		107 : 14,
		108 : 14,
		109 : 14,
		110 : 14,
		201 : 14,
		210 : 14,
		304 : 14,
		315 : 14,
		321 : 15,
		327 : 15,
		331 : 15,
		335 : 14,
		338 : 14,
		340 : 14,
		351 : 16,
		393 : 16,
		401 : 16,
		402 : 16,
		403 : 16,
		404 : 16,
		477 : 16,
		480 : 16,
		490 : 16,
		498 : 16,
		573 : 17,
		575 : 17,
		578 : 17,
		709 : 17,
		734 : 16,
		735 : 16,
		736 : 16,
		751 : 15,
		755 : 17,
		756 : 17,
		757 : 17
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		76 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		107 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		108 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		109 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		110 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		201 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		210 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		304 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		315 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		321 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		327 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		331 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		335 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		338 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		340 : [ ( 'matches', ArrayType(String, VarInt, ) ) ],
		351 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(String, VarInt, ) ) ],
		393 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		401 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		402 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		403 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		404 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		477 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		480 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		490 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		498 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		573 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		575 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		578 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		709 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		734 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		735 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		736 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		751 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		755 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		756 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ],
		757 : [ ( 'transactionId', VarInt ), ( 'start', VarInt ), ( 'length', VarInt ), ( 'matches', ArrayType(StructType(( 'match', String ), ( 'tooltip', OptionalType(String, ) ), ), VarInt, ) ) ]
	}
