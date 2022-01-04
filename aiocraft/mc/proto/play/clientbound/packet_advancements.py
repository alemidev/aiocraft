"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketAdvancements(Packet):
	__slots__ = ( 'id', 'reset', 'progressMapping', 'advancementMapping', 'identifiers' )
	
	reset : bool
	progressMapping : list
	advancementMapping : list
	identifiers : list

	_state : int = 3

	_ids : Dict[int, int] = {
		321 : 8,
		327 : 8,
		331 : 8,
		335 : 76,
		338 : 77,
		340 : 77,
		351 : 79,
		393 : 81,
		401 : 81,
		402 : 81,
		403 : 81,
		404 : 81,
		477 : 87,
		480 : 87,
		490 : 87,
		498 : 87,
		573 : 88,
		575 : 88,
		578 : 88,
		709 : 88,
		734 : 87,
		735 : 87,
		736 : 87,
		751 : 87,
		755 : 98,
		756 : 98,
		757 : 99,
		1073741839 : 88
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		321 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', VarInt ), ( 'frameType', VarInt ), ( 'backgroundTexture', OptionalType(String, ) ), ( 'xCord', VarInt ), ( 'yCord', VarInt ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		327 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'backgroundTexture', OptionalType(String, ) ), ( 'showToast', Boolean ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		331 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', OptionalType(String, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		335 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		338 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		340 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		351 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		393 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		401 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		402 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		403 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		404 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		477 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		480 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		490 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		498 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		573 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		575 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		578 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		709 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		734 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		735 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		736 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		751 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		755 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		756 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		757 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ],
		1073741839 : [ ( 'reset', Boolean ), ( 'advancementMapping', ArrayType(StructType(( 'key', String ), ( 'value', StructType(( 'parentId', OptionalType(String, ) ), ( 'displayData', OptionalType(StructType(( 'title', String ), ( 'description', String ), ( 'icon', Slot ), ( 'frameType', VarInt ), ( 'flags', Int ), ( 'backgroundTexture', SwitchType('has_background_texture', { 1 : String }, None, ) ), ( 'xCord', Float ), ( 'yCord', Float ), ), ) ), ( 'criteria', ArrayType(StructType(( 'key', String ), ( 'value', Void ), ), VarInt, ) ), ( 'requirements', ArrayType(ArrayType(String, VarInt, ), VarInt, ) ), ) ), ), VarInt, ) ), ( 'identifiers', ArrayType(String, VarInt, ) ), ( 'progressMapping', ArrayType(StructType(( 'key', String ), ( 'value', ArrayType(StructType(( 'criterionIdentifier', String ), ( 'criterionProgress', OptionalType(Long, ) ), ), VarInt, ) ), ), VarInt, ) ) ]
	}
