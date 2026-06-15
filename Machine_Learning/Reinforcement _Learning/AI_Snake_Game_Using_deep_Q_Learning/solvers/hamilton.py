import random

class HamiltonSolver:
    def get_action(self, snake, food, direction):
        return random.choice([0, 1, 2])