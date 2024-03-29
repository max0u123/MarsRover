# Class Domain Entité
import random

class Map:
    def __init__(self, width, height):
        """
        Initialise un objet Map avec une largeur, une hauteur et une liste d'obstacles.

        Args:
            width (int): Largeur de la carte.
            height (int): Hauteur de la carte.

        Attributes:
            width (int): Largeur de la carte.
            height (int): Hauteur de la carte.
            obstacles (set): Ensemble des positions des obstacles sur la carte.
        """
        self.width = width
        self.height = height
        self.obstacles = set()

    def generate_obstacles(self, num_obstacles):
        """
        Génère un ensemble aléatoire d'obstacles sur la carte.

        Args:
            num_obstacles (int): Nombre d'obstacles à générer.

        Returns:
            set: Ensemble des positions des obstacles générés.
        """
        self.obstacles.clear()
        return {(random.randint(0, self.width - 1), random.randint(0, self.height - 1)) for _ in range(num_obstacles)}

    def check_collision(self, x, y):
        """
        Vérifie s'il y a une collision avec un obstacle aux coordonnées spécifiées.

        Args:
            x (int): Coordonnée x à vérifier.
            y (int): Coordonnée y à vérifier.

        Returns:
            bool: True s'il y a collision, False sinon.
        """
        return (x, y) in self.obstacles
