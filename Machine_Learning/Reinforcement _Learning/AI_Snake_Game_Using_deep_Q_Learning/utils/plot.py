import matplotlib.pyplot as plt

scores = []

def plot(score):
    scores.append(score)

    plt.clf()
    plt.title("Training Progress")
    plt.xlabel("Games")
    plt.ylabel("Score")
    plt.plot(scores)
    plt.pause(0.1)