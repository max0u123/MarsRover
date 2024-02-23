# Fichier infra/command_executor.py
from domain.roverMovement import RoverMovement
from domain.roverRotation import RoverRotation
from utils.printing import print_with_timestamp

class CommandExecutor:
    def __init__(self, rover_instance):
        self._rover = rover_instance

    def execute(self, command):
        if command == 'avancer':
            RoverMovement.move_forward(self._rover)
        elif command == 'reculer':
            RoverMovement.move_backward(self._rover)
        elif command == 'gauche':
            RoverRotation.rotate_left(self._rover)
        elif command == 'droite':
            RoverRotation.rotate_right(self._rover)
        elif command == 'dodo':
            print_with_timestamp("The rover s'endort.")
            print_with_timestamp("Dernière position du rover:", self._rover.obtenir_etat())
