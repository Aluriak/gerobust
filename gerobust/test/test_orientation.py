

from gerobust import orientation


def test_point_in_clockwise_order():
    points = (0, 0), (0, 50), (50, 50), (50, 0)
    assert orientation(points) == -orientation(reversed(points))
    assert     point_in_clockwise_order(points)
    assert not point_in_counter_clockwise_order(points)
    assert not point_in_clockwise_order(reversed(points))
    assert     point_in_counter_clockwise_order(reversed(points))

def test_point_in_clockwise_order_2():
    points = (0, 0), (50, 50), (100, 0)
    assert orientation(points) == -orientation(reversed(points))
    assert     point_in_clockwise_order(points)
    assert not point_in_counter_clockwise_order(points)
    assert not point_in_clockwise_order(reversed(points))
    assert     point_in_counter_clockwise_order(reversed(points))

def test_point_in_counter_clockwise_order():
    points = (0, 0), (100, 0), (50, 50)
    assert orientation(points) == -orientation(reversed(points))
    assert not point_in_clockwise_order(points)
    assert     point_in_counter_clockwise_order(points)
    assert     point_in_clockwise_order(tuple(reversed(points)))
    assert not point_in_counter_clockwise_order(tuple(reversed(points)))


def test_orientation():
    points = (5,0), (6,4), (4,5), (1,5), (1,0)
    assert orientation(points) == -22
    assert point_in_counter_clockwise_order(points)
    assert orientation(reversed(points)) == 22
    assert point_in_clockwise_order(reversed(points))


def test_orientation_2():
    points = (3, 4), (5, 11), (12, 8), (9, 5), (5, 6), (3, 4)
    assert orientation(points) == 30
    assert point_in_clockwise_order(points)
    assert orientation(reversed(points)) == -30
    assert not point_in_clockwise_order(reversed(points))
