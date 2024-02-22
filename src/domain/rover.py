#Class Domain Entité - Objet
class Rover:
    def __init__(self, x, y, orientation, obstacles):
        self._x = x
        self._y = y
        self.orientation = orientation
        self.obstacle_encountered = False
        self.obstacles = obstacles

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
        next_x, next_y = self._next_position(1)
        if not self._check_collision(next_x, next_y):
            self.modifier_position(next_x, next_y)
        else:
            self.rencontrer_obstacle()

    def reculer(self):
        next_x, next_y = self._next_position(-1)
        if not self._check_collision(next_x, next_y):
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

    def _check_collision(self, x, y):
        return (round(x, 2), round(y, 2)) in self.obstacles
