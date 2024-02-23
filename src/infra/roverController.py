# Fichier infra/roverController.py
from domain.map import Map
from utils.printing import print_input_with_timestamp, print_with_timestamp
from domain.rover import Rover
from domain.roverCalculations import RoverCalculations
from domain.roverCollision import RoverCollision
from domain.roverMovement import RoverMovement
from domain.roverRotation import RoverRotation
from infra.mapBuilder import MapBuilder
from infra.roverBuilder import RoverBuilder
from infra.commandExecutor import CommandExecutor

class RoverController:
    def __init__(self):
        self._map = None
        self._rover = None

    def run(self):
        self._create_map()
        self._print_obstacles()
        self._create_rover()

        while not self._rover._obstacle_encountered:
            print_with_timestamp("Position Actuelle du Rover:", self._rover.obtenir_etat())
            command = input("Entrez une commande (avancer, reculer, gauche, droite, dodo): ")
            self._execute_command(command)

    def _create_map(self):
        self._map = MapBuilder().build()

    def _create_rover(self):
        self._rover = RoverBuilder(self._map).build()

    def _print_obstacles(self):
        print_with_timestamp("Positions des obstacles:")
        for obstacle in self._map.obstacles:
            print_with_timestamp(obstacle)

    def _execute_command(self, command):
        CommandExecutor(self._rover).execute(command)