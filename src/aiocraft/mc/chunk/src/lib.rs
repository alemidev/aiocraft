use pyo3::{prelude::*, exceptions::PyValueError};

pub trait ChunkSection {
	fn new(chunk_data: &mut Vec<u8>) -> Self;
	fn get_states(&self) -> [[[u16; 16]; 16]; 16];
	fn get_light(&self) -> [[[u16; 16]; 16]; 16];
	fn get_sky_light(&self) -> Option<[[[u16; 16]; 16]; 16]>;

	fn read_varint(buffer: &mut Vec<u8>) -> PyResult<i32> {
		let mut num_read = 0;
		let mut result : i32 = 0;
		loop {
			if buffer.len() < 1 {
				return Err(PyValueError::new_err("VarInt too short"));
			}
			let data = buffer.remove(0);
			result |= ((data & 0b01111111) << (7 * num_read)) as i32;
			num_read +=1;
			if num_read > 4 {
				return Err(PyValueError::new_err("VarInt too big"));
			}
			if data & 0b10000000 == 0 {
				break
			}
		}
		return Ok(result);
	}

	fn read_paletted_container(buffer: &mut Vec<u8>) -> [[[u16; 16]; 16]; 16] {
		let mut bits : u8 = buffer[0]; // TODO is this is big endian ?
		// bits = UnsignedByte.read(buffer, ctx=ctx) # FIXME if bits > 4 it reads trash
		// #logging.debug("[%d|%d@%d] Bits per block : %d", ctx.x, ctx.z, ctx.sec, bits)
		if bits < 4 { bits = 4 };
		if bits >= 9 { bits = 13 };  // this should not be hardcoded but we have no way to calculate all possible block states
		let palette_len = ChunkFormat340::read_varint(buffer).unwrap(); // TODO handle possible error
		let mut palette = vec![0;palette_len as usize];
		for p in 0..palette_len as usize{
			palette[p] = ChunkFormat340::read_varint(buffer).unwrap(); // TODO handle possible error
		}
		// # logging.debug("[%d|%d@%d] Palette section : [%d] %s", ctx.x, ctx.z, ctx.sec, palette_len, str(palette))
		let container_size = ChunkFormat340::read_varint(buffer).unwrap(); // TODO handle possible error
		let block_data = buffer.drain(0..(container_size as usize*8));
		let mut section = [[[0u16;16]; 16]; 16];
		let max_val : u16 = (1<<bits) - 1;
		for y in 0..16 { // TODO should probably read them as longs first!
			for z in 0..16 {
				for x in 0..16 {
		 			let i = x + ((y * 16) + z) * 16;
		 			let start_byte = (i * bits as usize) / 8; // TODO when fixes, change to /64
		 			let start_offset = (i * bits as usize) % 8; // TODO when fixed, change to %64
		 			let end_byte = ((i + 1) * bits as usize - 1) / 8; // TODO when fixed, change to /64
		 			if start_byte == end_byte {
		 				section[x][y][z] = palette[
							 ((block_data.as_slice()[start_byte as usize] >> start_offset) as usize) & max_val as usize
						] as u16;
					} else {
		 				let end_offset = 64 - start_offset;
		 				section[x][y][z] = palette[(
							 (block_data.as_slice()[start_byte as usize] as usize) >> start_offset
							 | (block_data.as_slice()[end_byte as usize] as usize) << end_offset
						) & max_val as usize] as u16;
					}
				}
			}
		}
		return section;
	}
}

struct ChunkFormat340 {
	block_states: [[[u16; 16]; 16]; 16],
	block_light: [[[u16; 16]; 16]; 16],
	sky_light: Option<[[[u16; 16]; 16]; 16]>,
} //https://docs.rs/crate/cpu-endian/latest/source/src/lib.rs

