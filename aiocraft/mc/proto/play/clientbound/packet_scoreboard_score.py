"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketScoreboardScore(Packet):
	__slots__ = ( 'id', 'action', 'itemName', 'scoreName', 'value' )
	
	action : int
	itemName : str
	scoreName : str
	value : Union[None, int]

	def __init__(self, proto:int,
		action:int=None,
		itemName:str=None,
		scoreName:str=None,
		value:Union[None, int]=None,
		**kwargs
	):
		super().__init__(proto,
			action=action,
			itemName=itemName,
			scoreName=scoreName,
			value=value
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 60,
		76 : 65,
		107 : 66,
		108 : 66,
		109 : 66,
		110 : 66,
		201 : 66,
		210 : 66,
		304 : 66,
		315 : 66,
		321 : 68,
		327 : 68,
		331 : 68,
		335 : 68,
		338 : 69,
		340 : 69,
		351 : 70,
		393 : 72,
		401 : 72,
		402 : 72,
		403 : 72,
		404 : 72,
		477 : 76,
		480 : 76,
		490 : 76,
		498 : 76,
		573 : 77,
		575 : 77,
		578 : 77,
		709 : 78,
		734 : 77,
		735 : 77,
		736 : 77,
		751 : 77,
		755 : 86,
		756 : 86,
		757 : 86,
		758 : 86,
		759 : 86,
		760 : 89,
		761 : 87
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		76 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		107 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		108 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		109 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		110 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		201 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		210 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		304 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		315 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		321 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		327 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		331 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		335 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		338 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		340 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		351 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		393 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		401 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		402 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		403 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		404 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		477 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		480 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		490 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		498 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		573 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		575 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		578 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		709 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		734 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		735 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		736 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		751 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		755 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		756 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		757 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		758 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		759 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		760 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ],
		761 : [ ( 'itemName', String ), ( 'action', VarInt ), ( 'scoreName', String ), ( 'value', SwitchType('action', { 1 : Void }, VarInt, ) ) ]
	}
