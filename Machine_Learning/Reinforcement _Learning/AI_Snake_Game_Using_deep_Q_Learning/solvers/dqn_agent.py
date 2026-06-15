import torch
import random
import numpy as np
from collections import deque
from models.model import Linear_QNet

class DQNAgent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9
        self.memory = deque(maxlen=100000)

        self.model = Linear_QNet(11, 256, 3)

        try:
            self.model.load()
            print("Loaded trained model")
        except:
            print("Training new model")

        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)
        self.criterion = torch.nn.MSELoss()

    def get_state(self, snake, food, direction):
        head = snake[0]

        point_l = (head[0] - 20, head[1])
        point_r = (head[0] + 20, head[1])
        point_u = (head[0], head[1] - 20)
        point_d = (head[0], head[1] + 20)

        dir_l = direction == (-20, 0)
        dir_r = direction == (20, 0)
        dir_u = direction == (0, -20)
        dir_d = direction == (0, 20)

        state = [
            point_r in snake,
            point_l in snake,
            point_u in snake,
            point_d in snake,
            dir_l, dir_r, dir_u, dir_d,
            food[0] < head[0],
            food[0] > head[0],
            food[1] < head[1],
        ]

        return np.array(state, dtype=int)

    def remember(self, s, a, r, ns, d):
        self.memory.append((s, a, r, ns, d))

    def train_short_memory(self, s, a, r, ns, d):
        self._train(s, a, r, ns, d)

    def train_long_memory(self):
        mini = random.sample(self.memory, min(len(self.memory), 1000))
        for s, a, r, ns, d in mini:
            self._train(s, a, r, ns, d)

    def _train(self, s, a, r, ns, d):
        s = torch.tensor(s, dtype=torch.float)
        ns = torch.tensor(ns, dtype=torch.float)

        pred = self.model(s)
        target = pred.clone()

        Q_new = r
        if not d:
            Q_new = r + self.gamma * torch.max(self.model(ns))

        target[a] = Q_new

        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()
        self.optimizer.step()

    def get_action(self, snake, food, direction):
        self.epsilon = max(0, 80 - self.n_games)
        state = self.get_state(snake, food, direction)

        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2)
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            move = torch.argmax(self.model(state0)).item()

        return move, state