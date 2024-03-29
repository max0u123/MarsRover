import unittest
import random  # Importez le module random pour générer des nombres aléatoires
from src.domain.rover import Rover

class TestRover(unittest.TestCase):
    def setUp(self):
        # Générez aléatoirement le nombre d'obstacles (entre 0 et 5)
        num_obstacles = random.randint(0, 5)

        # Générez aléatoirement les coordonnées des obstacles
        self.obstacles = [(random.randint(0, 9), random.randint(0, 9)) for _ in range(num_obstacles)]

        # Générez aléatoirement la taille de la carte (entre 5 et 15)
        map_size = random.randint(5, 15)
        self.map = [['.' for _ in range(map_size)] for _ in range(map_size)]

    def test_avancer(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        # Testez le comportement attendu lorsque le rover avance

    def test_reculer(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        # Testez le comportement attendu lorsque le rover recule

    def test_tourner_droite(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        # Testez le comportement attendu lorsque le rover tourne à droite

    def test_tourner_gauche(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        # Testez le comportement attendu lorsque le rover tourne à gauche

    def test_avancer_obstacle(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        # Testez le comportement attendu lorsque le rover avance et rencontre un obstacle

    def test_reculer_obstacle(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        # Testez le comportement attendu lorsque le rover recule et rencontre un obstacle

    def test_rencontrer_obstacle(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        # Testez le comportement attendu lorsque le rover rencontre un obstacle

    def test_avancer_tourner_droite(self):
        rover = Rover(0, 0, 'N', self.obstacles, self.map)
        # Testez le comportement attendu lorsque le rover avance puis tourne à droite

if __name__ == '__main__':
    unittest.main()
