# 💼 Salary Estimation using K-Nearest Neighbors (KNN)

## 📌 Project Overview

This project predicts the **salary of an employee based on their experience** using the **K-Nearest Neighbors (KNN)** algorithm.

KNN is a simple and powerful **machine learning algorithm** that makes predictions based on the similarity of data points.

---

## 🚀 Features

* Predict salary based on years of experience
* Simple and beginner-friendly implementation
* Uses KNN regression model
* Data visualization using matplotlib
* Easy to modify dataset and K value

---

## 🧠 How It Works

1. The model takes historical data of:

   * Experience (Years)
   * Salary (LPA)

2. When a new input is given:

   * The algorithm finds the **K nearest neighbors**
   * Calculates the **average salary**
   * Returns the predicted value

---

## 📂 Project Structure

```
Salary_Estimation_KNN/
│── SalaryEstimation_KNN.ipynb   # Jupyter Notebook
│── salaryestimation_knn.py      # python source
│── requirements.txt             # Dependencies
│── README.md                    # Project documentation
```

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/Salary_Estimation_KNN.git
cd Salary_Estimation_KNN
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run Jupyter Notebook

```
jupyter notebook
```

### OR run Python file

```
salaryestimation_knn.py
```

---

## 📊 Example

| Experience | Salary |
| ---------- | ------ |
| 1          | 3 LPA  |
| 2          | 4 LPA  |
| 3          | 5 LPA  |
| 5          | 8 LPA  |

👉 Input:

```
Experience = 4
```

👉 Output:

```
Predicted Salary ≈ 6.5 LPA
```

---

## ⚙️ Configuration

You can modify the following:

### 🔹 Change K value

```
model = KNeighborsRegressor(n_neighbors=2)
```

### 🔹 Change dataset

```
data = {
    "Experience": [1,2,3,5],
    "Salary": [3,4,5,8]
}
```

### 🔹 Change input

```
exp = float(input("Enter experience: "))
```

---

## 📈 Visualization

* Blue points → Existing data
* Red point → Predicted salary

---

## 📦 Requirements

* Python 3.x
* NumPy
* Pandas
* Scikit-learn
* Matplotlib

---

## 🎯 Learning Outcomes

* Understand KNN algorithm
* Learn regression using KNN
* Data visualization basics
* Model prediction workflow

---

## 🔥 Future Improvements

* Add Streamlit Web App
* Upload custom dataset
* Hyperparameter tuning
* Add multiple features (skills, age)

---

## 🤝 Contributing

Feel free to fork this repo and improve the project.

---

## 📜 License

This project is open-source and free to use.

---

## 🙌 Acknowledgement

This project is created as part of a **Machine Learning Daily Practice Series**.
