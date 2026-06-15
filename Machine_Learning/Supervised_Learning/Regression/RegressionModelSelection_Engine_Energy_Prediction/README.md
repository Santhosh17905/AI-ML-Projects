# 🔵 RegressionModelSelection_Engine_Energy_Prediction

## 📌 Project Overview

This project focuses on predicting the **Net Hourly Electrical Energy Output (PE)** of a Combined Cycle Power Plant using multiple regression algorithms.
The goal is to compare different models and identify the best-performing one.

This project demonstrates concepts from **Machine Learning** and **Regression Analysis**.

---

## 🚀 Features

* Multiple regression models implemented:

  * Linear Regression
  * Polynomial Regression
  * Random Forest Regression
  * Decision Tree Regression
  * Support Vector Regression (SVR)
* Model comparison using R² Score
* Feature scaling for SVR
* Visualization of predictions
* Best model selection
* Model deployment using Streamlit web app

---

## 📊 Dataset Information

The dataset contains the following features:

| Feature | Description                              |
| ------- | ---------------------------------------- |
| AT      | Ambient Temperature (°C)                 |
| V       | Exhaust Vacuum (cm Hg)                   |
| AP      | Ambient Pressure (millibar)              |
| RH      | Relative Humidity (%)                    |
| PE      | Net Hourly Electrical Energy Output (MW) |

---

## 🧠 Machine Learning Models Used

* Linear Regression
* Polynomial Regression
* Random Forest Regression
* Decision Tree Regression
* Support Vector Regression (SVR)

---

## ⚙️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Streamlit
* Joblib

---

## 📁 Project Structure

```
RegressionModelSelection_Engine_Energy_Prediction
│
├── dataset.csv
├── RegressionModelSelection_Engine_Energy.ipynb
├── regressionmodelselection_engine_energy.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/RegressionModelSelection_Engine_Energy_Prediction.git
cd RegressionModelSelection_Engine_Energy_Prediction
```

---

### 2️⃣ Install Requirements

```
pip install -r requirements.txt
```

---

### 3️⃣ Run Jupyter Notebook (Model Training)

```
jupyter notebook
```

Open:

```
model_training.ipynb
```

---

### 4️⃣ Run Streamlit App

```
streamlit run app.py
```

---

## 📈 Model Evaluation

The models are evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

## 🏆 Best Model

In most cases, **Random Forest Regression** gives the highest accuracy for this dataset.

---

## 📊 Sample Output

```
Linear Regression Accuracy: 0.92
Polynomial Regression Accuracy: 0.94
Random Forest Accuracy: 0.96
Decision Tree Accuracy: 0.92
SVR Accuracy: 0.95
```

---

## 🌐 Streamlit Web App (optional)

The project includes a web interface where users can input:

* Temperature
* Vacuum
* Pressure
* Humidity

and get real-time energy predictions.

---

## 💡 Future Improvements

* Hyperparameter tuning (GridSearchCV)
* Cross-validation
* Deployment on cloud platforms (AWS / Render / Streamlit Cloud)
* Adding more datasets for better generalization

---

## 👨‍💻 Author

**Santhosh S**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
