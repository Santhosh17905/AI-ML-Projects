import pygame
import random
from config.settings import Settings
from utils.plot import plot

class GameEngine:
    def __init__(self, solver):
        pygame.init()

        self.display = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        pygame.display.set_caption("AI Snake Game 🐍")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20)

        self.solver = solver
        self.reset()

    def reset(self):
        self.snake = [(100, 100)]
        self.direction = (20, 0)
        self.food = self._place_food()
        self.score = 0
        self.frame_iteration = 0

    def _place_food(self):
        while True:
            x = random.randint(0, (Settings.WIDTH - 20)//20) * 20
            y = random.randint(0, (Settings.HEIGHT - 20)//20) * 20
            if (x, y) not in self.snake:
                return (x, y)

    def run(self):
        running = True
        agent_mode = hasattr(self.solver, "remember")

        while running:
            self.clock.tick(60 if agent_mode else Settings.FPS)
            self.frame_iteration += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if agent_mode:
                old_state = self.solver.get_state(self.snake, self.food, self.direction)

            action = self.solver.get_action(self.snake, self.food, self.direction)

            if agent_mode:
                action, _ = action

            self._move(action)
            self.snake.insert(0, self.head)

            reward = 0
            done = False

            if self._is_collision() or self.frame_iteration > 100 * len(self.snake):
                reward = -10
                done = True
                self._handle_game_over(agent_mode)
                continue

            if self.head == self.food:
                self.score += 1
                reward = 10
                self.food = self._place_food()
            else:
                self.snake.pop()
                reward = -0.1

            if agent_mode:
                new_state = self.solver.get_state(self.snake, self.food, self.direction)

                self.solver.train_short_memory(old_state, action, reward, new_state, done)
                self.solver.remember(old_state, action, reward, new_state, done)

            self._update_ui()

        pygame.quit()

    def _handle_game_over(self, agent_mode):
        if agent_mode:
            self.solver.n_games += 1
            self.solver.train_long_memory()
            self.solver.model.save()

            print(f"Game: {self.solver.n_games}, Score: {self.score}")
            plot(self.score)

        self.reset()

    def _move(self, action):
        x, y = self.direction

        if action == 1:
            x, y = y, -x
        elif action == 2:
            x, y = -y, x

        self.direction = (x, y)
        self.head = (self.snake[0][0] + x, self.snake[0][1] + y)

    def _is_collision(self):
        x, y = self.head

        if x < 0 or x >= Settings.WIDTH or y < 0 or y >= Settings.HEIGHT:
            return True

        if self.head in self.snake[1:]:
            return True

        return False

    def _update_ui(self):
        self.display.fill((0, 0, 0))

        for block in self.snake:
            pygame.draw.rect(self.display, (0, 255, 0), (*block, 20, 20))

        pygame.draw.rect(self.display, (255, 0, 0), (*self.food, 20, 20))

        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.display.blit(text, (10, 10))

        pygame.display.flip()