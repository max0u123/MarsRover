# Fichier domain/roverCollision.py
from domain.coordinatesWrapper import CoordinatesWrapper
from domain.roverCalculations import RoverCalculations  # Ajout de l'import de RoverCalculations
from utils.printing import print_with_timestamp

class RoverCollision:
    @staticmethod
    def check_collision(rover, x, y):
        wrapper = CoordinatesWrapper(rover.map._width, rover.map._height)
        if wrapper.wrap_coordinates(x, y) in rover.obstacles:
            rover.rencontrer_obstacle()
            rover._retry_movement(1 if (x, y) == RoverCalculations.calculate_next_position(rover, 1) else -1)
            return True
        return False
