"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketPrepareCraftingGrid(Packet):
	__slots__ = ( 'id', 'actionNumber', 'prepareEntry', 'returnEntry', 'windowId' )
	
	actionNumber : int
	prepareEntry : list
	returnEntry : list
	windowId : int

	def __init__(self, proto:int,
		actionNumber:int=None,
		prepareEntry:list=None,
		returnEntry:list=None,
		windowId:int=None,
		**kwargs
	):
		super().__init__(proto,
			actionNumber=actionNumber,
			prepareEntry=prepareEntry,
			returnEntry=returnEntry,
			windowId=windowId
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		321 : 1,
		327 : 1,
		331 : 1,
		335 : 1
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		321 : [ ( 'windowId', Byte ), ( 'actionNumber', UnsignedShort ), ( 'returnEntry', ArrayType(StructType(( 'item', Slot ), ( 'craftingSlot', Byte ), ( 'playerSlot', Byte ), ), Byte, ) ), ( 'prepareEntry', ArrayType(StructType(( 'item', Slot ), ( 'craftingSlot', Byte ), ( 'playerSlot', Byte ), ), Byte, ) ) ],
		327 : [ ( 'windowId', Byte ), ( 'actionNumber', UnsignedShort ), ( 'returnEntry', ArrayType(StructType(( 'item', Slot ), ( 'craftingSlot', Byte ), ( 'playerSlot', Byte ), ), UnsignedShort, ) ), ( 'prepareEntry', ArrayType(StructType(( 'item', Slot ), ( 'craftingSlot', Byte ), ( 'playerSlot', Byte ), ), UnsignedShort, ) ) ],
		331 : [ ( 'windowId', Byte ), ( 'actionNumber', UnsignedShort ), ( 'returnEntry', ArrayType(StructType(( 'item', Slot ), ( 'craftingSlot', Byte ), ( 'playerSlot', Byte ), ), UnsignedShort, ) ), ( 'prepareEntry', ArrayType(StructType(( 'item', Slot ), ( 'craftingSlot', Byte ), ( 'playerSlot', Byte ), ), UnsignedShort, ) ) ],
		335 : [ ( 'windowId', Byte ), ( 'actionNumber', UnsignedShort ), ( 'returnEntry', ArrayType(StructType(( 'item', Slot ), ( 'craftingSlot', Byte ), ( 'playerSlot', Byte ), ), UnsignedShort, ) ), ( 'prepareEntry', ArrayType(StructType(( 'item', Slot ), ( 'craftingSlot', Byte ), ( 'playerSlot', Byte ), ), UnsignedShort, ) ) ]
	}
