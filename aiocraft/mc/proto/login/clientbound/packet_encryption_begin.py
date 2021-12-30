"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketEncryptionBegin(Packet):
	__slots__ = ( 'id', 'serverId', 'verifyToken', 'publicKey' )
	
	serverId : str
	verifyToken : bytes
	publicKey : bytes

	_state : int = 2

	_ids : Dict[int, int] = {
		5 : 1,
		47 : 1,
		76 : 1,
		107 : 1,
		108 : 1,
		109 : 1,
		110 : 1,
		201 : 1,
		210 : 1,
		304 : 1,
		315 : 1,
		321 : 1,
		327 : 1,
		331 : 1,
		335 : 1,
		338 : 1,
		340 : 1,
		351 : 1,
		393 : 1,
		401 : 1,
		402 : 1,
		403 : 1,
		404 : 1,
		477 : 1,
		480 : 1,
		490 : 1,
		498 : 1,
		573 : 1,
		575 : 1,
		578 : 1,
		709 : 1,
		734 : 1,
		735 : 1,
		736 : 1,
		751 : 1,
		755 : 1,
		756 : 1,
		757 : 1,
		1073741839 : 1
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		5 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		47 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		76 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		107 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		108 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		109 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		110 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		201 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		210 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		304 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		315 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		321 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		327 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		331 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		335 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		338 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		340 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		351 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		393 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		401 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		402 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		403 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		404 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		477 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		480 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		490 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		498 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		573 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		575 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		578 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		709 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		734 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		735 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		736 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		751 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		755 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		756 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		757 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ],
		1073741839 : [ ( 'serverId', String ), ( 'publicKey', ByteArray ), ( 'verifyToken', ByteArray ) ]
	}
