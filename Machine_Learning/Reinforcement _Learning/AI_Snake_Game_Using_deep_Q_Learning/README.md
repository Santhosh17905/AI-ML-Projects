# 🐍 AI Snake Game (Reinforcement Learning)

An AI-powered Snake Game built using **Deep Q-Learning (DQN)**, Greedy algorithms, and a modular game architecture.
This project demonstrates how AI agents learn to play a game through experience.

---

## 🚀 Features

* 🤖 Multiple AI Agents:

  * Greedy Solver (rule-based)
  * Hamilton Solver (basic placeholder)
  * Deep Q-Learning (DQN)

* 🧠 Reinforcement Learning (DQN)

* 📈 Training Visualization using Matplotlib

* 🎮 Pygame-based Game UI

* 💾 Model Saving & Loading

* ⚡ Fast Training Mode

* 🏗️ Clean Modular Code Structure

---

## 🧠 Tech Stack

* Python
* PyTorch
* Pygame
* NumPy
* Matplotlib

---

## 📁 Project Structure

snake-ai/
│
├── main.py
├── requirements.txt
├── README.md
│
├── config/
│   └── settings.py
│
├── game/
│   └── engine.py
│
├── solvers/
│   ├── greedy.py
│   ├── hamilton.py
│   └── dqn_agent.py
│
├── models/
│   └── model.py
│
├── utils/
│   └── plot.py

---

## ▶️ How to Run

### 1. Clone Repository

git clone https://github.com/your-username/snake-ai.git
cd snake-ai

---

### 2. Install Dependencies

pip install -r requirements.txt

---

### 3. Run the Game

python main.py

---

## 🎮 Usage

### 🔹 Train AI (Learning Mode)

Choose Solver: dqn
Mode: train

👉 The AI will:

* Start with random moves
* Learn from rewards
* Improve gradually

---

### 🔹 Play with Trained AI

Choose Solver: dqn
Mode: play

👉 The AI will:

* Load trained model
* Play intelligently
* No random moves

---

### 🔹 Greedy Solver

Choose Solver: greedy

👉 Behavior:

* Moves toward food
* Faster but not perfect
* Can get trapped

---

### 🔹 Hamilton Solver

Choose Solver: hamilton

👉 Behavior:

* Basic placeholder
* Safe random movement
* No crash

---

## 📊 Output

* Snake plays automatically
* Score increases over time
* Training graph shows performance improvement
* Model is saved automatically

---

## 🧠 How It Works

### State Representation (11 Features)

* Danger detection (front, left, right)
* Current direction
* Food position relative to snake

---

### Action Space

* 0 → Straight
* 1 → Right turn
* 2 → Left turn

---

### Reward System

| Action       | Reward |
| ------------ | ------ |
| Eat food 🍎  | +10    |
| Collision 💀 | -10    |
| Move         | -0.1   |

👉 This helps the AI learn optimal behavior.

---

## 💾 Model Saving

* Model is automatically saved in:
  models/model.pth

* Loaded automatically in play mode

---

## 📈 Training Behavior

* Initial stage → Random movement
* Mid stage → Learns food direction
* Final stage → Smart survival strategy

---


## 🧪 Future Improvements

* Advanced Hamiltonian Solver (perfect AI)
* Streamlit Web Dashboard
* AI vs AI Battle Mode
* Leaderboard System
* Game Speed Control UI

---

## 💼 Resume Description

Built an AI-powered Snake Game using Deep Reinforcement Learning (DQN) with real-time training, model persistence, and performance visualization using PyTorch and Pygame.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 📬 Contact

Created by: SANTHOSH
GitHub: https://github.com/your-Santhosh17905

---
