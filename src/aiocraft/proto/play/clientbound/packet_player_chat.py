"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union, Optional
from ....packet import Packet
from ....types import *
from ....primitives import *

class PacketPlayerChat(Packet):
	__slots__ = ( 'id', 'filterType', 'filterTypeMask', 'formattedMessage', 'index', 'networkName', 'networkTargetName', 'plainMessage', 'previousMessages', 'previousSignature', 'salt', 'senderName', 'senderTeam', 'senderUuid', 'signature', 'signedChatContent', 'timestamp', 'type', 'unsignedChatContent', 'unsignedContent' )
	
	filterType : int
	filterTypeMask : Union[None, list]
	formattedMessage : tuple
	index : int
	networkName : str
	networkTargetName : tuple
	plainMessage : str
	previousMessages : bytes
	previousSignature : tuple
	salt : int
	senderName : str
	senderTeam : tuple
	senderUuid : str
	signature : Union[bytes,tuple]
	signedChatContent : str
	timestamp : int
	type : int
	unsignedChatContent : tuple
	unsignedContent : tuple

	def __init__(self, 
		filterType:int | None = None,
		filterTypeMask:Union[None, list] | None = None,
		formattedMessage:tuple | None = None,
		index:int | None = None,
		networkName:str | None = None,
		networkTargetName:tuple | None = None,
		plainMessage:str | None = None,
		previousMessages:bytes | None = None,
		previousSignature:tuple | None = None,
		salt:int | None = None,
		senderName:str | None = None,
		senderTeam:tuple | None = None,
		senderUuid:str | None = None,
		signature:Union[bytes,tuple] | None = None,
		signedChatContent:str | None = None,
		timestamp:int | None = None,
		type:int | None = None,
		unsignedChatContent:tuple | None = None,
		unsignedContent:tuple | None = None,
		**kwargs
	):
		super().__init__(
			filterType=filterType,
			filterTypeMask=filterTypeMask,
			formattedMessage=formattedMessage,
			index=index,
			networkName=networkName,
			networkTargetName=networkTargetName,
			plainMessage=plainMessage,
			previousMessages=previousMessages,
			previousSignature=previousSignature,
			salt=salt,
			senderName=senderName,
			senderTeam=senderTeam,
			senderUuid=senderUuid,
			signature=signature,
			signedChatContent=signedChatContent,
			timestamp=timestamp,
			type=type,
			unsignedChatContent=unsignedChatContent,
			unsignedContent=unsignedContent
		)

	_state : int = 3

	_ids : Dict[int, int] = {
		759 : 48,
		760 : 51,
		761 : 49
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		759 : [ ( 'signedChatContent', String ), ( 'unsignedChatContent', OptionalType(String, ) ), ( 'type', VarInt ), ( 'senderUuid', UUID ), ( 'senderName', String ), ( 'senderTeam', OptionalType(String, ) ), ( 'timestamp', Long ), ( 'salt', Long ), ( 'signature', ByteArray ) ],
		760 : [ ( 'previousSignature', OptionalType(ByteArray, ) ), ( 'senderUuid', UUID ), ( 'signature', ByteArray ), ( 'plainMessage', String ), ( 'formattedMessage', OptionalType(String, ) ), ( 'timestamp', Long ), ( 'salt', Long ), ( 'previousMessages', TrailingData ), ( 'unsignedContent', OptionalType(String, ) ), ( 'filterType', VarInt ), ( 'filterTypeMask', SwitchType('filterType', { 2 : ArrayType(Long, VarInt, ) }, None, ) ), ( 'type', VarInt ), ( 'networkName', String ), ( 'networkTargetName', OptionalType(String, ) ) ],
		761 : [ ( 'senderUuid', UUID ), ( 'index', VarInt ), ( 'signature', OptionalType(ByteArray, ) ), ( 'plainMessage', String ), ( 'timestamp', Long ), ( 'salt', Long ), ( 'previousMessages', TrailingData ), ( 'unsignedChatContent', OptionalType(String, ) ), ( 'filterType', VarInt ), ( 'filterTypeMask', SwitchType('filterType', { 2 : ArrayType(Long, VarInt, ) }, None, ) ), ( 'type', VarInt ), ( 'networkName', String ), ( 'networkTargetName', OptionalType(String, ) ) ]
	}