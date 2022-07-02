use std::collections::HashMap;
use std::io::{Cursor, Read};
use log::{info, warn};

use pyo3::{exceptions::PyValueError, prelude::*};

fn abs(v:i32, modulo:i32) -> i32 {
	if v < 0 {
		return modulo + (v % modulo);
	} else {
		return v % modulo;
	}
}

#[pyfunction]
pub fn bit_pack(data: Vec<i32>, bits: i32, size: i32) -> PyResult<Vec<i32>> {
	if size <= bits {
		return Err(PyValueError::new_err(
			"Cannot pack into chunks smaller than bits per block",
		));
	}
	let mut out = vec![0; 0];
	let mut cursor = 0;
	let mut buffer = 0;
	for el in data {
		if cursor + bits > size {
			let delta = (cursor + bits) - size;
			buffer |= (el & (2 << (bits - delta) - 1)) << cursor;
			out.push(buffer);
			buffer = 0 | ((el >> (bits - delta)) & (2 << delta - 1));
			cursor = delta;
		} else {
			buffer |= (el & (2 << bits - 1)) << cursor;
			cursor += bits;
		}
	}
	return Ok(out);
}

pub trait ChunkSection {
	fn new() -> Self;
	fn read<R: Read>(&mut self, chunk_data: &mut R) -> PyResult<()>;
	fn get_states(&self) -> [[[u16; 16]; 16]; 16];
	fn get_light(&self) -> [[[u16; 16]; 16]; 16];
	fn get_sky_light(&self) -> Option<[[[u16; 16]; 16]; 16]>;

	fn read_varint<R: Read>(buffer: &mut R) -> PyResult<i32> {
		let mut num_read = 0;
		let mut result: i32 = 0;
		loop {
			let mut data: [u8; 1] = [0u8; 1];
			buffer.read_exact(&mut data)?;
			result |= ((data[0] & 0b01111111) as i32) << (7 * num_read);
			num_read += 1;
			if num_read > 4 {
				return Err(PyValueError::new_err("VarInt too big"));
			}
			if data[0] & 0b10000000 == 0 {
				break;
			}
		}
		return Ok(result);
	}

	fn read_paletted_container<R: Read>(buffer: &mut R) -> PyResult<[[[u16; 16]; 16]; 16]> {
		let mut data: [u8; 1] = [0u8; 1];
		buffer.read_exact(&mut data)?;
		// bits = UnsignedByte.read(buffer, ctx=ctx) # FIXME if bits > 4 it reads trash
		// #logging.debug("[%d|%d@%d] Bits per block : %d", ctx.x, ctx.z, ctx.sec, bits)
		let bits;
		if data[0] < 4 {
			bits = 4
		} else if data[0] >= 9 {
			bits = 13
		}
		// this should not be hardcoded but we have no way to calculate all possible block states
		else {
			bits = data[0]
		}
		let palette_len = ChunkFormat340::read_varint(buffer)?;
		let mut palette = vec![0; palette_len as usize];
		for p in 0..palette_len as usize {
			palette[p] = ChunkFormat340::read_varint(buffer)?;
		}
		// # logging.debug("[%d|%d@%d] Palette section : [%d] %s", ctx.x, ctx.z, ctx.sec, palette_len, str(palette))
		let container_size = ChunkFormat340::read_varint(buffer)?;
		let mut block_data = vec![0u64; container_size as usize];
		let mut recv_buf: [u8; 8] = [0u8; 8];
		for i in 0..container_size as usize {
			buffer.read_exact(&mut recv_buf)?;
			let mut tmp: u64 = 0;
			for j in 0..8 {
				tmp |= (recv_buf[j] as u64) << ((7-j) * 8);
			}
			block_data[i] = tmp;
		}
		let mut section = [[[0u16; 16]; 16]; 16];
		let max_val: u16 = (1 << bits) - 1;
		for y in 0..16 {
			for z in 0..16 {
				for x in 0..16 {
					let i = (((y * 16) + z) * 16) + x;
					let start_byte = (i * bits as usize) / 64;
					let start_offset = (i * bits as usize) % 64;
					let end_byte = ((i + 1) * bits as usize - 1) / 64;
					let value: u16;
					if start_byte == end_byte {
						value = ((block_data[start_byte as usize] //FIXME out of bounds?
							>> start_offset) & max_val as u64) as u16;
					} else {
						let end_offset = 64 - start_offset;
						value = (((block_data[start_byte as usize] as usize)
							>> start_offset
							| (block_data[end_byte as usize] as usize) << end_offset)
							& max_val as usize) as u16;
					}
					if bits == 13 {
						section[x][y][z] = value;
					} else {
						if value as i32 >= palette_len {
							warn!("index out of palette bounds : {}/{} (bits {})", value, palette_len, bits);
							section[x][y][z] = value;
						} else {
							section[x][y][z] = palette[value as usize] as u16;
						}
					}
				}
			}
		}
		return Ok(section);
	}
}

