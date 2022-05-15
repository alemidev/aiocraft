mod chunk;

use chunk::{Chunk,World,bit_pack};

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
