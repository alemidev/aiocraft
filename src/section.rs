use std::io::{Read, ErrorKind};

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
pub struct ChunkSectionModern {
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

impl ChunkSectionModern {
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

impl Iterator for ChunkSectionModern {
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

impl ChunkSection for ChunkSectionModern {
	fn read<R: Read>(&mut self, buffer: &mut R) -> PyResult<()> {
		let mut block_count_buf: [u8; 2] = [0; 2];
		buffer.read_exact(&mut block_count_buf)?;
		self.block_count = i16::from_be_bytes(block_count_buf);
		log::info!("block count is {}", self.block_count);

		let mut bits_per_block_buf: [u8; 1] = [0u8; 1];
		buffer.read_exact(&mut bits_per_block_buf)?;
		self.bits_per_block = u8::from_be_bytes(bits_per_block_buf);
		log::info!("bits per block is {}", self.bits_per_block);
		self.bits_per_block = match self.bits_per_block {
			0..=4 => 4,
			5..=8 => self.bits_per_block,
			9..   => ChunkSectionModern::max_bits(),
		};

		self.palette = Vec::new();
		if self.bits_per_block < 9 {
			let palette_len_buf = read_varint(buffer)?;
			for _ in 0..palette_len_buf {
				self.palette.push(read_varint(buffer)?);
			}
		}
		log::info!("palette of len {}: {:?}", self.palette.len(), self.palette);

		let content_len = read_varint(buffer)? as usize;
		log::info!("reading {} longs from buffer ({} bytes)", content_len, content_len * 8);

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

#[allow(unused)]
fn read_paletted_container<R: Read>(buffer: &mut R) -> PyResult<[[[u16; 16]; 16]; 16]> {
	let mut data: [u8; 1] = [0u8; 1];
	buffer.read_exact(&mut data)?;
	// bits = UnsignedByte.read(buffer, ctx=ctx) # FIXME if bits > 4 it reads trash
	// #logging.debug("[%d|%d@%d] Bits per block : %d", ctx.x, ctx.z, ctx.sec, bits)
	let bits_raw = u8::from_be_bytes(data);
	let bits = match bits_raw {
		0     => 0,
		1..=4 => 4,
		5..=8 => bits_raw,
		9..   => 13, // this should not be hardcoded but we have no way to calculate all possible block states
	};
	log::info!("bits per block: {} -> {}", bits_raw, bits);
	let palette_len = read_varint(buffer)?;
	log::info!("palette len: {}", palette_len);
	if bits == 0 { // single value palette: the length is the actual value and it fills the chunk
		let _container_size = read_varint(buffer)? as usize; // this is still sent
		assert_eq!(_container_size, 0);
		return Ok([[[palette_len as u16; 16]; 16]; 16]);
	}
	let mut palette = vec![0; palette_len as usize];
	for p in 0..palette_len as usize {
		palette[p] = read_varint(buffer)?;
	}
	// # logging.debug("[%d|%d@%d] Palette section : [%d] %s", ctx.x, ctx.z, ctx.sec, palette_len, str(palette))
	let container_size = read_varint(buffer)? as usize;
	log::info!("reading off socket {}x8 = {} bytes (palette of {} bits)", container_size, container_size * 8, bits);
	let mut block_data_buffer = vec![0u8; container_size * 8];
	buffer.read_exact(&mut block_data_buffer)?;
	let block_data : Vec<u64> = block_data_buffer
		.chunks_exact(8)
		.map(|x| u64::from_be_bytes(x.try_into().unwrap())) // wtf rust!!!
		.collect();
	let mut section = [[[0u16; 16]; 16]; 16];
	let max_val: u16 = (1 << bits) - 1;
	let mut i = 0;
	for y in 0..16 {
		for z in 0..16 {
			for x in 0..16 {
				// let i = (y * 16 * 16) + (z * 16) + x;
				let start_byte = (i * bits as usize) / 64;
				let start_offset = (i * bits as usize) % 64;
				let end_byte = ((i + 1) * bits as usize) / 64;
				if start_byte >= container_size || end_byte >= container_size {
					log::warn!("early exit? is this ok?");
					return Ok(section); // early exit? is this OK?
				}
				let value: u16;
				if start_byte == end_byte {
					value = ((block_data[start_byte as usize] //FIXME out of bounds?
						>> start_offset) & max_val as u64) as u16;
				} else {
					let end_offset = 64 - start_offset;
					value = (((block_data[start_byte as usize] as usize)
						>> start_offset
						| (block_data[end_byte as usize] as usize) << end_offset) // FIXME: out of bounds?
						& max_val as usize) as u16;
				}
				if bits == 13 {
					section[x][y][z] = value;
				} else if value as i32 >= palette_len {
					log::warn!("index out of palette bounds : {}/{} (bits {})", value, palette_len, bits);
					section[x][y][z] = value;
				} else {
					section[x][y][z] = palette[value as usize] as u16;
				}

				i += 1;
			}
		}
	}
	return Ok(section);
}
