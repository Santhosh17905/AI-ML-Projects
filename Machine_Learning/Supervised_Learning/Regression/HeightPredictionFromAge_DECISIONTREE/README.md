# 📊 Height Prediction using Decision Tree Regression

## 🚀 Project Overview

This project demonstrates how to build a **Machine Learning Regression model** using the **Decision Tree algorithm** to predict a person's **height** based on input features like **age**.

A Decision Tree model works like a flowchart where data is split into branches based on conditions, making it easy to understand and visualize.

---

## 🧠 Problem Statement

Predict the **height of a person** using:

* Age (Input Feature)

Target:

* Height (Output)

---

## 🛠️ Technologies Used

* Python 🐍
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

---

## 📂 Project Structure

```
Height_Prediction_DecisionTree/
│
├── dataset.csv
├── height_prediction_decision_tree.ipynb 
├── heightpredictionfromage_decisiontree.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The dataset contains:

* Age (Independent Variable)
* Height (Dependent Variable)

Example:

```
Age,Height
10,140
12,150
14,160
16,170
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/Height_Prediction_DecisionTree.git
cd Height_Prediction_DecisionTree
```

2. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Option 1: Google Colab

* Upload the notebook
* Upload dataset.csv when prompted
* Run all cells

### Option 2: Local Machine

```
jupyter notebook
```

Open the notebook and run all cells.

---

## 🔍 Model Used

* Decision Tree Regressor

### Why Decision Tree?

* Easy to understand
* Handles non-linear data
* No need for feature scaling

---

## 📈 Model Evaluation

Metrics used:

* Root Mean Squared Error (RMSE)
* R² Score

---

## 📊 Visualization

* Scatter plot of actual data
* Decision Tree regression curve
* Tree structure visualization

---

## 💡 Features

✅ Simple and beginner-friendly
✅ Visualization of model predictions
✅ User input prediction
✅ Decision Tree structure visualization

---

## 🧪 Example Prediction

```
Enter Age: 15
Predicted Height: 160.5
```

---

## 📌 Future Improvements

* Add more features (Weight, Gender)
* Hyperparameter tuning
* Deploy using Streamlit
* Use larger real-world dataset

---

## 👨‍💻 Author

Santhosh S

GitHub: https://github.com/Santhosh17905

---

## 📜 License

This project is open-source and free to use.

---

# 📦 requirements.txt

```
numpy
pandas
matplotlib
scikit-learn
```

---

# 🚫 .gitignore

```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Jupyter Notebook
.ipynb_checkpoints

# Virtual Environment
venv/
env/

# System Files
.DS_Store
Thumbs.db

# Dataset (optional)
# Uncomment if dataset is large
# *.csv
```
