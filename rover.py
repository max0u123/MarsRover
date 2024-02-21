import math

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
        #corriger pour avoir le bon y 
        return (round(x, 2), round(y, 2)) in obstacles

if __name__ == "__main__":
    x = float(input("Entrez la coordonnée x du rover : "))
    y = float(input("Entrez la coordonnée y du rover : "))
    orientation = input("Entrez l'orientation du rover (N, S, E ou O) : ")
    print("État initial du rover : {'x': "+str(round(x,2))+" 'y': "+str(round(y,2))+", 'orientation': '"+orientation+"'}")
    rover = Rover(x, y, orientation)

    obstacles = [(2, 2), (3, 3), (4, 4)]

    rover.reculer(obstacles)
    print(rover.obtenir_etat())
    rover.tourner_angle(300)
    rover.avancer(obstacles)

    if rover.obstacle_encountered:
        print("Obstacle rencontré à la position :", rover.obtenir_etat()['x'], rover.obtenir_etat()['y'])
    else:
        print("Aucun obstacle rencontré. État final du rover :", rover.obtenir_etat())

    rover.reinitialiser_obstacle()
