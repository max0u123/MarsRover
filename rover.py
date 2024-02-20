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
        self._x = new_x
        self._y = new_y

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

    def obtenir_etat(self):
        return {'x': self.x, 'y': self.y, 'orientation': self.orientation}
