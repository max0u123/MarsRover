# Fichier infra/rover_builder.py
from domain.rover import Rover
from utils.printing import print_input_with_timestamp, print_with_timestamp

class RoverBuilder:
    def __init__(self, map_instance):
        self._map = map_instance

    def build(self):
        while True:
            try:
                print_input_with_timestamp("Entrez la coordonnée x du rover : ")
                x = float(input())
                print_input_with_timestamp("Entrez la coordonnée y du rover : ")
                y = float(input())
                orientation = self._get_valid_orientation()
                return Rover(x, y, orientation, obstacles=self._map.obstacles, map=self._map)
            except ValueError:
                print_with_timestamp("La valeur entrée n'est pas valide. Veuillez entrer un nombre.")

    def _get_valid_orientation(self):
        while True:
            print_input_with_timestamp("Entrez l'orientation du rover (N, S, E ou O) : ")
            orientation = input().upper()
            if orientation in ['N', 'S', 'E', 'O']:
                return orientation
            else:
                print_with_timestamp("L'orientation entrée n'est pas valide. Veuillez entrer N, S, E ou O.")
