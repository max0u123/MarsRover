# src/models.py

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Orientation:
    NORTH = 'NORTH'
    SOUTH = 'SOUTH'
    EAST = 'EAST'
    WEST = 'WEST'
