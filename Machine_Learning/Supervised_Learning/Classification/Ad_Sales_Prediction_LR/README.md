#  Advertisement Sales Prediction using Logistic Regression

## 📌 Project Overview

This project predicts whether a customer will purchase a product based on their **Age** and **Estimated Salary** using a Machine Learning algorithm called **Logistic Regression**.

It is a **binary classification problem** where the output is:

* `1` → Customer will purchase
* `0` → Customer will not purchase

---

## 🎯 Objective

The main goal of this project is to:

* Understand Logistic Regression from scratch
* Build a prediction model for advertisement sales
* Analyze customer behavior based on input features

---

## 🧠 Algorithm Used

* Logistic Regression (Supervised Learning)
* Sigmoid Function for probability prediction

---

## 📂 Project Structure

DAY_3_Advertisement_Sales_Prediction/
│
├── data/
│   └── Social_Network_Ads.csv
│
├── notebooks/
│   └── ad_sales_prediction.ipynb
│
├── src/
│   └── logistic_model.py
│
├── requirements.txt
└── README.md

---

## 📊 Dataset Information

The dataset contains the following columns:

* **Age** → Age of the customer
* **EstimatedSalary** → Income of the customer
* **Purchased** → Target variable (0 or 1)

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```
git clone https://github.com/your-username/DAY_3_Advertisement_Sales_Prediction.git
cd DAY_3_Advertisement_Sales_Prediction
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

### Run Python Script

```
python src/logistic_model.py
```

---

## 📓 Jupyter Notebook

For detailed explanation, visualization, and step-by-step learning:

```
notebooks/ad_sales_prediction.ipynb
```

---

## 🔍 Example Prediction

Input:
Age = 30
Estimated Salary = 50000

Output:

```
[1]
```

Meaning:
👉 Customer is likely to purchase the product

---

## 📈 Model Workflow

1. Import dataset
2. Data preprocessing
3. Train-test split
4. Train Logistic Regression model
5. Make predictions
6. Evaluate model performance

---

## 💡 Real-World Applications

This model can be used in:

* Advertisement targeting
* Customer purchase prediction
* Marketing strategy optimization
* Product recommendation systems

Companies like Amazon, Google, and Netflix use similar techniques.

---

## 🚀 Future Improvements

* Add data visualization (Matplotlib / Seaborn)
* Implement Confusion Matrix & Accuracy Score
* Convert into a Streamlit Web App
* Deploy using cloud platforms

---

## 🛠️ Requirements

Libraries used in this project:

* pandas
* numpy
* matplotlib
* scikit-learn

---

## 👨‍💻 Author

**Santhosh S**

---

## ⭐ Support

If you like this project:

* ⭐ Star this repository
* 🍴 Fork it
* 📢 Share with others

---
