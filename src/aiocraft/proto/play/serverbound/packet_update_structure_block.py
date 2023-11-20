"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketUpdateStructureBlock(Packet):
	__slots__ = ( 'id', 'action', 'flags', 'integrity', 'location', 'metadata', 'mirror', 'mode', 'name', 'offset_x', 'offset_y', 'offset_z', 'rotation', 'seed', 'size_x', 'size_y', 'size_z' )
	
	action : int
	flags : int
	integrity : float
	location : tuple
	metadata : str
	mirror : int
	mode : int
	name : str
	offset_x : int
	offset_y : int
	offset_z : int
	rotation : int
	seed : int
	size_x : int
	size_y : int
	size_z : int

	def __init__(self, 
		action:int | None = None,
		flags:int | None = None,
		integrity:float | None = None,
		location:tuple | None = None,
		metadata:str | None = None,
		mirror:int | None = None,
		mode:int | None = None,
		name:str | None = None,
		offset_x:int | None = None,
		offset_y:int | None = None,
		offset_z:int | None = None,
		rotation:int | None = None,
		seed:int | None = None,
		size_x:int | None = None,
		size_y:int | None = None,
		size_z:int | None = None,
		**kwargs
	):
		super().__init__(
			action=action,
			flags=flags,
			integrity=integrity,
			location=location,
			metadata=metadata,
			mirror=mirror,
			mode=mode,
			name=name,
			offset_x=offset_x,
			offset_y=offset_y,
			offset_z=offset_z,
			rotation=rotation,
			seed=seed,
			size_x=size_x,
			size_y=size_y,
			size_z=size_z
		)

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
		758 : 42,
		759 : 44,
		760 : 45,
		761 : 45
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		401 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		402 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		403 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		404 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		477 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		480 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		490 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		498 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		573 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		575 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		578 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		709 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		734 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		735 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		736 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		751 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		755 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		756 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		757 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		758 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarLong ), ( 'flags', Byte ) ],
		759 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		760 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ],
		761 : [ ( 'location', Position ), ( 'action', VarInt ), ( 'mode', VarInt ), ( 'name', String ), ( 'offset_x', Byte ), ( 'offset_y', Byte ), ( 'offset_z', Byte ), ( 'size_x', Byte ), ( 'size_y', Byte ), ( 'size_z', Byte ), ( 'mirror', VarInt ), ( 'rotation', VarInt ), ( 'metadata', String ), ( 'integrity', Float ), ( 'seed', VarInt ), ( 'flags', Byte ) ]
	}