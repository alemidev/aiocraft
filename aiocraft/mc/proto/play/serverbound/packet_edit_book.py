"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketEditBook(Packet):
	__slots__ = ( 'id', 'hand', 'new_book', 'pages', 'signing', 'title' )
	
	hand : int
	new_book : Item
	pages : list
	signing : bool
	title : tuple

	def __init__(self, proto:int,
		hand:int=None,
		new_book:Item=None,
		pages:list=None,
		signing:bool=None,
		title:tuple=None,
		**kwargs
	):
		super().__init__(proto,
			hand=hand,
			new_book=new_book,
			pages=pages,
			signing=signing,
			title=title
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		393 : 11,
		401 : 11,
		402 : 11,
		403 : 11,
		404 : 11,
		477 : 12,
		480 : 12,
		490 : 12,
		498 : 12,
		573 : 12,
		575 : 12,
		578 : 12,
		709 : 12,
		734 : 12,
		735 : 12,
		736 : 12,
		751 : 12,
		755 : 11,
		756 : 11,
		757 : 11
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'new_book', Slot ), ( 'signing', Boolean ) ],
		401 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		402 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		403 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		404 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		477 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		480 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		490 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		498 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		573 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		575 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		578 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		709 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		734 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		735 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		736 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		751 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		755 : [ ( 'new_book', Slot ), ( 'signing', Boolean ), ( 'hand', VarInt ) ],
		756 : [ ( 'hand', VarInt ), ( 'pages', ArrayType(String, VarInt, ) ), ( 'title', OptionalType(String, ) ) ],
		757 : [ ( 'hand', VarInt ), ( 'pages', ArrayType(String, VarInt, ) ), ( 'title', OptionalType(String, ) ) ]
	}
