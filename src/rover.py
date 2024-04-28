# src/rover.py

from models import Point

class Rover:
    def __init__(self, position, orientation, planet_size):
        self.position = position  # Utilisation de la classe Point pour initialiser la position
        self.orientation = orientation
        self.planet_size = planet_size

    def avancer(self):
        """
        Move the rover forward based on its current orientation.
        """
        print("Advancing the rover")
        # Update position based on orientation
        if self.orientation == 'NORTH':
            self.position.y = (self.position.y + 1) % self.planet_size[1]
        elif self.orientation == 'SOUTH':
            self.position.y = (self.position.y - 1) % self.planet_size[1]
        elif self.orientation == 'EAST':
            self.position.x = (self.position.x + 1) % self.planet_size[0]
        elif self.orientation == 'WEST':
            self.position.x = (self.position.x - 1) % self.planet_size[0]
    
    def reculer(self):
        """
        Move the rover backward opposite to its current orientation.
        """
        print("Moving the rover backward")
        # Update position based on orientation
        if self.orientation == 'NORTH':
            self.position.y = (self.position.y - 1) % self.planet_size[1]
        elif self.orientation == 'SOUTH':
            self.position.y = (self.position.y + 1) % self.planet_size[1]
        elif self.orientation == 'EAST':
            self.position.x = (self.position.x - 1) % self.planet_size[0]
        elif self.orientation == 'WEST':
            self.position.x = (self.position.x + 1) % self.planet_size[0]


    def tourner_gauche(self):
        """
        Turn the rover left (counter-clockwise).
        """
        print("Turning left")
        # Example turning logic:
        orientations = ['NORTH', 'WEST', 'SOUTH', 'EAST']
        current_index = orientations.index(self.orientation)
        self.orientation = orientations[(current_index + 1) % 4]

    def tourner_droite(self):
        """
        Turn the rover right (clockwise).
        """
        print("Turning right")
        # Example turning logic:
        orientations = ['NORTH', 'EAST', 'SOUTH', 'WEST']
        current_index = orientations.index(self.orientation)
        self.orientation = orientations[(current_index + 1) % 4]
