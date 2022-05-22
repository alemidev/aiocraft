from typing import List, Optional, Iterable
def bit_pack(data:Iterable[int], bits:int, size:int): ...

class Chunk:
	def __init__(self, x: int, z: int, bitmask: int, ground_up_continuous: bool): ...
	def read(self, chunk_data:bytes): ...
	def merge(self, other:'Chunk'): ...

class World:
	def __init__(self): ...
	def get_block(self, x:int, y:int, z:int) -> Optional[int]: ...
	def put_block(self, x:int, y:int, z:int, id:int) -> Optional[int]: ...
	def get(self, x:int, z:int) -> Optional[Chunk]: ...
	def put(self, chunk:Chunk, x:int, z:int, merge:bool): ...
