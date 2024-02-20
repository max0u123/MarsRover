import unittest
from rover import Rover

class TestRover(unittest.TestCase):

    def test_avancer(self):
        rover = Rover(0, 0, 'N')
        rover.avancer()
        self.assertEqual(rover.obtenir_etat(), {'x': 0, 'y': -1, 'orientation': 'N'})

    def test_tourner_gauche(self):
        rover = Rover(0, 0, 'N')
        rover.tourner_gauche()
        self.assertEqual(rover.obtenir_etat(), {'x': 0, 'y': 0, 'orientation': 'O'})

    def test_avancer_tourner_droite(self):
        rover = Rover(0, 0, 'N')
        rover.avancer()
        rover.tourner_droite()
        self.assertEqual(rover.obtenir_etat(), {'x': 0, 'y': -1, 'orientation': 'E'})

if __name__ == '__main__':
    unittest.main()
