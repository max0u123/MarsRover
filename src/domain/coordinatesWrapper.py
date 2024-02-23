# Fichier domain/coordinatesWrapper.py

class CoordinatesWrapper:
    def __init__(self, map_width, map_height):
        self._map_width = map_width
        self._map_height = map_height

    def wrap_coordinates(self, x, y):
        x = self._wrap_coordinate(x, self._map_width)
        y = self._wrap_coordinate(y, self._map_height)
        return round(x, 2), round(y, 2)

    def _wrap_coordinate(self, coord, limit):
        if coord < 0:
            coord += limit
        if coord >= limit:
            coord -= limit
        return coord
