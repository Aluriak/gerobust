"""Build of python module wrapping geolib.c, as defined by CFFI lib.

"""

import os
from cffi import FFI

ffi = FFI()
SOURCE = os.path.join(os.path.split(__file__)[0], 'geolib.c')

ffi.cdef("""
void exactinit(void);
double orient2dfast(double *pa, double *pb, double *pc);
double orient2d(double *pa, double *pb, double *pc);
double orient3dfast(double *pa, double *pb, double *pc, double *pd);
double orient3d(double *pa, double *pb, double *pc, double *pd);
double incirclefast(double *pa, double *pb, double *pc, double *pd);
double incircle(double *pa, double *pb, double *pc, double *pd);
double inspherefast(double *pa, double *pb, double *pc, double *pd, double *pe);
double insphere(double *pa, double *pb, double *pc, double *pd, double *pe);
bool pred_incirclefast(double *pa, double *pb, double *pc, double *pd);
bool pred_incircle(double *pa, double *pb, double *pc, double *pd);
bool pred_incirclefast_strict(double *pa, double *pb, double *pc, double *pd);
bool pred_incircle_strict(double *pa, double *pb, double *pc, double *pd);
bool pred_inspherefast(double *pa, double *pb, double *pc, double *pd, double *pe);
bool pred_insphere(double *pa, double *pb, double *pc, double *pd, double *pe);
bool pred_inspherefast_strict(double *pa, double *pb, double *pc, double *pd, double *pe);
bool pred_insphere_strict(double *pa, double *pb, double *pc, double *pd, double *pe);
""")

with open(SOURCE) as sfd:
    ffi.set_source("gerobust._wrapped_geolib", sfd.read(),
                   extra_compile_args=['-O3', '-frounding-math', '-fsignaling-nans'],
                   libraries=['c'])

if __name__ == "__main__":
    ffi.compile()
