# 🧠 Day 11 - Diabetes Prediction Using Deep Neural Networks

## 📌 Project Overview

This project demonstrates the design and implementation of a **Deep Neural Network (DNN)** for predicting diabetes using the famous **Pima Indians Diabetes Dataset**.

The model learns patterns from medical attributes such as glucose level, blood pressure, BMI, insulin level, age, and pregnancies to predict whether a patient is diabetic or non-diabetic.

This project is part of my **30 Days AI & Machine Learning Challenge** and serves as my first end-to-end Neural Network implementation using TensorFlow/Keras.

---

## 🎯 Objectives

* Understand Artificial Neural Networks (ANN)
* Design a Deep Neural Network architecture
* Train a binary classification model
* Evaluate model performance using multiple metrics
* Save and reload trained models
* Perform diabetes risk prediction on new patient data

---

## 🏥 Problem Statement

Diabetes is one of the most common chronic diseases worldwide.

The objective of this project is to predict:

* **0 → Non-Diabetic**
* **1 → Diabetic**

based on patient health measurements.

---

## 📊 Dataset Information

Dataset: Pima Indians Diabetes Dataset

Features:

| Feature                  | Description                  |
| ------------------------ | ---------------------------- |
| Pregnancies              | Number of pregnancies        |
| Glucose                  | Plasma glucose concentration |
| BloodPressure            | Diastolic blood pressure     |
| SkinThickness            | Triceps skin fold thickness  |
| Insulin                  | 2-Hour serum insulin         |
| BMI                      | Body Mass Index              |
| DiabetesPedigreeFunction | Diabetes pedigree score      |
| Age                      | Age in years                 |
| Outcome                  | Target Variable              |

Dataset Size:

* Rows: 768
* Features: 8
* Target Classes: 2

---

## 🧠 Neural Network Architecture

Input Layer (8 Features)

↓

Dense Layer (64 Neurons, ReLU)

↓

Batch Normalization

↓

Dropout (30%)

↓

Dense Layer (32 Neurons, ReLU)

↓

Batch Normalization

↓

Dropout (25%)

↓

Dense Layer (16 Neurons, ReLU)

↓

Output Layer (1 Neuron, Sigmoid)

---

## ⚙️ Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Scikit-Learn
* Pandas

---

## 🚀 Features

### Data Processing

* Dataset loading
* Feature scaling
* Train/Test splitting
* Stratified sampling

### Deep Learning

* Multi-layer Neural Network
* ReLU Activation
* Sigmoid Output Layer
* Binary Classification

### Optimization

* Early Stopping
* Reduce Learning Rate on Plateau
* Model Checkpointing
* Batch Normalization
* Dropout Regularization

### Evaluation

* Accuracy Score
* Confusion Matrix
* Classification Report
* ROC-AUC Score

### Model Persistence

* Save trained model
* Load saved model
* Predict new patient outcomes

---

## 📂 Project Structure

```text
Day_11_Diabetes_Prediction/
│
├── train.py
├── predict.py
├── pima-indians-diabetes.csv
│
├── best_diabetes_model.keras
├── scaler.npy
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔧 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Diabetes-Prediction-DNN.git
```

```bash
cd Diabetes-Prediction-DNN
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Training the Model

```bash
python train.py
```

Training pipeline:

* Load dataset
* Scale features
* Split data
* Train neural network
* Evaluate model
* Save best model

---

## 🔮 Predicting New Patients

```bash
python predict.py
```

Example Output:

```text
Model Loaded Successfully

Diabetes Probability : 0.8245

Prediction : Diabetic
```

---

## 📈 Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC Score
* Confusion Matrix

Typical Performance:

* Accuracy: 78% – 85%
* ROC-AUC: 0.82 – 0.90

---

## 💡 Real-World Applications

* Hospital Decision Support Systems
* Healthcare Analytics
* Disease Risk Assessment
* Medical Screening Tools
* AI-Assisted Healthcare Platforms

---

## 📚 Key Concepts Learned

* Artificial Neural Networks (ANN)
* Deep Learning Fundamentals
* Binary Classification
* Data Preprocessing
* Feature Scaling
* Model Evaluation
* Overfitting Prevention
* Model Persistence

---

## 🎯 Future Improvements

* Hyperparameter Tuning
* Explainable AI (XAI)
* Flask Deployment
* Streamlit Web Application
* Docker Containerization
* Cloud Deployment
* Real-Time API Integration

---

## 👨‍💻 Author

Santhosh S


Focused on building practical Artificial Intelligence, Machine Learning, Deep Learning, and Computer Vision projects.

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share with others

---
