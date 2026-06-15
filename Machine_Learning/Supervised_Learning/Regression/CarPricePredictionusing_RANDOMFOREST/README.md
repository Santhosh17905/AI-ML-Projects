# 🚗 Car Price Prediction using Random Forest Regression

## 📌 Project Overview

This project predicts the **price of a car** using Machine Learning.
It uses the **Random Forest Regression algorithm** to estimate car prices based on various features such as engine size, horsepower, mileage, etc.

---

## 🎯 Objective

* Build a machine learning model to predict car prices
* Understand feature importance
* Learn real-world ML workflow
* Prepare a project for GitHub portfolio

---

## 🧠 Algorithm Used

* Random Forest Regressor

---

## 📂 Dataset

The dataset contains multiple features related to cars:

* symboling
* wheelbase
* carlength
* carwidth
* carheight
* curbweight
* enginesize
* boreratio
* stroke
* compressionratio
* horsepower
* peakrpm
* citympg
* highwaympg
* price (Target Variable)

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## 📁 Project Structure

```
Car_Price_Prediction_RandomForest/
│
├── dataset.csv
├── CarPricePredictionusing_RANDOMFOREST.ipynb
├── carpricepredictionusing_randomforest.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 Workflow

```
Data Collection
      ↓
Data Cleaning
      ↓
Feature Selection
      ↓
Encoding (if needed)
      ↓
Train-Test Split
      ↓
Model Training (Random Forest)
      ↓
Hyperparameter Tuning
      ↓
Model Evaluation (R2 Score)
      ↓
Feature Importance
      ↓
Model Saving (.pkl)
      ↓
Prediction
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Car_Price_Prediction_RandomForest.git
cd Car_Price_Prediction_RandomForest
```

### 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```
car_price_prediction.ipynb
```

---

## 📊 Model Training

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=0)
model.fit(x_train, y_train)
```

---

## 📈 Model Evaluation

```python
from sklearn.metrics import r2_score

ypred = model.predict(x_test)
print("Accuracy:", r2_score(y_test, ypred))
```

---

## 💾 Model Saving

```python
import pickle

with open("car_price_model.pkl", "wb") as f:
    pickle.dump(model, f)
```

---

## 🔮 Prediction Example

```python
sample = X_test.iloc[0].values.reshape(1,-1)
prediction = model.predict(sample)

print("Predicted Price:", prediction[0])
```

---

## 📌 Results

* Achieved high accuracy using Random Forest
* Model successfully predicts car prices
* Feature importance helps understand key factors affecting price

---

## 📊 Feature Importance

* Engine Size
* Horsepower
* Curb Weight
* Mileage

---

## 🔥 Future Improvements

* Deploy using Flask / Streamlit
* Add UI for user input
* Use advanced models like Gradient Boosting
* Hyperparameter tuning using GridSearchCV

---

## 🤝 Contributing

Feel free to fork this repository and improve the project.

---

## 📜 License

This project is open-source and free to use.

---

## 👨‍💻 Author

Santhosh S

---