struct ChunkFormat340 {
	block_states: [[[u16; 16]; 16]; 16],
	block_light: [[[u16; 16]; 16]; 16],
	sky_light: Option<[[[u16; 16]; 16]; 16]>,
}

impl ChunkFormat340 {
	fn read_half_byte_array<R: Read>(buffer: &mut R) -> PyResult<[[[u16; 16]; 16]; 16]> {
		let mut buf: [u8; (16 * 16 * 16) / 2] = [0u8; (16 * 16 * 16) / 2];
		buffer.read_exact(&mut buf)?;
		let mut out = [[[0u16; 16]; 16]; 16];
		for y in 0..16 {
			for z in 0..16 {
				for x in 0..16 {
					let index: usize = (((y * 16) + z) * 16) + x;
					let tmp = buf[index / 2];
					out[x][y][z] = if index / 2 != 0 { tmp >> 4 } else { tmp & 0xF } as u16
				}
			}
		}
		return Ok(out);
	}
}

impl ChunkSection for ChunkFormat340 {
	fn new() -> Self {
		return Self { block_states: [[[0;16];16];16], block_light: [[[0;16];16];16], sky_light: Some([[[0;16];16];16]) };
	}

	fn read<R: Read>(&mut self, chunk_data: &mut R) -> PyResult<()> {
		self.block_states = ChunkFormat340::read_paletted_container(chunk_data)?; // TODO! Handle error
		self.block_light = ChunkFormat340::read_half_byte_array(chunk_data)?;
		self.sky_light =  Some(ChunkFormat340::read_half_byte_array(chunk_data)?); // TODO are we in overworld?
		return Ok(());
	}

	fn get_states(&self) -> [[[u16; 16]; 16]; 16] {
		self.block_states
	}
	fn get_light(&self) -> [[[u16; 16]; 16]; 16] {
		self.block_light
	}
	fn get_sky_light(&self) -> Option<[[[u16; 16]; 16]; 16]> {
		self.sky_light
	}
}

#[pyclass]
pub struct Chunk {
	pub x: i32,
	pub z: i32,
	pub bitmask: u16,
	pub ground_up_continuous: bool,
	block_states: [[[u16; 16]; 256]; 16],
	block_light: [[[u16; 16]; 256]; 16],
	sky_light: [[[u16; 16]; 256]; 16],
	biomes: [u8; 256],
	block_entities: String, // TODO less jank way to store this NBT/JSON/PyDict ...
}
// Biomes
// The biomes array is only present when ground-up continuous is set to true. Biomes cannot be changed unless a chunk is re-sent.
// The structure is an array of 256 bytes, each representing a Biome ID (it is recommended that 127 for "Void" is used if there is no set biome). The array is indexed by z * 16 | x.

#[pymethods]
impl Chunk {
	#[new]
	pub fn new(x: i32, z: i32, bitmask: u16, ground_up_continuous: bool, block_entities: String) -> Self {
		Self {
			x: x,
			z: z,
			bitmask: bitmask,
			ground_up_continuous: ground_up_continuous,
			block_states: [[[0u16; 16]; 256]; 16],
			block_light: [[[0u16; 16]; 256]; 16],
			sky_light: [[[0u16; 16]; 256]; 16],
			biomes: [0u8; 256],
			block_entities: block_entities,
		}
	}

