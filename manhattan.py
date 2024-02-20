import unittest

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def distance_to(self, other):
        return abs(self._x - other._x) + abs(self._y - other._y)

def ManhattanDistance(pointA, pointB):
    return pointA.distance_to(pointB)

class TestPoint(unittest.TestCase):
    def test_ManhattanDistance(self):
        pointA1 = Point(1, 2)
        pointB1 = Point(1, 3)
        self.assertEqual(ManhattanDistance(pointA1, pointB1), 1)

        pointA2 = Point(1, 2)
        pointB2 = Point(1, 102)
        self.assertEqual(ManhattanDistance(pointA2, pointB2), 100)

        pointA3 = Point(1, 2)
        pointB3 = Point(101, 102)
        self.assertEqual(ManhattanDistance(pointA3, pointB3), 200)

        pointA4 = Point(1, 2)
        pointB4 = Point(-9, -18)
        self.assertEqual(ManhattanDistance(pointA4, pointB4), 30)

if __name__ == "__main__":
    unittest.main()
