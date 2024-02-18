from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='O',
    ext_modules=cythonize(module_list="shelcode.py"),
)