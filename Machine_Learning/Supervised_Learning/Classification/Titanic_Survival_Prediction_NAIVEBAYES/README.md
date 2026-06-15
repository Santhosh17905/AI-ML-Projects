# 🚢 Titanic Survival Prediction using Naive Bayes

## 📌 Project Overview

This project predicts whether a passenger survived the Titanic disaster using the **Naive Bayes Machine Learning algorithm**.

The model is trained on historical passenger data and uses features like passenger class, age, fare, and gender to make predictions.

---

## 🎯 Objective

* Build a classification model using Naive Bayes
* Understand probability-based prediction
* Perform data preprocessing and evaluation

---

## 🧠 Algorithm Used

* Naive Bayes (GaussianNB)

---

## 📂 Project Structure

Titanic_Survival_Prediction_NAIVEBAYES/
│
├── notebooks/
│   └── Titanic_Survival_Prediction_NAIVEBAYES.ipynb
│
├── src/
│   └── titanic_survival_prediction_naivebayes.py
│
├── requirements.txt
├── README.md
└── .gitignore

---

## 📊 Dataset Features

| Feature  | Description              |
| -------- | ------------------------ |
| Pclass   | Passenger class (1,2,3)  |
| Sex      | Gender                   |
| Age      | Age                      |
| SibSp    | Siblings/Spouse          |
| Parch    | Parents/Children         |
| Fare     | Ticket Fare              |
| Embarked | Port                     |
| Survived | Target (0 = No, 1 = Yes) |

---

## ⚙️ Installation

git clone https://github.com/your-Santhosh17905/Titanic_Survival_Prediction_NAIVEBAYES.git

cd Titanic_Survival_Prediction_NAIVEBAYES

pip install -r requirements.txt

---

## ▶️ How to Run

Run Python file:
python src/titanic_survival_prediction_naivebayes.py

OR

Run Notebook:
jupyter notebook

Open:
notebooks/Titanic_Survival_Prediction_NAIVEBAYES.ipynb

---

## 🔍 Workflow

1. Load dataset
2. Handle missing values
3. Feature selection
4. Train-Test split
5. Train model
6. Prediction
7. Accuracy check

---

## 📈 Sample Output

Accuracy: 78%

---

## 💡 Key Learnings

* Naive Bayes concept
* Real dataset handling
* Model evaluation

---

## 🚀 Future Improvements

* Feature engineering
* Try other ML models
* Streamlit deployment

---

## 🛠️ Technologies Used

Python, Pandas, NumPy, Scikit-learn, Jupyter

---

## 📌 Author

Santhosh S

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

========================
📦 requirements.txt
===================

pandas
numpy
scikit-learn
jupyter
matplotlib
seaborn

---

========================
🚫 .gitignore
=============

**pycache**/
*.pyc
*.pyo
*.pyd
.env
venv/
.ipynb_checkpoints/
