import math

WIDTH = 600
HEIGHT = 600

class GreedySolver:
    def get_action(self, snake, food, direction):
        head_x, head_y = snake[0]
        food_x, food_y = food

        directions = [
            direction,
            (direction[1], -direction[0]),
            (-direction[1], direction[0])
        ]

        best_move = 0
        best_score = float('-inf')

        for i, move in enumerate(directions):
            new_x = head_x + move[0]
            new_y = head_y + move[1]

            if (new_x, new_y) in snake:
                continue

            if new_x < 0 or new_x >= WIDTH or new_y < 0 or new_y >= HEIGHT:
                continue

            dist = math.sqrt((food_x - new_x)**2 + (food_y - new_y)**2)
            score = -dist

            if score > best_score:
                best_score = score
                best_move = i

        return best_move