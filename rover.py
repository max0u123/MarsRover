import math

class Rover:
    def __init__(self, x, y, orientation):
        self._x = x
        self._y = y
        self.orientation = orientation

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def modifier_position(self, new_x, new_y):
        self._x = round(new_x, 2)
        self._y = round(new_y, 2)

    def avancer(self):
        if self.orientation == 'N':
            self.modifier_position(self.x, self.y - 1)
        elif self.orientation == 'S':
            self.modifier_position(self.x, self.y + 1)
        elif self.orientation == 'E':
            self.modifier_position(self.x + 1, self.y)
        elif self.orientation == 'O':
            self.modifier_position(self.x - 1, self.y)

    def reculer(self):
        if self.orientation == 'N':
            self.modifier_position(self.x, self.y + 1)
        elif self.orientation == 'S':
            self.modifier_position(self.x, self.y - 1)
        elif self.orientation == 'E':
            self.modifier_position(self.x - 1, self.y)
        elif self.orientation == 'O':
            self.modifier_position(self.x + 1, self.y)

    def tourner_gauche(self):
        orientation_map = {'N': 'O', 'O': 'S', 'S': 'E', 'E': 'N'}
        self.orientation = orientation_map[self.orientation]

    def tourner_droite(self):
        orientation_map = {'N': 'E', 'E': 'S', 'S': 'O', 'O': 'N'}
        self.orientation = orientation_map[self.orientation]

    def tourner_angle(self, angle):
        angle_radians = math.radians(angle)
        new_x = self.x + math.cos(angle_radians)
        new_y = self.y + math.sin(angle_radians)
        self.modifier_position(new_x, new_y)

    def obtenir_etat(self):
        return {'x': self.x, 'y': self.y, 'orientation': self.orientation}

if __name__ == "__main__":
    x = float(input("Entrez la coordonnée x du rover : "))
    y = float(input("Entrez la coordonnée y du rover : "))
    orientation = input("Entrez l'orientation du rover (N, S, E ou O) : ")
    print("État initial du rover : {'x': "+str(round(x,2))+" 'y': "+str(round(y,2))+", 'orientation': '"+orientation+"'}")
    rover = Rover(x, y, orientation)
#######INSTRUCTIONS##########
    rover.reculer()
    rover.tourner_angle(300)
    rover.avancer()
#############################
    print("État final du rover   :"  , rover.obtenir_etat())
