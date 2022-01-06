"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketEncryptionBegin(Packet):
	__slots__ = ( 'id', 'sharedSecret', 'verifyToken' )
	
	sharedSecret : bytes
	verifyToken : bytes

	def __init__(self, proto:int,
		sharedSecret:bytes=None,
		verifyToken:bytes=None
	):
		super().__init__(proto,
			sharedSecret=sharedSecret,
			verifyToken=verifyToken
		)

	_state : int = 2

	_ids : Dict[int, int] = {
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
		757 : 1
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		47 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		76 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		107 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		108 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		109 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		110 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		201 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		210 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		304 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		315 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		321 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		327 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		331 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		335 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		338 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		340 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		351 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		393 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		401 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		402 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		403 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		404 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		477 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		480 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		490 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		498 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		573 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		575 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		578 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		709 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		734 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		735 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		736 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		751 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		755 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		756 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ],
		757 : [ ( 'sharedSecret', ByteArray ), ( 'verifyToken', ByteArray ) ]
	}
