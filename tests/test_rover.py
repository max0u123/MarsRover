import unittest
import random
from src.domain.rover import Rover

class TestRover(unittest.TestCase):
    def setUp(self):
        num_obstacles = random.randint(0, 5)
        self.obstacles = {(random.randint(0, 9), random.randint(0, 9)) for _ in range(num_obstacles)}
        map_size = random.randint(5, 15)
        self.map = [['.' for _ in range(map_size)] for _ in range(map_size)]

    def test_avancer(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        temoin = Rover(0, 0, 'N', self.obstacles, self.map)
        rover.avancer()
        temoin.avancer()
        self.assertEqual(rover.obtenir_etat(), temoin.obtenir_etat())

    def test_reculer(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        temoin = Rover(0, 0, 'N', self.obstacles, self.map)
        rover.reculer()
        temoin.reculer()
        self.assertEqual(rover.obtenir_etat(), temoin.obtenir_etat())

    def test_tourner_droite(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        temoin = Rover(0, 0, 'N', self.obstacles, self.map)
        rover.tourner_droite()
        temoin.tourner_droite()
        self.assertEqual(rover.obtenir_etat(), temoin.obtenir_etat())

    def test_tourner_gauche(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        temoin = Rover(0, 0, 'N', self.obstacles, self.map)
        rover.tourner_gauche()
        temoin.tourner_gauche()
        self.assertEqual(rover.obtenir_etat(), temoin.obtenir_etat())

    def test_avancer_obstacle(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        temoin = Rover(0, 0, 'N', self.obstacles, self.map)
        rover.avancer()
        self.assertEqual(rover.obtenir_etat(), temoin.obtenir_etat())

    def test_reculer_obstacle(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        temoin = Rover(0, 0, 'N', self.obstacles, self.map)
        rover.reculer()
        self.assertEqual(rover.obtenir_etat(), temoin.obtenir_etat())

    def test_rencontrer_obstacle(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        temoin = Rover(0, 0, 'N', self.obstacles, self.map)
        rover.rencontrer_obstacle()
        self.assertEqual(rover.obtenir_etat(), temoin.obtenir_etat())

    def test_avancer_tourner_droite(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        temoin = Rover(0, 0, 'N', self.obstacles, self.map)
        rover.reinitialiser_obstacle()
        temoin.reinitialiser_obstacle()
        rover.avancer()
        rover.tourner_droite()
        temoin.avancer()
        temoin.tourner_droite()
        self.assertEqual(rover.obtenir_etat(), temoin.obtenir_etat())

if __name__ == '__main__':
    unittest.main()
