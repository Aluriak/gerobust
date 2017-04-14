"""Build of python module wrapping geolib.c, as defined by CFFI lib.

"""

import os
from cffi import FFI

ffi = FFI()
SOURCE = os.path.join(os.path.split(__file__)[0], 'geolib.c')

with open(SOURCE) as sfd:
    ffi.set_source("gerobust._wrapped_geolib", sfd.read(),
                   extra_compile_args=['-O3', '-frounding-math', '-fsignaling-nans'],
                   libraries=['c'])

if __name__ == "__main__":
    ffi.compile()