	pub fn read(&mut self, chunk_data: Vec<u8>) -> PyResult<()> {
		let mut c = Cursor::new(chunk_data);
		for i in 0..16 {
			if ((self.bitmask >> i) & 1) != 0 {
				let mut section: ChunkFormat340 = ChunkFormat340::new();
				section.read(&mut c)?;
				for x in 0..16 {
					for y in 0..16 {
						for z in 0..16 {
							self.block_states[x][(i * 16) + y][z] = section.block_states[x][y][z];
							self.block_light[x][(i * 16) + y][z] = section.block_states[x][y][z];
							self.sky_light[x][(i * 16) + y][z] = section.block_states[x][y][z];
						}
					}
				}
			}
		}

		if self.ground_up_continuous {
			c.read_exact(&mut self.biomes)?;
		}

		// if buffer.read() {
		// 	logging.warning("Leftover data in chunk buffer")
		// }
		return Ok(());
	}

	pub fn merge(&mut self, other: Chunk) -> Option<Chunk> {
		let old_chunk = self.clone();
		for i in 0..16 {
			if ((self.bitmask >> i) & 1) != 0 {
				for x in 0..16 {
					for y in 0..16 {
						for z in 0..16 {
							self.block_states[x][(i * 16) + y][z] =
								other.block_states[x][(i * 16) + y][z];
							self.block_light[x][(i * 16) + y][z] =
								other.block_light[x][(i * 16) + y][z];
							self.sky_light[x][(i * 16) + y][z] =
								other.sky_light[x][(i * 16) + y][z];
						}
					}
				}
			}
		}
		return Some(old_chunk); //TODO: is this really we want to return?
	}

	pub fn get_slice(&self, y:u8) -> Vec<Vec<u16>> {
		let mut slice = vec![vec![0u16;16];16];
		for x in 0..16 {
			for z in 0..16 {
				slice[x][z] = self.block_states[x][y as usize][z];
			}
		}
		return slice;
	}
}

impl Clone for Chunk {
	fn clone(&self) -> Self {
		Chunk {
			x: self.x,
			z: self.z,
			bitmask: self.bitmask,
			ground_up_continuous: self.ground_up_continuous,
			block_states: self.block_states.clone(),
			block_light: self.block_light.clone(),
			sky_light: self.sky_light.clone(),
			biomes: self.biomes.clone(),
			block_entities: self.block_entities.clone(),
		}
	}
}

#[pyclass]
pub struct World {
	chunks: HashMap<(i32, i32), Chunk>,
}

#[pymethods]
impl World {
	#[new]
	pub fn new() -> Self {
		info!("Initializing world from Rust");
		World {
			chunks: HashMap::new(),
		}
	}

	pub fn __getitem__(&self, item: (i32, i32)) -> Option<Chunk> {
		return self.get(item.0, item.1);
	}

	pub fn get_block(&self, x: i32, y: i32, z: i32) -> Option<u16> {
		let mut chunk_x = x / 16;
		let mut chunk_z = z / 16;
		if chunk_x < 0 && chunk_x % 16 != 0 { chunk_x-=1; }
		if chunk_z < 0 && chunk_z % 16 != 0 { chunk_z-=1; }
		if let Some(chunk) = self.chunks.get(&(chunk_x, chunk_z)) {
			return Some(chunk.block_states[abs(x, 16) as usize][y as usize][abs(z, 16) as usize]);
		}
		None
	}

	pub fn put_block(&mut self, x: i32, y:i32, z:i32, id:u16) -> Option<u16> {
		let x_off = (x % 16) as usize; let z_off = (z % 16) as usize;
		let c = self.chunks.get_mut(&(x as i32 / 16, z as i32 / 16))?;
		let old_block = c.block_states[x_off][y as usize][z_off];
		c.block_states[x_off][y as usize][z_off] = id;
		return Some(old_block);
	}

	pub fn get(&self, x: i32, z: i32) -> Option<Chunk> {
		return Some((self.chunks.get(&(x, z))?).clone());
	}

	pub fn put(&mut self, chunk: Chunk, x: i32, z: i32, merge: bool) -> Option<Chunk> {
		info!("Adding chunk x{} z{}", x, z);
		if merge && self.chunks.contains_key(&(x, z)) {
			return self.chunks.get_mut(&(x, z)).unwrap().merge(chunk);
		} else {
			return self.chunks.insert((x, z), chunk);
		}
	}
}
