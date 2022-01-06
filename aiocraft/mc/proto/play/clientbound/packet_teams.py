"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketTeams(Packet):
	__slots__ = ( 'id', 'collisionRule', 'color', 'formatting', 'friendlyFire', 'mode', 'name', 'nameTagVisibility', 'players', 'prefix', 'suffix', 'team' )
	
	collisionRule : bytes
	color : bytes
	formatting : bytes
	friendlyFire : bytes
	mode : int
	name : bytes
	nameTagVisibility : bytes
	players : bytes
	prefix : bytes
	suffix : bytes
	team : str

	def __init__(self, proto:int,
		collisionRule:bytes=None,
		color:bytes=None,
		formatting:bytes=None,
		friendlyFire:bytes=None,
		mode:int=None,
		name:bytes=None,
		nameTagVisibility:bytes=None,
		players:bytes=None,
		prefix:bytes=None,
		suffix:bytes=None,
		team:str=None
	):
		super().__init__(proto,
			collisionRule=collisionRule,
			color=color,
			formatting=formatting,
			friendlyFire=friendlyFire,
			mode=mode,
			name=name,
			nameTagVisibility=nameTagVisibility,
			players=players,
			prefix=prefix,
			suffix=suffix,
			team=team
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		107 : 65,
		108 : 65,
		109 : 65,
		110 : 65,
		201 : 65,
		210 : 65,
		304 : 65,
		315 : 65,
		321 : 67,
		327 : 67,
		331 : 67,
		335 : 67,
		338 : 68,
		340 : 68,
		351 : 69,
		393 : 71,
		401 : 71,
		402 : 71,
		403 : 71,
		404 : 71,
		477 : 75,
		480 : 75,
		490 : 75,
		498 : 75,
		573 : 76,
		575 : 76,
		578 : 76,
		709 : 77,
		734 : 76,
		735 : 76,
		736 : 76,
		751 : 76,
		755 : 85,
		756 : 85,
		757 : 85
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		107 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		108 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		109 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		110 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		201 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		210 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		304 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		315 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		321 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		327 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		331 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		335 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		338 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		340 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		351 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'color', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		393 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		401 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		402 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ) ],
		403 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ) ],
		404 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		477 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		480 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		490 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		498 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		573 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		575 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		578 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		709 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		734 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		735 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		736 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		751 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		755 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		756 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ],
		757 : [ ( 'team', String ), ( 'mode', Byte ), ( 'name', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'friendlyFire', SwitchType('mode', { 0 : Byte, 2 : Byte }, None, ) ), ( 'nameTagVisibility', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'collisionRule', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'formatting', SwitchType('mode', { 0 : VarInt, 2 : VarInt }, None, ) ), ( 'prefix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'suffix', SwitchType('mode', { 0 : String, 2 : String }, None, ) ), ( 'players', SwitchType('mode', { 0 : ArrayType(String, VarInt, ), 3 : ArrayType(String, VarInt, ), 4 : ArrayType(String, VarInt, ) }, None, ) ) ]
	}
