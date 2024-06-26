from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    version='1.0.0',  # Specify the version here
    rust_extensions=[RustExtension('sqlite_zstd.libsqlite_zstd',
        path='/app/sqlite-zstd/Cargo.toml',
        binding=Binding.NoBinding,
        features=['build_extension'],
        py_limited_api=True,
    )],
)