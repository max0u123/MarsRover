# Class Domain Entité - Objet
class Rover:
    def __init__(self, x, y, orientation, obstacles):
        """
        Initialise un objet Rover avec des coordonnées, une orientation et une liste d'obstacles.

        Args:
            x (float): Coordonnée x initiale du rover.
            y (float): Coordonnée y initiale du rover.
            orientation (str): Orientation initiale du rover ('N', 'S', 'E' ou 'O').
            obstacles (list): Liste des positions des obstacles sur la carte.

        Attributes:
            _x (float): Coordonnée x du rover (attribut privé).
            _y (float): Coordonnée y du rover (attribut privé).
            orientation (str): Orientation actuelle du rover.
            obstacle_encountered (bool): Indique si le rover a rencontré un obstacle.
            obstacles (list): Liste des positions des obstacles sur la carte.
        """
        self._x = x
        self._y = y
        self.orientation = orientation
        self.obstacle_encountered = False
        self.obstacles = obstacles

    @property
    def x(self):
        """
        Renvoie la coordonnée x actuelle du rover.

        Returns:
            float: Coordonnée x du rover.
        """
        return self._x

    @property
    def y(self):
        """
        Renvoie la coordonnée y actuelle du rover.

        Returns:
            float: Coordonnée y du rover.
        """
        return self._y

    def modifier_position(self, new_x, new_y):
        """
        Modifie la position du rover avec de nouvelles coordonnées.

        Args:
            new_x (float): Nouvelle coordonnée x.
            new_y (float): Nouvelle coordonnée y.
        """
        self._x = round(new_x, 2)
        self._y = round(new_y, 2)

    def avancer(self):
        """
        Déplace le rover d'une unité vers l'avant, sauf s'il rencontre un obstacle.
        """
        next_x, next_y = self._next_position(1)
        if not self._check_collision(next_x, next_y):
            self.modifier_position(next_x, next_y)
        else:
            self.rencontrer_obstacle()

    def reculer(self):
        """
        Déplace le rover d'une unité vers l'arrière, sauf s'il rencontre un obstacle.
        """
        next_x, next_y = self._next_position(-1)
        if not self._check_collision(next_x, next_y):
            self.modifier_position(next_x, next_y)
        else:
            self.rencontrer_obstacle()

    def tourner_gauche(self):
        """
        Tourne le rover de 90 degrés vers la gauche, sauf s'il a rencontré un obstacle.
        """
        if not self.obstacle_encountered:
            orientation_map = {'N': 'O', 'O': 'S', 'S': 'E', 'E': 'N'}
            self.orientation = orientation_map[self.orientation]

    def tourner_droite(self):
        """
        Tourne le rover de 90 degrés vers la droite, sauf s'il a rencontré un obstacle.
        """
        if not self.obstacle_encountered:
            orientation_map = {'N': 'E', 'E': 'S', 'S': 'O', 'O': 'N'}
            self.orientation = orientation_map[self.orientation]

    def rencontrer_obstacle(self):
        """
        Indique que le rover a rencontré un obstacle.
        """
        self.obstacle_encountered = True

    def obtenir_etat(self):
        """
        Renvoie un dictionnaire représentant l'état actuel du rover.

        Returns:
            dict: Dictionnaire avec les clés 'x', 'y', 'orientation' et 'obstacle_encountered'.
        """
        return {'x': self.x, 'y': self.y, 'orientation': self.orientation, 'obstacle_encountered': self.obstacle_encountered}

    def reinitialiser_obstacle(self):
        """
        Réinitialise le statut de rencontre d'obstacle à False.
        """
        self.obstacle_encountered = False

    def _next_position(self, step):
        """
        Calcule les nouvelles coordonnées du rover après un déplacement donné.

        Args:
            step (int): Nombre d'unités à déplacer (peut être négatif pour reculer).

        Returns:
            tuple: Nouvelles coordonnées (x, y).
        """
        if self.orientation == 'N':
            return self.x, self.y - step
        elif self.orientation == 'S':
            return self.x, self.y + step
        elif self.orientation == 'E':
            return self.x + step, self.y
        elif self.orientation == 'O':
            return self.x - step, self.y

    def _check_collision(self, x, y):
        """
        Vérifie s'il y a une collision avec un obstacle aux coordonnées spécifiées.

        Args:
            x (float): Coordonnée x à vérifier.
            y (float): Coordonnée y à vérifier.

        Returns:
            bool: True s'il y a collision, False sinon.
        """
        return (round(x, 2), round(y, 2)) in self.obstacles
