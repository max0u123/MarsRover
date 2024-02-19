class Rover:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def avancer(self):
        if self.orientation == 'N':
            self.y -= 1
        elif self.orientation == 'S':
            self.y += 1
        elif self.orientation == 'E':
            self.x += 1
        elif self.orientation == 'O':
            self.x -= 1

    def reculer(self):
        if self.orientation == 'N':
            self.y += 1
        elif self.orientation == 'S':
            self.y -= 1
        elif self.orientation == 'E':
            self.x -= 1
        elif self.orientation == 'O':
            self.x += 1

    def tourner_gauche(self):
        orientation_map = {'N': 'O', 'O': 'S', 'S': 'E', 'E': 'N'}
        self.orientation = orientation_map[self.orientation]

    def tourner_droite(self):
        orientation_map = {'N': 'E', 'E': 'S', 'S': 'O', 'O': 'N'}
        self.orientation = orientation_map[self.orientation]

    def obtenir_etat(self):
        return {'x': self.x, 'y': self.y, 'orientation': self.orientation}
