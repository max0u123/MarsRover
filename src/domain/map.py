# Fichier domain/map.py

import random

class Map:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._obstacles = set()

    def generate_obstacles(self, num_obstacles):
        self._obstacles.clear()
        return self._generate_obstacles(num_obstacles)

    def _generate_obstacles(self, num_obstacles):
        return {(random.randint(0, self._width - 1), random.randint(0, self._height - 1)) for _ in range(num_obstacles)}

    def has_collision(self, x, y):
        return (x, y) in self._obstacles
