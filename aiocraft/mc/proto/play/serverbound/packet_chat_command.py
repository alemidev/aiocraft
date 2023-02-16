"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....definitions import *
from ....types import *

class PacketChatCommand(Packet):
	__slots__ = ( 'id', 'acknowledged', 'argumentSignatures', 'command', 'lastRejectedMessage', 'messageCount', 'previousMessages', 'salt', 'signedPreview', 'timestamp' )
	
	acknowledged : bytes
	argumentSignatures : list
	command : str
	lastRejectedMessage : tuple
	messageCount : int
	previousMessages : bytes
	salt : int
	signedPreview : bool
	timestamp : int

	def __init__(self, proto:int,
		acknowledged:bytes=None,
		argumentSignatures:list=None,
		command:str=None,
		lastRejectedMessage:tuple=None,
		messageCount:int=None,
		previousMessages:bytes=None,
		salt:int=None,
		signedPreview:bool=None,
		timestamp:int=None,
		**kwargs
	):
		super().__init__(proto,
			acknowledged=acknowledged,
			argumentSignatures=argumentSignatures,
			command=command,
			lastRejectedMessage=lastRejectedMessage,
			messageCount=messageCount,
			previousMessages=previousMessages,
			salt=salt,
			signedPreview=signedPreview,
			timestamp=timestamp
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		759 : 3,
		760 : 4,
		761 : 4
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		759 : [ ( 'command', String ), ( 'timestamp', Long ), ( 'salt', Long ), ( 'argumentSignatures', ArrayType(StructType(( 'argumentName', String ), ( 'signature', ByteArray ), ), VarInt, ) ), ( 'signedPreview', Boolean ) ],
		760 : [ ( 'command', String ), ( 'timestamp', Long ), ( 'salt', Long ), ( 'argumentSignatures', ArrayType(StructType(( 'argumentName', String ), ( 'signature', ByteArray ), ), VarInt, ) ), ( 'signedPreview', Boolean ), ( 'previousMessages', TrailingData ), ( 'lastRejectedMessage', OptionalType(StructType(( 'sender', UUID ), ( 'signature', ByteArray ), ), ) ) ],
		761 : [ ( 'command', String ), ( 'timestamp', Long ), ( 'salt', Long ), ( 'argumentSignatures', ArrayType(StructType(( 'argumentName', String ), ( 'signature', ByteArray ), ), VarInt, ) ), ( 'messageCount', VarInt ), ( 'acknowledged', ByteArray ) ]
	}
