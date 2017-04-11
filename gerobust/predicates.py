"""High level functions built on top of the C library.

"""


from gerobust import wrapper
from gerobust.wrapper import PREDICATES, coordinates


def counter_clockwise_fast(pa:(float, float), pb:(float, float), pc:(float, float)) -> bool:
    """Approximate 2D orientation test. Nonrobust.

    Return True if the points pa, pb, and pc occur
    in counterclockwise order ; False if they occur
    in clockwise order; and None if they are collinear.

    Do not use exact arithmetic, therefore is quicker than orientation.

    """
    orient = wrapper.orientation_fast(pa, pb, pc)
    return None if not orient else (orient > 0)

def clockwise_fast(pa:(float, float), pb:(float, float), pc:(float, float)) -> bool:
    """Approximate 2D orientation test. Nonrobust.

    Return True if the points pa, pb, and pc occur
    in clockwise order ; False if they occur
    in clockwise order; and None if they are collinear.

    Do not use exact arithmetic, therefore is quicker than orientation.

    """
    orient = wrapper.orientation_fast(pa, pb, pc)
    return None if not orient else (orient < 0)

def counter_clockwise(pa:(float, float), pb:(float, float), pc:(float, float)) -> bool:
    """Adaptive exact 2D orientation test. Robust.

    Return True if the points pa, pb, and pc occur
    in counterclockwise order ; False if they occur
    in clockwise order; and None if they are collinear.

    Use exact arithmetic to ensure a correct answer.
    Hence, this function is usually quite fast,
    but will run more slowly when the input points are collinear or nearly so.

    """
    orient = wrapper.orientation(pa, pb, pc)
    return None if not orient else (orient > 0)

def clockwise(pa:(float, float), pb:(float, float), pc:(float, float)) -> bool:
    """Adaptive exact 2D orientation test. Robust.

    Return True if the points pa, pb, and pc occur
    in counterclockwise order ; False if they occur
    in clockwise order; and None if they are collinear.

    Use exact arithmetic to ensure a correct answer.
    Hence, this function is usually quite fast,
    but will run more slowly when the input points are collinear or nearly so.

    """
    orient = wrapper.orientation(pa, pb, pc)
    return None if not orient else (orient < 0)


def orientation_3d_fast(pa:(float, float), pb:(float, float),
                        pc:(float, float), pd:(float, float)) -> bool:
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
    return PREDICATES.orient3dfast(coordinates(*pa), coordinates(*pb),
                                   coordinates(*pc), coordinates(*pd))

def orientation_3d(pa:(float, float), pb:(float, float),
                   pc:(float, float), pd:(float, float)) -> bool:
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
    return PREDICATES.orient3d(coordinates(*pa), coordinates(*pb),
                               coordinates(*pc), coordinates(*pd))


def incirclefast(pa:(float, float), pb:(float, float),
                 pc:(float, float), pd:(float, float), strict:bool=True) -> bool:
    """Approximate 2D incircle test. Nonrobust.

    Return True if the point pd lies inside the
    circle passing through pa, pb, and pc; False if
    it lies outside.

    If the four points are cocircular, returns strict.

    Do not use exact arithmetic, therefore is quicker than incircle.

    """
    return (PREDICATES.pred_incirclefast_strict if strict else PREDICATES.pred_incirclefast)(
        coordinates(*pa), coordinates(*pb), coordinates(*pc), coordinates(*pd)
    )

def incircle(pa:(float, float), pb:(float, float),
             pc:(float, float), pd:(float, float), strict:bool=True) -> bool:
    """Adaptive exact 2D incircle test. Robust.

    Return True if the point pd lies inside the
    circle passing through pa, pb, and pc; False if
    it lies outside.

    If the four points are cocircular, returns strict.

    Use exact arithmetic to ensure a correct answer.
    Hence, this function is usually quite fast, but will run more slowly
    when the input points are cocircular or nearly so.

    """
    return (PREDICATES.pred_incircle_strict if strict else PREDICATES.pred_incircle)(
        coordinates(*pa), coordinates(*pb), coordinates(*pc), coordinates(*pd)
    )


def inspherefast(pa:(float, float), pb:(float, float), pc:(float, float),
                 pd:(float, float), pe:(float, float), strict:bool=True) -> bool:
    """Approximate 3D insphere test. Nonrobust.

    Return a positive value if the point pe lies inside the
    sphere passing through pa, pb, pc, and pd; a negative value
    if it lies outside; and zero if the five points are
    cospherical. The points pa, pb, pc, and pd must be ordered
    so that they have a positive orientation,
    or the sign of the result will be reversed.

    Do not use exact arithmetic, therefore is quicker than orientation_3d.

    """
    return (PREDICATES.pred_inspherefast_strict if strict else PREDICATES.pred_inspherefast)(
        coordinates(*pa), coordinates(*pb), coordinates(*pc), coordinates(*pd), coordinates(*pe)
    )

def insphere(pa:(float, float), pb:(float, float), pc:(float, float),
             pd:(float, float), pe:(float, float), strict:bool=True) -> bool:
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
    return (PREDICATES.pred_insphere_strict if strict else PREDICATES.pred_insphere)(
        coordinates(*pa), coordinates(*pb), coordinates(*pc), coordinates(*pd), coordinates(*pe)
    )