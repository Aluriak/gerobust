%module wrapped_geolib

%{
#define SWIG_FILE_WITH_INIT
extern void exactinit();
extern double orient2dfast(double *pa, double *pb, double *pc);
extern double orient2d(double *pa, double *pb, double *pc);
extern double orient3dfast(double *pa, double *pb, double *pc);
extern double orient3d(double *pa, double *pb, double *pc);
extern double incirclefast(double *pa, double *pb, double *pc, double *pd);
extern double incircle(double *pa, double *pb, double *pc, double *pd);
extern double inspherefast(double *pa, double *pb, double *pc, double *pd, double *pe);
extern double insphere(double *pa, double *pb, double *pc, double *pd, double *pe);
extern _Bool pred_incirclefast(double *pa, double *pb, double *pc, double *pd);
extern _Bool pred_incircle(double *pa, double *pb, double *pc, double *pd);
extern _Bool pred_incirclefast_strict(double *pa, double *pb, double *pc, double *pd);
extern _Bool pred_incircle_strict(double *pa, double *pb, double *pc, double *pd);
extern _Bool pred_inspherefast(double *pa, double *pb, double *pc, double *pd, double *pe);
extern _Bool pred_insphere(double *pa, double *pb, double *pc, double *pd, double *pe);
extern _Bool pred_inspherefast_strict(double *pa, double *pb, double *pc, double *pd, double *pe);
extern _Bool pred_insphere_strict(double *pa, double *pb, double *pc, double *pd, double *pe);
%}

extern void exactinit();
extern double orient2dfast(double *pa, double *pb, double *pc);
extern double orient2d(double *pa, double *pb, double *pc);
extern double orient3dfast(double *pa, double *pb, double *pc);
extern double orient3d(double *pa, double *pb, double *pc);
extern double incirclefast(double *pa, double *pb, double *pc, double *pd);
extern double incircle(double *pa, double *pb, double *pc, double *pd);
extern double inspherefast(double *pa, double *pb, double *pc, double *pd, double *pe);
extern double insphere(double *pa, double *pb, double *pc, double *pd, double *pe);
extern _Bool pred_incirclefast(double *pa, double *pb, double *pc, double *pd);
extern _Bool pred_incircle(double *pa, double *pb, double *pc, double *pd);
extern _Bool pred_incirclefast_strict(double *pa, double *pb, double *pc, double *pd);
extern _Bool pred_incircle_strict(double *pa, double *pb, double *pc, double *pd);
extern _Bool pred_inspherefast(double *pa, double *pb, double *pc, double *pd, double *pe);
extern _Bool pred_insphere(double *pa, double *pb, double *pc, double *pd, double *pe);
extern _Bool pred_inspherefast_strict(double *pa, double *pb, double *pc, double *pd, double *pe);
extern _Bool pred_insphere_strict(double *pa, double *pb, double *pc, double *pd, double *pe);