impl ChunkFormat340 {
	fn read_half_byte_array(buffer: &mut Vec<u8>) -> [[[u16; 16]; 16]; 16] {
		let buf = buffer.drain(0..((16 * 16 * 16) / 2));
		let mut out = [[[0u16; 16]; 16]; 16];
		for y in 0..16 {
			for z in 0..16 {
				for x in 0..16 {
					let index:usize = (((y * 16) + z) * 16) + x;
					let tmp = buf.as_slice()[index / 2];
					out[x][y][z] = if index / 2 != 0 { tmp >> 4 } else { tmp & 0xF } as u16
				}
			}
		}
		return out;
	}
}

impl ChunkSection for ChunkFormat340 {
	fn new(chunk_data: &mut Vec<u8>) -> Self {
		Self {
			block_states: ChunkFormat340::read_paletted_container(chunk_data), // TODO! It's a paletted container
			block_light: ChunkFormat340::read_half_byte_array(chunk_data),
			sky_light: Some(ChunkFormat340::read_half_byte_array(chunk_data)), // TODO are we in overworld?
		}
	}

	fn get_states(&self) -> [[[u16; 16]; 16]; 16] { self.block_states }
	fn get_light(&self) -> [[[u16; 16]; 16]; 16] { self.block_light }
	fn get_sky_light(&self) -> Option<[[[u16; 16]; 16]; 16]> { self.sky_light }
}

#[pyclass]
struct Chunk {
	x: i32,
	z: i32,
	bitmask: u16,
	ground_up_continuous: bool,
	block_states: [[[u16; 16]; 256]; 16],
	block_light: [[[u16; 16]; 256]; 16],
	sky_light: [[[u16; 16]; 256]; 16],
	biomes: [u8; 256],
}

impl Chunk {
	fn new(x: i32, z: i32, bitmask: u16, ground_up_continuous: bool) -> Self {
		Self {
			x: x,
			z: z,
			bitmask: bitmask,
			ground_up_continuous: ground_up_continuous,
			block_states: [[[0u16; 16]; 256]; 16],
			block_light: [[[0u16; 16]; 256]; 16],
			sky_light: [[[0u16; 16]; 256]; 16],
			biomes: [0u8; 256],
		}
	}

	fn read(&self, mut chunk_data: Vec<u8>) -> PyResult<()> {
		for i in 0..16 {
			if ((self.bitmask >> i) & 1) != 0 {
				let section: ChunkFormat340 = ChunkFormat340::new(&mut chunk_data);
				// self.blocks[:, i*16 : (i+1)*16, :] = block_states
				// self.block_light[:, i*16 : (i+1)*16, :] = block_light
				// self.sky_light[:, i*16 : (i+1)*16, :] = sky_light
			}
		}
		// TODO
		// if self.ground_up_continuous {
		// 	self.biomes = buffer.read(256) //16x16
		// }
		// if buffer.read() {
		// 	logging.warning("Leftover data in chunk buffer")
		// }
		return Ok(());
	}
}

// Biomes
//
// The biomes array is only present when ground-up continuous is set to true. Biomes cannot be changed unless a chunk is re-sent.
//
// The structure is an array of 256 bytes, each representing a Biome ID (it is recommended that 127 for "Void" is used if there is no set biome). The array is indexed by z * 16 | x.

/*
class World:
	chunks : Dict[Tuple[int, int], Chunk]

	def __init__(self):
		self.chunks = {}

	def __getitem__(self, item:Tuple[int, int, int]):
		return self.get(*item)

	def get(self, x:int, y:int, z:int) -> int:
		coord = (x//16, z//16)
		if coord not in self.chunks:
			raise KeyError(f"Chunk {coord} not loaded")
		return self.chunks[coord][int(x%16), int(y), int(z%16)]

	def put(self, chunk:Chunk, x:int, z:int, merge:bool=False):
		if merge and (x,z) in self.chunks:
			chunk.merge(self.chunks[(x,z)])
		self.chunks[(x,z)] = chunk
*/
