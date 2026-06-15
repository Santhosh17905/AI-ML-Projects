from game.engine import GameEngine
from solvers.greedy import GreedySolver
from solvers.hamilton import HamiltonSolver
from solvers.dqn_agent import DQNAgent

def main():
    print("🐍 AI Snake Game")

    solver_type = input("Choose Solver (greedy/hamilton/dqn): ").lower()
    mode = input("Mode (train/play): ").lower()

    if solver_type == "greedy":
        solver = GreedySolver()

    elif solver_type == "hamilton":
        solver = HamiltonSolver()

    else:
        solver = DQNAgent()

        if mode == "play":
            solver.epsilon = 0  # no randomness

    game = GameEngine(solver)
    game.run()

if __name__ == "__main__":
    main()