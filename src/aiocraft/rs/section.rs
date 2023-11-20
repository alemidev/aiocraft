use std::io::Read;

use pyo3::prelude::*;

fn read_varint<R: Read>(buffer: &mut R) -> PyResult<i32> {
	let mut num_read = 0;
	let mut result: i32 = 0;
	loop {
		let mut data: [u8; 1] = [0u8; 1];
		buffer.read_exact(&mut data)?;
		result |= ((data[0] & 0b01111111) as i32) << (7 * num_read);
		num_read += 1;
		if num_read > 4 {
			return Err(pyo3::exceptions::PyValueError::new_err("VarInt too big"));
		}
		if data[0] & 0b10000000 == 0 {
			break;
		}
	}
	Ok(result)
}

pub trait ChunkSection : Default + Iterator {
	fn read<R: Read>(&mut self, chunk_data: &mut R) -> PyResult<()>;
	fn max_bits() -> u8;
}

#[derive(Debug, Clone, Default)]
pub struct ChunkSection754 {
	pub block_count: i16,
	pub bits_per_block: u8,
	pub palette: Vec<i32>,
	pub data: Vec<u64>,
	count: usize,
	bits: usize,
	x: usize,
	z: usize,
	y: usize,
}

impl ChunkSection754 {
	fn count_up_coordinates(&mut self) {
		self.x += 1;
		if self.x >= 16 {
			self.z += 1;
			self.x = 0;
		}
		if self.z >= 16 {
			self.y += 1;
			self.z = 0;
		}
	}
}

impl Iterator for ChunkSection754 {
	type Item = ((usize, usize, usize), u16);

	fn next(&mut self) -> Option<Self::Item> {
		if self.count >= 4096 { return None };
		if self.bits % 64 > 64 - self.bits_per_block as usize {
			self.bits += 64 - (self.bits % 64);
		}
		let start_byte = self.bits / 64;
		let start_offset = self.bits % 64;
		let end_byte = (self.bits + self.bits_per_block as usize - 1) / 64;
		let max_val = (1_u64 << self.bits_per_block) - 1_u64;
		let value = if start_byte == end_byte { // just discard from start and end
			(self.data[start_byte] >> start_offset) & max_val // FIXME out of bounds?
		} else {
			log::warn!("block spread across two longs, this shouldn't happen");
			let end_offset = 64 - start_offset;
			(self.data[start_byte] >> start_offset) | (self.data[end_byte] << end_offset) & max_val // FIXME: out of bounds?
		};

		self.bits += self.bits_per_block as usize;
		self.count += 1;

		let coord = (self.x, self.y, self.z);
		self.count_up_coordinates();

		let state = if self.bits_per_block >= 9 {
			value as u16
		} else {
			self.palette[value as usize] as u16
		};

		Some((coord, state))
	}
}

impl ChunkSection for ChunkSection754 {
	fn read<R: Read>(&mut self, buffer: &mut R) -> PyResult<()> {
		let mut block_count_buf: [u8; 2] = [0; 2];
		buffer.read_exact(&mut block_count_buf)?;
		self.block_count = i16::from_be_bytes(block_count_buf);

		let mut bits_per_block_buf: [u8; 1] = [0u8; 1];
		buffer.read_exact(&mut bits_per_block_buf)?;
		self.bits_per_block = u8::from_be_bytes(bits_per_block_buf);
		self.bits_per_block = match self.bits_per_block {
			0..=4 => 4,
			5..=8 => self.bits_per_block,
			9..   => ChunkSection754::max_bits(),
		};

		self.palette = Vec::new();
		if self.bits_per_block < 9 {
			let palette_len_buf = read_varint(buffer)?;
			for _ in 0..palette_len_buf {
				self.palette.push(read_varint(buffer)?);
			}
		}

		let content_len = read_varint(buffer)? as usize;

		let mut data_buf = vec![0u8; content_len * 8];
		buffer.read_exact(&mut data_buf)?;

		self.data = data_buf.chunks(8)
			.map(|x| u64::from_be_bytes(x.try_into().unwrap())) // wtf rust!!!
			.collect();

		self.bits = 0;
		self.count = 0;

		Ok(())
	}

	#[inline]
	fn max_bits() -> u8 {
		15
	}
}





#[allow(unused)]
pub struct ChunkSection340 {
	pub block_states: [[[u16; 16]; 16]; 16],
	pub block_light: [[[u16; 16]; 16]; 16],
	pub sky_light: Option<[[[u16; 16]; 16]; 16]>,
}
