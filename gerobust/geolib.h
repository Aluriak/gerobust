#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>
#include <stdbool.h>


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
