"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *

class PacketFacePlayer(Packet):
	__slots__ = ( 'id', 'entityId', 'entity_feet_eyes', 'feet_eyes', 'isEntity', 'x', 'y', 'z' )
	
	entityId : Union[int, None]
	entity_feet_eyes : Union[str, None]
	feet_eyes : int
	isEntity : bool
	x : float
	y : float
	z : float

	def __init__(self, proto:int,
		entityId:Union[int, None]=None,
		entity_feet_eyes:Union[str, None]=None,
		feet_eyes:int=None,
		isEntity:bool=None,
		x:float=None,
		y:float=None,
		z:float=None,
		**kwargs
	):
		super().__init__(proto,
			entityId=entityId,
			entity_feet_eyes=entity_feet_eyes,
			feet_eyes=feet_eyes,
			isEntity=isEntity,
			x=x,
			y=y,
			z=z
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		393 : 49,
		401 : 49,
		402 : 49,
		403 : 49,
		404 : 49,
		477 : 52,
		480 : 52,
		490 : 52,
		498 : 52,
		573 : 53,
		575 : 53,
		578 : 53,
		709 : 53,
		734 : 52,
		735 : 52,
		736 : 52,
		751 : 51,
		755 : 55,
		756 : 55,
		757 : 55
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		393 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		401 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		402 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		403 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		404 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		477 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		480 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		490 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		498 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		573 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		575 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		578 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		709 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		734 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		735 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		736 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		751 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		755 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		756 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ],
		757 : [ ( 'feet_eyes', VarInt ), ( 'x', Double ), ( 'y', Double ), ( 'z', Double ), ( 'isEntity', Boolean ), ( 'entityId', SwitchType('isEntity', { 'true' : VarInt }, None, ) ), ( 'entity_feet_eyes', SwitchType('isEntity', { 'true' : String }, None, ) ) ]
	}
