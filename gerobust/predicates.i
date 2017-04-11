%module wrapped_predicates

%{
#define SWIG_FILE_WITH_INIT
#define REAL double
extern void exactinit();
extern REAL orient2dfast(REAL *pa, REAL *pb, REAL *pc);
extern REAL orient2d(REAL *pa, REAL *pb, REAL *pc);
extern REAL orient3dfast(REAL *pa, REAL *pb, REAL *pc);
extern REAL orient3d(REAL *pa, REAL *pb, REAL *pc);
extern REAL incirclefast(REAL *pa, REAL *pb, REAL *pc, REAL *pd);
extern REAL incircle(REAL *pa, REAL *pb, REAL *pc, REAL *pd);
extern REAL inspherefast(REAL *pa, REAL *pb, REAL *pc, REAL *pd, REAL *pe);
extern REAL insphere(REAL *pa, REAL *pb, REAL *pc, REAL *pd, REAL *pe);
%}

extern void exactinit();
extern REAL orient2dfast(REAL *pa, REAL *pb, REAL *pc);
extern REAL orient2d(REAL *pa, REAL *pb, REAL *pc);
extern REAL orient3dfast(REAL *pa, REAL *pb, REAL *pc);
extern REAL orient3d(REAL *pa, REAL *pb, REAL *pc);
extern REAL incirclefast(REAL *pa, REAL *pb, REAL *pc, REAL *pd);
extern REAL incircle(REAL *pa, REAL *pb, REAL *pc, REAL *pd);
extern REAL inspherefast(REAL *pa, REAL *pb, REAL *pc, REAL *pd, REAL *pe);
extern REAL insphere(REAL *pa, REAL *pb, REAL *pc, REAL *pd, REAL *pe);
