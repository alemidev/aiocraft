"""[!] This file is autogenerated"""

from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *

class PacketUnlockRecipes(Packet):
	__slots__ = ( 'id', 'filteringCraftable', 'action', 'filteringSmeltable', 'smeltingBookOpen', 'smokerBookOpen', 'notification', 'blastFurnaceOpen', 'recipes1', 'recipes2', 'filteringBlastFurnace', 'craftingBookOpen', 'recipes', 'filteringSmoker' )
	
	filteringCraftable : bool
	action : int
	filteringSmeltable : bool
	smeltingBookOpen : bool
	smokerBookOpen : bool
	notification : bool
	blastFurnaceOpen : bool
	recipes1 : list
	recipes2 : Union[bytes,list]
	filteringBlastFurnace : bool
	craftingBookOpen : bool
	recipes : list
	filteringSmoker : bool

	_state : int = 3

	_ids : Dict[int, int] = {
		321 : 49,
		327 : 49,
		331 : 49,
		335 : 48,
		338 : 49,
		340 : 49,
		351 : 50,
		393 : 52,
		401 : 52,
		402 : 52,
		403 : 52,
		404 : 52,
		477 : 54,
		480 : 54,
		490 : 54,
		498 : 54,
		573 : 55,
		575 : 55,
		578 : 55,
		709 : 55,
		734 : 54,
		735 : 54,
		736 : 54,
		751 : 53,
		755 : 57,
		756 : 57,
		757 : 57,
		1073741839 : 54
	}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {
		321 : [ ( 'notification', Boolean ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'recipes', ArrayType(StructType(( 'identifier', String ), ( 'isUnlocked', Boolean ), ( 'hasBeenDisplayed', Boolean ), ), VarInt, ) ) ],
		327 : [ ( 'action', Short ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'recipes1', ArrayType(Int, VarInt, ) ), ( 'recipes2', ArrayType(Int, VarInt, ) ) ],
		331 : [ ( 'action', Short ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'recipes1', ArrayType(Int, VarInt, ) ), ( 'recipes2', ArrayType(Int, VarInt, ) ) ],
		335 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'recipes1', ArrayType(VarInt, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(VarInt, VarInt, ) }, None, ) ) ],
		338 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'recipes1', ArrayType(VarInt, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(VarInt, VarInt, ) }, None, ) ) ],
		340 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'recipes1', ArrayType(VarInt, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(VarInt, VarInt, ) }, None, ) ) ],
		351 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		393 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		401 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		402 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		403 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		404 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		477 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		480 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		490 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		498 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		573 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		575 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		578 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		709 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		734 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		735 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		736 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		751 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'blastFurnaceOpen', Boolean ), ( 'filteringBlastFurnace', Boolean ), ( 'smokerBookOpen', Boolean ), ( 'filteringSmoker', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		755 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'blastFurnaceOpen', Boolean ), ( 'filteringBlastFurnace', Boolean ), ( 'smokerBookOpen', Boolean ), ( 'filteringSmoker', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		756 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'blastFurnaceOpen', Boolean ), ( 'filteringBlastFurnace', Boolean ), ( 'smokerBookOpen', Boolean ), ( 'filteringSmoker', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		757 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'blastFurnaceOpen', Boolean ), ( 'filteringBlastFurnace', Boolean ), ( 'smokerBookOpen', Boolean ), ( 'filteringSmoker', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ],
		1073741839 : [ ( 'action', VarInt ), ( 'craftingBookOpen', Boolean ), ( 'filteringCraftable', Boolean ), ( 'smeltingBookOpen', Boolean ), ( 'filteringSmeltable', Boolean ), ( 'blastFurnaceOpen', Boolean ), ( 'filteringBlastFurnace', Boolean ), ( 'smokerBookOpen', Boolean ), ( 'filteringSmoker', Boolean ), ( 'recipes1', ArrayType(String, VarInt, ) ), ( 'recipes2', SwitchType('action', { 0 : ArrayType(String, VarInt, ) }, None, ) ) ]
	}
