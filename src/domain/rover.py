# Fichier domain/rover.py
from domain.coordinatesWrapper import CoordinatesWrapper
from domain.roverCalculations import RoverCalculations
from utils.printing import print_with_timestamp

class Rover:
    def __init__(self, x, y, orientation, obstacles, map):
        self._x = x
        self._y = y
        self.orientation = orientation
        self._obstacle_encountered = False
        self.obstacles = obstacles
        self.map = map

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def modifier_position(self, new_x, new_y):
        new_x, new_y = CoordinatesWrapper(self.map._width, self.map._height).wrap_coordinates(new_x, new_y)
        self._x, self._y = new_x, new_y

    def rencontrer_obstacle(self):
        self._obstacle_encountered = True

    def obtenir_etat(self):
        return {'x': self.x, 'y': self.y, 'orientation': self.orientation, 'obstacle_encountered': self._obstacle_encountered}

    def reinitialiser_obstacle(self):
        self._obstacle_encountered = False

    def _check_collision(self, x, y):
        wrapper = CoordinatesWrapper(self.map._width, self.map._height)
        return wrapper.wrap_coordinates(x, y) in self.obstacles

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
                return direction 
            elif command == 'n':
                print_with_timestamp("Fin de déplacement pour le rover en position:", self.obtenir_etat())
                exit(0)
            else:
                print_with_timestamp("Commande invalide. Veuillez entrer 'o' pour oui ou 'n' pour non.")

    def check_collision(self, x, y):
        return self._check_collision(x, y)

    def move_to(self, x, y):
        if not self._check_collision(x, y):
            self.modifier_position(x, y)
        else:
            self.rencontrer_obstacle()
            self._retry_movement(1 if (x, y) == RoverCalculations.calculate_next_position(self, 1) else -1)

    def move_forward(self):
        next_x, next_y = RoverCalculations.calculate_next_position(self, 1)
        self.move_to(next_x, next_y)

    def move_backward(self):
        next_x, next_y = RoverCalculations.calculate_next_position(self, -1)
        self.move_to(next_x, next_y)
