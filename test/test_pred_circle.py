

import itertools
from gerobust.predicates import incircle


def test_out():
    assert not incircle((100, 100), (100, 0), (70, 10), (0, 100))
    assert not incircle((40, 60), (40, 40), (80, 10), (100, 100))

def test_in():
    assert incircle((0, 100), (100, 100), (100, 0), (70, 10))
    assert incircle((0, 10), (4, 4), (10, 0), (10, 10))
    assert incircle((0, 100), (40, 40), (100, 0), (100, 100))
    assert incircle((0, 100), (70, 10), (100, 0), (100, 100))

def test_on():
    points = (0, 100), (0, 0), (100, 0), (100, 100)
    for combi in itertools.combinations(points, r=4):
        assert not incircle(*points)
        assert incircle(*points, strict=False)


def test_aligned():
    assert not incircle((1,2), (0,2), (3,2), (1,-100))
    assert not incircle((0,2), (1,2), (3,2), (2,4))
    assert not incircle((2,1), (2,0), (2,3), (2,4))


def test_clockwise():
    # non aligned points in clockwise order
    assert not incircle((1,0), (0,1), (1,2), (3-0.1,1))
    assert incircle((1,0), (0,1), (1,2), (2-0.1,1))
    assert incircle((1,0), (0,1), (1,2), (1-0.1,1))
