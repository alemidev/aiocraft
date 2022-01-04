"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketUpdateStructureBlock(Packet):
	__slots__ = ( 'id', 'name', 'size_x', 'size_z', 'offset_z', 'rotation', 'offset_y', 'size_y', 'flags', 'offset_x', 'mirror', 'seed', 'action', 'metadata', 'integrity', 'location', 'mode' )
	
	name : str
	size_x : int
	size_z : int
	offset_z : int
	rotation : int
	offset_y : int
	size_y : int
	flags : int
	offset_x : int
	mirror : int
	seed : int
	action : int
	metadata : str
	integrity : float
	location : tuple
	mode : int

	_state : int = 3

	_ids : Dict[int, int] = {
		393 : 37,
		401 : 37,
		402 : 37,
		403 : 37,
		404 : 37,
		477 : 40,
		480 : 40,
		490 : 40,
		498 : 40,
		573 : 40,
		575 : 40,
		578 : 40,
		709 : 40,
		734 : 41,
		735 : 41,
		736 : 41,
		751 : 42,
		755 : 42,
		756 : 42,
		757 : 42,
		1073741839 : 42
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		401 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		402 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		403 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		404 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		477 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		480 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		490 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		498 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		573 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		575 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		578 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		709 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		734 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		735 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		736 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		751 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		755 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		756 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		757 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		1073741839 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ]
	}
