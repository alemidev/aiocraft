use std::io::{Cursor, Seek};

use pyo3::prelude::*;

use crate::section::{ChunkSection754, ChunkSection};

#[pyclass]
#[derive(Debug, Clone)]
pub struct Chunk {
	pub x: i32,
	pub z: i32,
	pub bitmask: u16,
	pub ground_up_continuous: bool,
	pub(crate) block_states: [[[u16; 16]; 256]; 16],
	// pub(crate) block_light: [[[u16; 16]; 256]; 16],
	// pub(crate) sky_light: [[[u16; 16]; 256]; 16],
	// pub(crate) biomes: [u16; 256],
	pub(crate) block_entities: String, // TODO less jank way to store this NBT/JSON/PyDict ...
}

#[pymethods]
impl Chunk {
	#[new]
	pub fn new(x: i32, z: i32, bitmask: u16, ground_up_continuous: bool, block_entities: String) -> Self {
		Self {
			x, z, bitmask, ground_up_continuous, block_entities,
			block_states: [[[0u16; 16]; 256]; 16],
			// block_light: [[[0u16; 16]; 256]; 16],
			// sky_light: [[[0u16; 16]; 256]; 16],
			// biomes: [0u16; 256],
		}
	}

	pub fn read(&mut self, chunk_data: Vec<u8>) -> PyResult<()> {
		let mut c = Cursor::new(chunk_data);
		c.seek(std::io::SeekFrom::Start(0)).unwrap(); // just in case
		for i in 0..16 {
			if ((self.bitmask >> i) & 1) != 0 {
				let mut section = ChunkSection754::default();
				section.read(&mut c)?;
				for ((x, y, z), state) in section {
					self.block_states[x][y + (i*16)][z] = state;
				}
			}
		}

		Ok(())
	}

	pub fn merge(&mut self, other: &Chunk) {
		for i in 0..16 {
			if ((self.bitmask >> i) & 1) != 0 {
				for x in 0..16 {
					for y in 0..16 {
						for z in 0..16 {
							self.block_states[x][(i * 16) + y][z] =
								other.block_states[x][(i * 16) + y][z];
							// self.block_light[x][(i * 16) + y][z] =
							// 	other.block_light[x][(i * 16) + y][z];
							// self.sky_light[x][(i * 16) + y][z] =
							// 	other.sky_light[x][(i * 16) + y][z];
						}
					}
				}
			}
		}
	}

	pub fn get_slice(&self, y:u8) -> Vec<Vec<u16>> {
		let mut slice = vec![vec![0u16;16];16];
		for (x, row) in self.block_states.iter().enumerate() {
			for (z, state) in row[y as usize].iter().enumerate() {
				slice[x][z] = *state;
			}
		}
		slice
	}

	pub fn get(&self, x:usize, y:usize, z:usize) -> u16 {
		self.block_states[x][y][z]
	}

	pub fn entities(&self) -> &str {
		&self.block_entities
	}
}
