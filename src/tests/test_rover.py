import unittest
from domain.rover import Rover
from domain.map import Map

class TestRover(unittest.TestCase):
    def setUp(self):
        self.map = Map(width=10, height=10)
        self.rover = Rover(x=5, y=5, orientation='N', obstacles=[], map=self.map)

    def test_move_forward_no_collision(self):
        self.rover.move_forward()
        self.assertEqual(self.rover.obtenir_etat(), {'x': 5, 'y': 4, 'orientation': 'N', 'obstacle_encountered': False})

    def test_move_forward_collision(self):
        self.rover.obstacles.append((5, 3))
        self.rover.move_forward()
        self.assertEqual(self.rover.obtenir_etat(), {'x': 5, 'y': 4, 'orientation': 'N', 'obstacle_encountered': True})


if __name__ == '__main__':
    unittest.main()
