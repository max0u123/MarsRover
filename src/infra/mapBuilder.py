# Fichier infra/map_builder.py
from domain.map import Map
from utils.printing import print_input_with_timestamp, print_with_timestamp

class MapBuilder:
    def build(self):
        while True:
            try:
                print_input_with_timestamp("Entrez la largeur de la carte : ")
                width = int(input())
                print_input_with_timestamp("Entrez la hauteur de la carte : ")
                height = int(input())
                print_input_with_timestamp("Entrez le nombre d'obstacles : ")
                num_obstacles = int(input())
                if width > 0 and height > 0 and num_obstacles >= 0:
                    new_map = Map(width, height)
                    new_map.obstacles = new_map.generate_obstacles(num_obstacles)
                    return new_map
                raise ValueError
            except ValueError:
                print_with_timestamp("Les valeurs entrées ne sont pas valides. Veuillez entrer des entiers positifs.")
