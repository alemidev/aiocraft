"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketBossBar(Packet):
	__slots__ = ( 'id', 'action', 'color', 'dividers', 'entityUUID', 'flags', 'health', 'title' )
	
	action : int
	color : bytes
	dividers : bytes
	entityUUID : str
	flags : bytes
	health : bytes
	title : bytes

	def __init__(self, proto:int,
		action:int=None,
		color:bytes=None,
		dividers:bytes=None,
		entityUUID:str=None,
		flags:bytes=None,
		health:bytes=None,
		title:bytes=None
	):
		super().__init__(proto,
			action=action,
			color=color,
			dividers=dividers,
			entityUUID=entityUUID,
			flags=flags,
			health=health,
			title=title
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		76 : 12,
		107 : 12,
		108 : 12,
		109 : 12,
		110 : 12,
		201 : 12,
		210 : 12,
		304 : 12,
		315 : 12,
		321 : 13,
		327 : 13,
		331 : 13,
		335 : 12,
		338 : 12,
		340 : 12,
		351 : 12,
		393 : 12,
		401 : 12,
		402 : 12,
		403 : 12,
		404 : 12,
		477 : 12,
		480 : 12,
		490 : 12,
		498 : 12,
		573 : 13,
		575 : 13,
		578 : 13,
		709 : 13,
		734 : 12,
		735 : 12,
		736 : 12,
		751 : 12,
		755 : 13,
		756 : 13,
		757 : 13
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		76 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		107 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		108 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		109 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		110 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		201 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		210 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		304 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		315 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		321 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		327 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		331 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		335 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		338 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		340 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		351 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		393 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		401 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		402 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		403 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		404 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		477 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		480 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		490 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		498 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		573 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		575 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		578 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		709 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		734 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		735 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		736 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		751 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		755 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		756 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ],
		757 : [ ( 'entityUUID', UUID ), ( 'action', VarInt ), ( 'title', SwitchType('action', { 0 : String, 3 : String }, None, ) ), ( 'health', SwitchType('action', { 0 : Float, 2 : Float }, None, ) ), ( 'color', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'dividers', SwitchType('action', { 0 : VarInt, 4 : VarInt }, None, ) ), ( 'flags', SwitchType('action', { 0 : Byte, 5 : Byte }, None, ) ) ]
	}
