import unittest
from src.domain.rover import Rover

class TestRover(unittest.TestCase):

    def test_avancer(self):
        rover = Rover(0, 0, 'N')
        rover.avancer()
        self.assertEqual(rover.obtenir_etat(), {'x': 0, 'y': -1, 'orientation': 'N', 'obstacle_encountered': False})

    def test_reculer(self):
        rover = Rover(0, 0, 'N')
        rover.reculer()
        self.assertEqual(rover.obtenir_etat(), {'x': 0, 'y': 1, 'orientation': 'N', 'obstacle_encountered': False})

    def test_tourner_gauche(self):
        rover = Rover(0, 0, 'N')
        rover.tourner_gauche()
        self.assertEqual(rover.obtenir_etat(), {'x': 0, 'y': 0, 'orientation': 'O', 'obstacle_encountered': False})

    def test_tourner_droite(self):
        rover = Rover(0, 0, 'N')
        rover.tourner_droite()
        self.assertEqual(rover.obtenir_etat(), {'x': 0, 'y': 0, 'orientation': 'E', 'obstacle_encountered': False})

    def test_avancer_tourner_droite(self):
        rover = Rover(0, 0, 'N')
        rover.tourner_angle(45)
        rover.avancer()
        rover.tourner_droite()
        self.assertEqual(rover.obtenir_etat(), {'x': 0.71, 'y': -0.29, 'orientation': 'E', 'obstacle_encountered': False})

    def test_rencontrer_obstacle(self):
        rover = Rover(0, 0, 'N')
        rover.rencontrer_obstacle()
        self.assertTrue(rover.obstacle_encountered)

    def test_avancer_obstacle(self):
        rover = Rover(0, 0, 'N')
        rover.rencontrer_obstacle()
        rover.avancer()
        self.assertEqual(rover.obtenir_etat(), {'x': 0, 'y': 0, 'orientation': 'N', 'obstacle_encountered': True})

    def test_reculer_obstacle(self):
        rover = Rover(0, 0, 'N')
        rover.rencontrer_obstacle()
        rover.reculer()
        self.assertEqual(rover.obtenir_etat(), {'x': 0, 'y': 0, 'orientation': 'N', 'obstacle_encountered': True})

if __name__ == '__main__':
    unittest.main()
