use std::collections::HashMap;

use pyo3::prelude::*;

use crate::{chunk::Chunk, abs};

#[pyclass]
pub struct World {
	chunks: HashMap<(i32, i32), Chunk>,
}

#[pymethods]
impl World {
	#[new]
	pub fn new() -> Self {
		log::info!("Initializing world from Rust");
		World {
			chunks: HashMap::new(),
		}
	}

	pub fn __getitem__(&self, item: (i32, i32)) -> Option<Chunk> {
		return self.get(item.0, item.1);
	}

	pub fn get_block(&self, x: i32, y: i32, z: i32) -> Option<u16> {
		if y < 0 {
			return Some(0); // TODO no longer the case after 1.17
		}
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
		if y < 0 {
			return Some(0);
		}
		let mut chunk_x = x / 16;
		let mut chunk_z = z / 16;
		if chunk_x < 0 && chunk_x % 16 != 0 { chunk_x-=1; }
		if chunk_z < 0 && chunk_z % 16 != 0 { chunk_z-=1; }
		let x_off = abs(x, 16) as usize; let z_off = abs(z, 16) as usize;
		let c = self.chunks.get_mut(&(chunk_x, chunk_z))?;
		let old_block = c.block_states[x_off][y as usize][z_off];
		c.block_states[x_off][y as usize][z_off] = id;
		return Some(old_block);
	}

	pub fn get(&self, x: i32, z: i32) -> Option<Chunk> {
		return Some((self.chunks.get(&(x, z))?).clone());
	}

	pub fn put(&mut self, chunk: Chunk, x: i32, z: i32, merge: bool) -> Option<Chunk> {
		if merge && self.chunks.contains_key(&(x, z)) {
			return self.chunks.get_mut(&(x, z)).unwrap().merge(chunk);
		} else {
			return self.chunks.insert((x, z), chunk);
		}
	}
}
