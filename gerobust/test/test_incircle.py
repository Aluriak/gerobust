

import itertools
from gerobust import incircle


def test_out():
    assert incircle((100, 100), (70, 10), (100, 0), (0, 100)) < 0
    assert incircle((40, 60), (40, 40), (80, 10), (100, 100)) < 0

def test_out_reversed():
    assert incircle((100, 100), (100, 0), (70, 10), (0, 100)) > 0
    assert incircle((40, 60), (80, 10), (40, 40), (100, 100)) > 0

def test_in():
    assert incircle((0, 10), (4, 4), (10, 0), (10, 10))       > 0
    assert incircle((0, 100), (100, 0), (100, 100), (70, 10)) > 0
    assert incircle((0, 100), (40, 40), (100, 0), (100, 100)) > 0
    assert incircle((0, 100), (70, 10), (100, 0), (100, 100)) > 0

def test_in_reversed():
    # results are reversed because points are not in counter clockwise order
    assert incircle((0, 10), (10, 0), (4, 4), (10, 10))       < 0
    assert incircle((0, 100), (100, 100), (100, 0), (70, 10)) < 0
    assert incircle((0, 100), (100, 0), (40, 40), (100, 100)) < 0
    assert incircle((0, 100), (100, 0), (70, 10), (100, 100)) < 0

def test_on():
    points = (0, 100), (0, 0), (100, 0), (100, 100)
    for combi in itertools.combinations(points, r=4):
        assert incircle(*points) == 0.


def test_aligned():
    assert incircle((1,2), (0,2), (3,2), (1,-100)) > 0
    assert incircle((0,2), (1,2), (3,2), (2,4)) > 0
    assert incircle((2,1), (2,0), (2,3), (2,4)) == 0.


def test_counter_clockwise():
    # non aligned points in counter-clockwise order
    assert incircle((1,0), (1,2), (0,1), (1-0.1,1)) > 0
    assert incircle((1,0), (1,2), (0,1), (2-0.1,1)) > 0
    assert incircle((1,0), (1,2), (0,1), (    2,1)) == 0.
    assert incircle((1,0), (1,2), (0,1), (3-0.1,1)) < 0
