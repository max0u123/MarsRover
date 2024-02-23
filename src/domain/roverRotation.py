# Fichier domain/roverRotation.py

class RoverRotation:
    @staticmethod
    def rotate_left(rover):
        if not rover._obstacle_encountered:
            orientation_map = {'N': 'O', 'O': 'S', 'S': 'E', 'E': 'N'}
            rover.orientation = orientation_map[rover.orientation]

    @staticmethod
    def rotate_right(rover):
        if not rover._obstacle_encountered:
            orientation_map = {'N': 'E', 'E': 'S', 'S': 'O', 'O': 'N'}
            rover.orientation = orientation_map[rover.orientation]
