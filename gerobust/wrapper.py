"""Wrapper around geolib.c file.

"""


import os
import ctypes

from gerobust._wrapped_geolib import lib as GEOLIB


GEOLIB.exactinit()


def orientation_fast(pa:(float, float), pb:(float, float), pc:(float, float)) -> float:
    """Approximate 2D orientation test. Nonrobust.

    Return a positive value if the points pa, pb, and pc occur
    in counterclockwise order; a negative value if they occur
    in clockwise order; and zero if they are collinear.

    The result is also a rough approximation of twice the signed
    area of the triangle defined by the three points.

    Do not use exact arithmetic, therefore is quicker than orientation.

    """
    return GEOLIB.orient2dfast(pa, pb, pc)

def orientation(pa:(float, float), pb:(float, float), pc:(float, float)) -> float:
    """Adaptive exact 2D orientation test. Robust.

    Return a positive value if the points pa, pb, and pc occur
    in counterclockwise order; a negative value if they occur
    in clockwise order; and zero if they are collinear.

    The result is also a rough approximation of twice the signed
    area of the triangle defined by the three points.

    Use exact arithmetic to ensure a correct answer.
    The result returned is the determinant of a matrix.
    This determinant is here computed adaptively, in the sense that exact
    arithmetic is used only to the degree it is needed to ensure that the
    returned value has the correct sign.

    Hence, this function is usually quite fast,
    but will run more slowly when the input points are collinear or nearly so.

    """
    return GEOLIB.orient2d(pa, pb, pc)


def orientation_3d_fast(pa:(float, float), pb:(float, float),
                        pc:(float, float), pd:(float, float)) -> float:
    """Approximate 3D orientation test. Nonrobust.

    Return a positive value if the point pd lies below the
    plane passing through pa, pb, and pc; "below" is defined so
    that pa, pb, and pc appear in counterclockwise order when
    viewed from above the plane. Returns a negative value if
    pd lies above the plane. Returns zero if the points are
    coplanar. The result is also a rough approximation of six
    times the signed volume of the tetrahedron defined by the
    four points.

    Do not use exact arithmetic, therefore is quicker than orientation_3d.

    """
    return GEOLIB.orient3dfast(pa, pb,
                               pc, pd)

def orientation_3d(pa:(float, float), pb:(float, float),
                   pc:(float, float), pd:(float, float)) -> float:
    """Adaptive exact 3D orientation test. Robust.

    Return a positive value if the point pd lies below the
    plane passing through pa, pb, and pc; "below" is defined so
    that pa, pb, and pc appear in counterclockwise order when
    viewed from above the plane. Returns a negative value if
    pd lies above the plane. Returns zero if the points are
    coplanar. The result is also a rough approximation of six
    times the signed volume of the tetrahedron defined by the
    four points.

    Use exact arithmetic to ensure a correct answer.
    The result returned is the determinant of a matrix.
    This determinant is computed adaptively, in the sense that exact
    arithmetic is used only to the degree it is needed to ensure that the
    returned value has the correct sign. Hence, this function is usually quite
    fast, but will run more slowly when the input points are coplanar or
    nearly so.

    """
    return GEOLIB.orient3d(pa, pb,
                           pc, pd)


def incirclefast(pa:(float, float), pb:(float, float),
                 pc:(float, float), pd:(float, float)) -> float:
    """Approximate 2D incircle test. Nonrobust.

    Return a positive value if the point pd lies inside the
    circle passing through pa, pb, and pc; a negative value if
    it lies outside; and zero if the four points are cocircular.
    The points pa, pb, and pc must be in counterclockwise
    order, or the sign of the result will be reversed.

    Do not use exact arithmetic, therefore is quicker than incircle.

    """
    return GEOLIB.incirclefast(pa, pb,
                               pc, pd)

def incircle(pa:(float, float), pb:(float, float),
             pc:(float, float), pd:(float, float)) -> float:
    """Adaptive exact 2D incircle test. Robust.

    Return a positive value if the point pd lies inside the
    circle passing through pa, pb, and pc; a negative value if
    it lies outside; and zero if the four points are cocircular.
    The points pa, pb, and pc must be in counterclockwise
    order, or the sign of the result will be reversed.

    Use exact arithmetic to ensure a correct answer.
    The result returned is the determinant of a matrix.
    This determinant is computed adaptively,
    in the sense that exact arithmetic is used only to the degree it is needed
    to ensure that the returned value has the correct sign.
    Hence, this function is usually quite fast, but will run more slowly
    when the input points are cocircular or nearly so.

    """
    return GEOLIB.incircle(pa, pb, pc, pd)


def inspherefast(pa:(float, float), pb:(float, float), pc:(float, float),
                 pd:(float, float), pe:(float, float)) -> float:
    """Approximate 3D insphere test. Nonrobust.

    Return a positive value if the point pe lies inside the
    sphere passing through pa, pb, pc, and pd; a negative value
    if it lies outside; and zero if the five points are
    cospherical. The points pa, pb, pc, and pd must be ordered
    so that they have a positive orientation,
    or the sign of the result will be reversed.

    Do not use exact arithmetic, therefore is quicker than insphere.

    """
    return GEOLIB.inspherefast(pa, pb, pc, pd, pe)

def insphere(pa:(float, float), pb:(float, float), pc:(float, float),
             pd:(float, float), pe:(float, float)) -> float:
    """Adaptive exact 3D insphere test. Robust.

    Return a positive value if the point pe lies inside the
    sphere passing through pa, pb, pc, and pd; a negative value
    if it lies outside; and zero if the five points are
    cospherical. The points pa, pb, pc, and pd must be ordered
    so that they have a positive orientation (as defined by
    orient3d()), or the sign of the result will be reversed.

    Use exact arithmetic to ensure a correct answer.
    The result returned is the determinant of a matrix.
    This determinant is computed adaptively,
    in the sense that exact arithmetic is used only to the degree it is needed
    to ensure that the returned value has the correct sign.
    Hence, this function is usually quite fast, but will run more slowly
    when the input points are cospherical or nearly so.

    """
    return GEOLIB.insphere(pa, pb, pc, pd, pe)


# shortcuts
orientation.fast = orientation_fast
orientation_3d.fast = orientation_3d_fast
incircle.fast = incirclefast
insphere.fast = inspherefast
