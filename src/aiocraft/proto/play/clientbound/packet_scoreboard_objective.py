"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketScoreboardObjective(Packet):
	__slots__ = ( 'id', 'action', 'displayText', 'name', 'type' )
	
	action : int
	displayText : Union[None, str]
	name : str
	type : Union[Union[None, int],Union[None, str]]

	def __init__(self, 
		action:int | None = None,
		displayText:Union[None, str] | None = None,
		name:str | None = None,
		type:Union[Union[None, int],Union[None, str]] | None = None,
		**kwargs
	):
		super().__init__(
			action=action,
			displayText=displayText,
			name=name,
			type=type
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 59,
		76 : 63,
		107 : 63,
		108 : 63,
		109 : 63,
		110 : 63,
		201 : 63,
		210 : 63,
		304 : 63,
		315 : 63,
		321 : 65,
		327 : 65,
		331 : 65,
		335 : 65,
		338 : 66,
		340 : 66,
		351 : 67,
		393 : 69,
		401 : 69,
		402 : 69,
		403 : 69,
		404 : 69,
		477 : 73,
		480 : 73,
		490 : 73,
		498 : 73,
		573 : 74,
		575 : 74,
		578 : 74,
		709 : 75,
		734 : 74,
		735 : 74,
		736 : 74,
		751 : 74,
		755 : 83,
		756 : 83,
		757 : 83,
		758 : 83,
		759 : 83,
		760 : 86,
		761 : 84
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		76 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		107 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		108 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		109 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		110 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		201 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		210 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		304 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		315 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		321 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		327 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		331 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		335 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		338 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		340 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		351 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : String, 2 : String }, None, ) ) ],
		393 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		401 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		402 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		403 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		404 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		477 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		480 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		490 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		498 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		573 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		575 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		578 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		709 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		734 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		735 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		736 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		751 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		755 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		756 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		757 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		758 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		759 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		760 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ],
		761 : [ ( 'name', String ), ( 'action', Byte ), ( 'displayText', SwitchType('action', { 0 : String, 2 : String }, None, ) ), ( 'type', SwitchType('action', { 0 : VarInt, 2 : VarInt }, None, ) ) ]
	}
