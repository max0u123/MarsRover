import random
from domain.map import Map
from utils.printing import print_input_with_timestamp, print_with_timestamp
from domain.rover import Rover

# Classe Infrastructure
class RoverController:
    def __init__(self):
        """
        Initialise un objet RoverController avec les attributs map et rover.

        Attributes:
            map (Map): La carte sur laquelle le rover se déplace.
            rover (Rover): Le rover contrôlé par le RoverController.
        """
        self.map = None
        self.rover = None

    def _create_map(self):
        """
        Crée une nouvelle carte en demandant à l'utilisateur d'entrer la largeur, la hauteur et le nombre d'obstacles.
        """
        try:
            print_input_with_timestamp("Entrez la largeur de la carte : ")
            width = int(input())
            print_input_with_timestamp("Entrez la hauteur de la carte : ")
            height = int(input())
            print_input_with_timestamp("Entrez le nombre d'obstacles : ")
            num_obstacles = int(input())
            if width <= 0 or height <= 0 or num_obstacles < 0:
                raise ValueError
        except ValueError:
            print_with_timestamp("Les valeurs entrées ne sont pas valides. Veuillez entrer des entiers positifs.")
            exit(1)

        self.map = Map(width, height)
        self.map.obstacles = self.map.generate_obstacles(num_obstacles)

    
    def _create_rover(self):
        """
        Crée un nouveau rover en demandant à l'utilisateur d'entrer les coordonnées et l'orientation.
        """
        try:
            print_input_with_timestamp("Entrez la coordonnée x du rover : ")
            x = float(input())
            print_input_with_timestamp("Entrez la coordonnée y du rover : ")
            y = float(input())
        except ValueError:
            print_with_timestamp("La valeur entrée n'est pas valide. Veuillez entrer un nombre.")
            exit(1)

        print_input_with_timestamp("Entrez l'orientation du rover (N, S, E ou O) : ")
        orientation = input().upper()

        while orientation not in ['N', 'S', 'E', 'O']:
            print_with_timestamp("L'orientation entrée n'est pas valide. Veuillez entrer N, S, E ou O.")
            print_input_with_timestamp("Entrez l'orientation du rover (N, S, E ou O) : ")
            orientation = input().upper()

        self.rover = Rover(x, y, orientation, obstacles=self.map.obstacles)

    def _retry_movement(self, direction):
        """
        Demande à l'utilisateur s'il souhaite réessayer un mouvement après avoir rencontré un obstacle.

        Args:
            direction (int): La direction du mouvement (1 pour avancer, -1 pour reculer).
        """
        print_with_timestamp("Déplacement impossible car obstacle. Réessayez.")
        while True:
            command = input("Voulez-vous réessayer ? (o/n): ").lower()
            if command == 'o':
                break
            elif command == 'n':
                print_with_timestamp("Fin de déplacement pour le rover en position:", self.rover.obtenir_etat())
                exit(0)
            else:
                print_with_timestamp("Commande invalide. Veuillez entrer 'o' pour oui ou 'n' pour non.")

    def _print_obstacles(self):
        """Imprime les positions des obstacles sur la carte."""
        print_with_timestamp("Positions des obstacles:")
        for obstacle in self.map.obstacles:
            print_with_timestamp(obstacle)

    def run(self):
        """Exécute le contrôleur du rover, permettant à l'utilisateur de commander les mouvements du rover."""
        self._create_map()
        self._print_obstacles()
        self._create_rover()

        while not self.rover.obstacle_encountered:
            print_with_timestamp("Position Actuelle du Rover:", self.rover.obtenir_etat())
            command = input("Entrez une commande (avancer, reculer, gauche, droite, dodo): ")
            if command == 'avancer':
                if not self.rover._check_collision(*self.rover._next_position(1)):
                    self.rover.avancer()
                else:
                    self._retry_movement(1)
            elif command == 'reculer':
                if not self.rover._check_collision(*self.rover._next_position(-1)):
                    self.rover.reculer()
                else:
                    self._retry_movement(-1)
            elif command == 'gauche':
                self.rover.tourner_gauche()
            elif command == 'droite':
                self.rover.tourner_droite()
            elif command == 'dodo':
                print_with_timestamp("The rover s'endort.")
                print_with_timestamp("Dernière position du rover:", self.rover.obtenir_etat())
