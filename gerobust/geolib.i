%module wrapped_geolib
%include "carrays.i"

// Map 2 doubles array as a Python 2-tuple
%typemap(in) double*(double temp[2]) {   // temp[2] becomes a local variable
  int i;
  if (PyTuple_Check($input)) {
    if (!PyArg_ParseTuple($input,"dd",temp,temp+1)) {
      PyErr_SetString(PyExc_TypeError,"tuple must have 2 elements");
      return NULL;
    }
    $1 = &temp[0];
  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple or a list.");
    return NULL;
  }
}

%{
#define SWIG_FILE_WITH_INIT
#include "geolib.h"
%}

void exactinit();
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
