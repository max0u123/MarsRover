import math
import random
import datetime

class Rover:
    def __init__(self, x, y, orientation):
        self._x = x
        self._y = y
        self.orientation = orientation
        self.obstacle_encountered = False

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def modifier_position(self, new_x, new_y):
        self._x = round(new_x, 2)
        self._y = round(new_y, 2)

    def avancer(self, obstacles):
        next_x, next_y = self._next_position(1)
        if not self._check_collision(next_x, next_y, obstacles):
            self.modifier_position(next_x, next_y)
        else:
            self.rencontrer_obstacle()

    def reculer(self, obstacles):
        next_x, next_y = self._next_position(-1)
        if not self._check_collision(next_x, next_y, obstacles):
            self.modifier_position(next_x, next_y)
        else:
            self.rencontrer_obstacle()

    def tourner_gauche(self):
        if not self.obstacle_encountered:
            orientation_map = {'N': 'O', 'O': 'S', 'S': 'E', 'E': 'N'}
            self.orientation = orientation_map[self.orientation]

    def tourner_droite(self):
        if not self.obstacle_encountered:
            orientation_map = {'N': 'E', 'E': 'S', 'S': 'O', 'O': 'N'}
            self.orientation = orientation_map[self.orientation]

    def tourner_angle(self, angle):
        if not self.obstacle_encountered:
            angle_radians = math.radians(angle)
            new_x = self.x + math.cos(angle_radians)
            new_y = self.y + math.sin(angle_radians)
            self.modifier_position(new_x, new_y)

    def rencontrer_obstacle(self):
        self.obstacle_encountered = True

    def obtenir_etat(self):
        return {'x': self.x, 'y': self.y, 'orientation': self.orientation, 'obstacle_encountered': self.obstacle_encountered}

    def reinitialiser_obstacle(self):
        self.obstacle_encountered = False 

    def _next_position(self, step):
        if self.orientation == 'N':
            return self.x, self.y - step
        elif self.orientation == 'S':
            return self.x, self.y + step
        elif self.orientation == 'E':
            return self.x + step, self.y
        elif self.orientation == 'O':
            return self.x - step, self.y

    def _check_collision(self, x, y, obstacles):
        return (round(x, 2), round(y, 2)) in obstacles
    
def print_with_timestamp(*messages):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    message = ' '.join(map(str, messages))
    print(f"[{timestamp}] {message}")

def print_input_with_timestamp(message):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}", end="")

if __name__ == "__main__":
    try:
        print_input_with_timestamp("Entrez la coordonnée x du rover : ")
        x = float(input())
    except ValueError:
        print_with_timestamp("La valeur entrée n'est pas valide. Veuillez entrer un nombre.")
        exit(1)
    
    try:
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

    print_with_timestamp("État initial du rover : {'x': "+str(round(x,2))+" 'y': "+str(round(y,2))+", 'orientation': '"+orientation+"'}")
    rover = Rover(x, y, orientation)
    
    try:
        print_input_with_timestamp("Entrez le nombre d'obstacles : ")
        num_obstacles = int(input())
    except ValueError:
        print_with_timestamp("La valeur entrée n'est pas valide. Veuillez entrer un nombre entier.")
        exit(1)

    obstacles = [{'x': random.randint(0, 10), 'y': random.randint(0, 10)} for _ in range(num_obstacles)]
    
    while not rover.obstacle_encountered:
        print_input_with_timestamp("Entrez une commande (avancer, reculer, gauche, droite, angle ,dodo) : ")
        command = input()
        if command == 'avancer':
            rover.avancer(obstacles)
        elif command == 'reculer':
            rover.reculer(obstacles)
        elif command == 'gauche':
            rover.tourner_gauche()
        elif command == 'droite':
            rover.tourner_droite()
        elif command == 'angle':
            try:
                print_input_with_timestamp("Entrez l'angle de rotation : ")
                angle = float(input())
            except ValueError:
                print_with_timestamp("La valeur entrée n'est pas valide. Veuillez entrer un nombre.")
                continue
            rover.tourner_angle(angle)
        elif command == 'dodo':
            print_with_timestamp("Le rover s'endort")
            print_with_timestamp("Dernière position du rover : {'x': ",rover.obtenir_etat()['x']," 'y': ",rover.obtenir_etat()['y'],", 'orientation': '",rover.obtenir_etat()['orientation'],"'}")
            if not rover.obstacle_encountered:
                break
        else:
            print_with_timestamp("Commande invalide - Ressayer !")
            continue
        print_with_timestamp("État actuel du rover : {'x': ",rover.obtenir_etat()['x']," 'y': ",rover.obtenir_etat()['y'],", 'orientation': '",rover.obtenir_etat()['orientation'],"'}")
            
    if command != 'dodo':
        print_with_timestamp("Obstacle rencontré à la positiion :", rover.obtenir_etat()['x'], rover.obtenir_etat()['y'])