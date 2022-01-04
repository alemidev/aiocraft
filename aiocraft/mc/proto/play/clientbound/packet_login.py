"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketLogin(Packet):
	__slots__ = ( 'id', 'worldNames', 'reducedDebugInfo', 'entityId', 'gameMode', 'viewDistance', 'isHardcore', 'enableRespawnScreen', 'simulationDistance', 'dimensionCodec', 'isFlat', 'isDebug', 'hashedSeed', 'dimension', 'difficulty', 'levelType', 'maxPlayers', 'previousGameMode', 'worldName' )
	
	worldNames : list
	reducedDebugInfo : bool
	entityId : int
	gameMode : int
	viewDistance : int
	isHardcore : bool
	enableRespawnScreen : bool
	simulationDistance : int
	dimensionCodec : bytes
	isFlat : bool
	isDebug : bool
	hashedSeed : int
	dimension : Union[int,bytes,str]
	difficulty : int
	levelType : str
	maxPlayers : int
	previousGameMode : int
	worldName : str

	_state : int = 3

	_ids : Dict[int, int] = {
		5 : 1,
		47 : 1,
		76 : 36,
		107 : 35,
		108 : 35,
		109 : 35,
		110 : 35,
		201 : 35,
		210 : 35,
		304 : 35,
		315 : 35,
		321 : 36,
		327 : 36,
		331 : 36,
		335 : 35,
		338 : 35,
		340 : 35,
		351 : 36,
		393 : 37,
		401 : 37,
		402 : 37,
		403 : 37,
		404 : 37,
		477 : 37,
		480 : 37,
		490 : 37,
		498 : 37,
		573 : 38,
		575 : 38,
		578 : 38,
		709 : 38,
		734 : 37,
		735 : 37,
		736 : 37,
		751 : 36,
		755 : 38,
		756 : 38,
		757 : 38,
		1073741839 : 37
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Byte ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ) ],
		47 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Byte ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		76 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Byte ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		107 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Byte ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		108 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		109 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		110 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		201 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		210 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		304 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		315 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		321 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		327 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		331 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		335 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		338 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		340 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		351 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		393 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		401 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		402 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		403 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		404 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'difficulty', Byte ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'reducedDebugInfo', Boolean ) ],
		477 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ) ],
		480 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ) ],
		490 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ) ],
		498 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ) ],
		573 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'hashedSeed', Long ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ) ],
		575 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'hashedSeed', Long ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ) ],
		578 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'hashedSeed', Long ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ) ],
		709 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'dimension', Int ), ( 'hashedSeed', Long ), ( 'maxPlayers', Byte ), ( 'levelType', String ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ) ],
		734 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'previousGameMode', Byte ), ( 'worldNames', ArrayType(String, VarInt, ) ), ( 'dimensionCodec', NBTTag ), ( 'dimension', String ), ( 'worldName', String ), ( 'hashedSeed', Long ), ( 'maxPlayers', Byte ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ), ( 'isDebug', Boolean ), ( 'isFlat', Boolean ) ],
		735 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'previousGameMode', Byte ), ( 'worldNames', ArrayType(String, VarInt, ) ), ( 'dimensionCodec', NBTTag ), ( 'dimension', String ), ( 'worldName', String ), ( 'hashedSeed', Long ), ( 'maxPlayers', Byte ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ), ( 'isDebug', Boolean ), ( 'isFlat', Boolean ) ],
		736 : [ ( 'entityId', Int ), ( 'gameMode', Byte ), ( 'previousGameMode', Byte ), ( 'worldNames', ArrayType(String, VarInt, ) ), ( 'dimensionCodec', NBTTag ), ( 'dimension', String ), ( 'worldName', String ), ( 'hashedSeed', Long ), ( 'maxPlayers', Byte ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ), ( 'isDebug', Boolean ), ( 'isFlat', Boolean ) ],
		751 : [ ( 'entityId', Int ), ( 'isHardcore', Boolean ), ( 'gameMode', Byte ), ( 'previousGameMode', Byte ), ( 'worldNames', ArrayType(String, VarInt, ) ), ( 'dimensionCodec', NBTTag ), ( 'dimension', NBTTag ), ( 'worldName', String ), ( 'hashedSeed', Long ), ( 'maxPlayers', VarInt ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ), ( 'isDebug', Boolean ), ( 'isFlat', Boolean ) ],
		755 : [ ( 'entityId', Int ), ( 'isHardcore', Boolean ), ( 'gameMode', Byte ), ( 'previousGameMode', Byte ), ( 'worldNames', ArrayType(String, VarInt, ) ), ( 'dimensionCodec', NBTTag ), ( 'dimension', NBTTag ), ( 'worldName', String ), ( 'hashedSeed', Long ), ( 'maxPlayers', VarInt ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ), ( 'isDebug', Boolean ), ( 'isFlat', Boolean ) ],
		756 : [ ( 'entityId', Int ), ( 'isHardcore', Boolean ), ( 'gameMode', Byte ), ( 'previousGameMode', Byte ), ( 'worldNames', ArrayType(String, VarInt, ) ), ( 'dimensionCodec', NBTTag ), ( 'dimension', NBTTag ), ( 'worldName', String ), ( 'hashedSeed', Long ), ( 'maxPlayers', VarInt ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ), ( 'isDebug', Boolean ), ( 'isFlat', Boolean ) ],
		757 : [ ( 'entityId', Int ), ( 'isHardcore', Boolean ), ( 'gameMode', Byte ), ( 'previousGameMode', Byte ), ( 'worldNames', ArrayType(String, VarInt, ) ), ( 'dimensionCodec', NBTTag ), ( 'dimension', NBTTag ), ( 'worldName', String ), ( 'hashedSeed', Long ), ( 'maxPlayers', VarInt ), ( 'viewDistance', VarInt ), ( 'simulationDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ), ( 'isDebug', Boolean ), ( 'isFlat', Boolean ) ],
		1073741839 : [ ( 'entityId', Int ), ( 'isHardcore', Boolean ), ( 'gameMode', Byte ), ( 'previousGameMode', Byte ), ( 'worldNames', ArrayType(String, VarInt, ) ), ( 'dimensionCodec', NBTTag ), ( 'dimension', NBTTag ), ( 'worldName', String ), ( 'hashedSeed', Long ), ( 'maxPlayers', VarInt ), ( 'viewDistance', VarInt ), ( 'reducedDebugInfo', Boolean ), ( 'enableRespawnScreen', Boolean ), ( 'isDebug', Boolean ), ( 'isFlat', Boolean ) ]
	}
