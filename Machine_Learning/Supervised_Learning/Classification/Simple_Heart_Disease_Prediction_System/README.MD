# ❤️ Heart Disease Prediction System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web_App-green.svg)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Naive_Bayes-orange.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML_Model-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

### AI-Powered Heart Disease Risk Prediction Web Application

Predicts the likelihood of heart disease using Machine Learning and provides instant risk assessment through a modern web interface.

</div>

---

# 📌 Overview

Heart Disease Prediction System is an end-to-end Machine Learning web application that predicts whether a patient is likely to have heart disease based on clinical and physiological parameters.

The system utilizes a trained Machine Learning model and provides real-time predictions through an interactive Flask-based web interface.

This project demonstrates:

- Data Preprocessing
- Feature Engineering
- Machine Learning Classification
- Model Evaluation
- Model Deployment
- Flask Web Development
- Healthcare AI Applications

---

# 🎯 Project Objectives

The primary objective of this project is to assist in early detection of heart disease risks by analyzing patient health parameters and generating instant predictions.

The application aims to:

✔ Reduce manual analysis effort

✔ Assist healthcare professionals

✔ Provide quick risk assessments

✔ Demonstrate practical AI in healthcare

✔ Showcase Machine Learning deployment skills

---

# 🧠 Machine Learning Pipeline

## 1. Data Collection

The system uses a Heart Disease dataset containing medical records and health indicators.

### Features Used

| Feature | Description |
|----------|------------|
| Age | Patient Age |
| Sex | Gender |
| ChestPainType | Type of Chest Pain |
| RestingBP | Resting Blood Pressure |
| Cholesterol | Cholesterol Level |
| FastingBS | Fasting Blood Sugar |
| RestingECG | ECG Results |
| MaxHR | Maximum Heart Rate |
| ExerciseAngina | Exercise-Induced Angina |
| Oldpeak | ST Depression |
| ST_Slope | Slope of Peak Exercise ST Segment |

---

## 2. Data Preprocessing

The following preprocessing techniques were applied:

- Missing Value Handling
- Label Encoding
- Feature Selection
- Dataset Cleaning
- Train-Test Split

---

## 3. Model Training

### Algorithm Used

**Gaussian Naive Bayes**

Naive Bayes is a probabilistic classification algorithm based on Bayes Theorem.

Advantages:

- Fast Training
- Low Computational Cost
- Performs Well on Small Datasets
- Easy Deployment

---

## 4. Model Evaluation

Performance metrics used:

- Accuracy Score
- Precision Score
- Recall Score
- F1 Score
- Confusion Matrix

---

# 🌐 Web Application Features

### Modern Flask Interface

- Professional UI
- Mobile Responsive Design
- Real-Time Prediction
- Error Handling
- Confidence Score Display
- Prediction History Logging
- User-Friendly Forms

### Prediction Output

The system predicts:

### ✅ Low Risk

Patient is unlikely to have heart disease.

### ⚠️ High Risk

Patient may have heart disease and should consult a medical professional.

---

# 🏗️ Project Architecture

```text
User Input
     │
     ▼
Flask Web Interface
     │
     ▼
Data Validation
     │
     ▼
Trained ML Model (.pkl)
     │
     ▼
Prediction Engine
     │
     ▼
Risk Assessment Result
```

---

# 📂 Project Structure

```text
Heart_Disease_Prediction/
│
├── app.py
├── heart_model.pkl
├── hearts.csv
├── prediction_history.csv
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Step 1

Clone Repository

```bash
git clone https://github.com/santhosh17905
```

## Step 2

Navigate to Project Directory

```bash
cd Heart-Disease-Prediction
```

## Step 3

Create Virtual Environment

```bash
python -m venv venv
```

## Step 4

Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Step 5

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# 📊 Sample Prediction

### Input

```text
Age = 39
Sex = 1
ChestPainType = 2
RestingBP = 120
Cholesterol = 339
FastingBS = 0
RestingECG = 1
MaxHR = 170
ExerciseAngina = 0
Oldpeak = 0
ST_Slope = 2
```

### Output

```text
No Heart Disease Detected
Confidence Score: 92%
```

---

# 🔬 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Flask | Web Framework |
| NumPy | Numerical Computing |
| Pandas | Data Processing |
| Scikit-Learn | Machine Learning |
| Joblib | Model Serialization |
| HTML5 | Frontend |
| CSS3 | Styling |
| Bootstrap | Responsive UI |

---

# 📈 Future Enhancements

### Planned Improvements

- Random Forest Model
- XGBoost Model
- Deep Learning Version
- PDF Medical Report Generation
- Patient Database
- User Authentication
- Explainable AI Dashboard
- Doctor Recommendation Module
- Cloud Deployment
- REST API Support

---

# 🩺 Healthcare Disclaimer

This application is intended for educational and research purposes only.

The predictions generated by this system should not be considered a substitute for professional medical diagnosis, treatment, or consultation.

Always consult a qualified healthcare professional for medical advice.

---

# 💼 Resume Highlights

### Key Skills Demonstrated

- Machine Learning
- Healthcare AI
- Flask Development
- Model Deployment
- Data Preprocessing
- Feature Engineering
- Web Application Development
- Scikit-Learn
- Predictive Analytics

---

# 🌟 Project Highlights

✅ End-to-End Machine Learning Project

✅ Real-Time Heart Disease Prediction

✅ Flask Web Deployment

✅ Professional UI Design

✅ Model Serialization with Joblib

✅ Prediction History Tracking

✅ Healthcare AI Application

✅ Portfolio-Ready Project

---

# 👨‍💻 Author

Santhosh S

AI & Machine Learning Developer

Passionate about Machine Learning, Deep Learning, Computer Vision, and Real-World AI Applications.

---

## ⭐ If you found this project useful, consider giving it a star!