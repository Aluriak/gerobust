"""Build of python module wrapping geolib.c, as defined by CFFI lib.

"""

import os
from cffi import FFI

ffi = FFI()
SOURCE = os.path.join(os.path.split(__file__)[0], 'geolib.c')
HEADER = os.path.join(os.path.split(__file__)[0], 'geolib.h')

with open(SOURCE) as sfd, open(HEADER) as hfd:
    header = hfd.read()
    ffi.set_source("gerobust._wrapped_geolib.py", sfd.read())
# ffi.cdef(header)

if __name__ == "__main__":
    ffi.compile()
