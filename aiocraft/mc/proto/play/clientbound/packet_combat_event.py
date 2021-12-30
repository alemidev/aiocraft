"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketCombatEvent(Packet):
	__slots__ = ( 'id', 'event', 'duration', 'playerId', 'message', 'entityId' )
	
	event : int
	duration : bytes
	playerId : bytes
	message : bytes
	entityId : bytes

	_state : int = 3

	_ids : Dict[int, int] = {
		47 : 66,
		76 : 44,
		107 : 44,
		108 : 44,
		109 : 44,
		110 : 44,
		201 : 44,
		210 : 44,
		304 : 44,
		315 : 44,
		321 : 45,
		327 : 45,
		331 : 45,
		335 : 44,
		338 : 45,
		340 : 45,
		351 : 46,
		393 : 47,
		401 : 47,
		402 : 47,
		403 : 47,
		404 : 47,
		477 : 50,
		480 : 50,
		490 : 50,
		498 : 50,
		573 : 51,
		575 : 51,
		578 : 51,
		709 : 51,
		734 : 50,
		735 : 50,
		736 : 50,
		751 : 49,
		1073741839 : 50
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		76 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		107 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		108 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		109 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		110 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		201 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		210 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		304 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		315 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		321 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		327 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		331 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		335 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		338 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		340 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		351 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		393 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		401 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		402 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		403 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		404 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		477 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		480 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		490 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		498 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		573 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		575 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		578 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		709 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		734 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		735 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		736 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		751 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ],
		1073741839 : [ ( 'event', VarInt ), ( 'duration', SwitchType('event', { 1 : VarInt }, None, ) ), ( 'playerId', SwitchType('event', { 2 : VarInt }, None, ) ), ( 'entityId', SwitchType('event', { 1 : Int, 2 : Int }, None, ) ), ( 'message', SwitchType('event', { 2 : String }, None, ) ) ]
	}
