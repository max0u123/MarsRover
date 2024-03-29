# Class Domain Entité - Objet
class Rover:
    def __init__(self, x, y, orientation, obstacles, map):
        """
        Initialise un objet Rover avec des coordonnées, une orientation et une liste d'obstacles.

        Args:
            x (float): Coordonnée x initiale du rover.
            y (float): Coordonnée y initiale du rover.
            orientation (str): Orientation initiale du rover ('N', 'S', 'E' ou 'O').
            obstacles (list): Liste des positions des obstacles sur la carte.
            map (list): Liste représentant la carte.

        Attributes:
            _x (float): Coordonnée x du rover (attribut privé).
            _y (float): Coordonnée y du rover (attribut privé).
            orientation (str): Orientation actuelle du rover.
            obstacle_encountered (bool): Indique si le rover a rencontré un obstacle.
            obstacles (list): Liste des positions des obstacles sur la carte.
            map (list): Liste représentant la carte.
        """
        self._x = x
        self._y = y
        self.orientation = orientation
        self.obstacle_encountered = False
        self.obstacles = obstacles
        self.map = map

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def wrap_coordinates(self, x, y):
        """
        Vérifie et ajuste les coordonnées pour qu'elles restent dans les limites de la carte.

        Args:
            x (float): Coordonnée x à vérifier.
            y (float): Coordonnée y à vérifier.

        Returns:
            tuple: Nouvelles coordonnées ajustées.
        """
        if x < 0:
            x += len(self.map[0])  # Utilisation de len() pour obtenir la largeur de la carte
        elif x >= len(self.map[0]):
            x -= len(self.map[0])

        if y < 0:
            y += len(self.map)  # Utilisation de len() pour obtenir la hauteur de la carte
        elif y >= len(self.map):
            y -= len(self.map)

        return round(x, 2), round(y, 2)

    def modifier_position(self, new_x, new_y):
        """
        Modifie la position du rover avec de nouvelles coordonnées en prenant en compte les limites de la carte.

        Args:
            new_x (float): Nouvelle coordonnée x.
            new_y (float): Nouvelle coordonnée y.
        """
        new_x, new_y = self.wrap_coordinates(new_x, new_y)
        self._x = new_x
        self._y = new_y

    def avancer(self):
        """
        Déplace le rover d'une unité vers l'avant, en prenant en compte les limites de la carte.
        """
        next_x, next_y = self._next_position(1)
        next_x, next_y = self.wrap_coordinates(next_x, next_y)
        if not self._check_collision(next_x, next_y):
            self.modifier_position(next_x, next_y)
        else:
            self.rencontrer_obstacle()

    def reculer(self):
        """
        Déplace le rover d'une unité vers l'arrière, en prenant en compte les limites de la carte.
        """
        next_x, next_y = self._next_position(-1)
        next_x, next_y = self.wrap_coordinates(next_x, next_y)
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
        Calcule la prochaine position du rover en fonction de l'orientation et du pas.

        Args:
            step (int): Pas de déplacement (+1 pour avancer, -1 pour reculer).

        Returns:
            tuple: Coordonnées de la prochaine position.
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
            x (float): Coordonnée x.
            y (float): Coordonnée y.

        Returns:
            bool: True s'il y a collision, False sinon.
        """
        return (round(x), round(y)) in self.obstacles
