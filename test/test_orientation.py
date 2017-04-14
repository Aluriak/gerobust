

import itertools
from collections import deque

import pytest
from gerobust import orientation
from gerobust import counter_clockwise, clockwise


def sliding(it:iter, size:int) -> iter:
    it = iter(it)
    acc = deque(itertools.islice(it, 0, size), maxlen=size)
    yield tuple(acc)
    for item in it:
        acc.append(item)
        yield tuple(acc)

def test_sliding():
    assert ((1, 2, 3), (2, 3, 4)) == tuple(sliding((1, 2, 3, 4), size=3))

def test_list_usage():
    assert orientation([0, 0], [0, 50], [50, 50])

def test_clockwise():
    points = (0, 0), (0, 50), (50, 50)
    assert orientation(*points) == -orientation(*reversed(points))
    assert     clockwise(*points)
    assert not counter_clockwise(*points)
    assert not clockwise(*reversed(points))
    assert     counter_clockwise(*reversed(points))

def test_clockwise_2():
    points = (0, 0), (50, 50), (100, 0)
    assert orientation(*points) == -orientation(*reversed(points))
    assert     clockwise(*points)
    assert not counter_clockwise(*points)
    assert not clockwise(*reversed(points))
    assert     counter_clockwise(*reversed(points))

def test_counter_clockwise():
    points = (0, 0), (100, 0), (50, 50)
    assert orientation(*points) == -orientation(*reversed(points))
    assert not clockwise(*points)
    assert     counter_clockwise(*points)
    assert     clockwise(*reversed(points))
    assert not counter_clockwise(*reversed(points))


def test_orientation():
    points = (5,0), (6,4), (4,5)
    assert counter_clockwise(*points)
    assert clockwise(*reversed(points))


def test_orientation_2():
    triangles = (
        ((3, 4), (5, 6), (9, 5), True),
        ((5, 6), (9, 5), (12, 8), False),
        ((9, 5), (12, 8), (5, 11), False),
        ((12, 8), (5, 11), (3, 4), False),
    )
    for *points, is_clockwise in triangles:
         # = triangle
        assert clockwise(*points) is is_clockwise
        assert counter_clockwise(*points) is not is_clockwise
        assert clockwise(*reversed(points)) is not is_clockwise
        assert counter_clockwise(*reversed(points)) is is_clockwise
