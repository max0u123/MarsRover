# Fichier domain/roverCalculations.py

class RoverCalculations:
    @staticmethod
    def calculate_next_position(rover, step):
        if rover.orientation == 'N':
            return rover.x, rover.y - step
        if rover.orientation == 'S':
            return rover.x, rover.y + step
        if rover.orientation == 'E':
            return rover.x + step, rover.y
        if rover.orientation == 'O':
            return rover.x - step, rover.y
