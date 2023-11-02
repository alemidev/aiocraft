mod chunk;
mod world;
mod section;

use chunk::Chunk;
use world::World;

use pyo3::prelude::*;

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn aiocraft(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
	pyo3_log::init();
	// let native = PyModule::new(_py, "native")?;
	m.add_function(wrap_pyfunction!(bit_pack, _py)?)?;
	m.add_class::<Chunk>()?;
	m.add_class::<World>()?;
	// m.add_submodule(native)?;
	Ok(())
}

fn abs(v:i32, modulo:i32) -> i32 {
	if v < 0 {
		return (modulo + (v % modulo)) % modulo;
	} else {
		return v % modulo;
	}
}

#[pyfunction]
pub fn bit_pack(data: Vec<i32>, bits: i32, size: i32) -> PyResult<Vec<i32>> {
	if size <= bits {
		return Err(pyo3::exceptions::PyValueError::new_err(
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
