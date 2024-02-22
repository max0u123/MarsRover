import random
#Class Domain Entité
class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def generate_obstacles(self, num_obstacles):
        self.obstacles.clear()
        return {(random.randint(0, self.width - 1), random.randint(0, self.height - 1)) for _ in range(num_obstacles)}

    def check_collision(self, x, y):
        return (x, y) in self.obstacles
