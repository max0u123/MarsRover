# Fichier domain/roverMovement.py
from domain.roverCalculations import RoverCalculations
from domain.roverCollision import RoverCollision

class RoverMovement:
    @staticmethod
    def move_to(rover, x, y):
        if not RoverCollision.check_collision(rover, x, y):
            rover.modifier_position(x, y)
            return
        rover.rencontrer_obstacle()

    @staticmethod
    def move_forward(rover):
        next_x, next_y = RoverCalculations.calculate_next_position(rover, 1)
        RoverMovement.move_to(rover, next_x, next_y)

    @staticmethod
    def move_backward(rover):
        next_x, next_y = RoverCalculations.calculate_next_position(rover, -1)
        RoverMovement.move_to(rover, next_x, next_y)
