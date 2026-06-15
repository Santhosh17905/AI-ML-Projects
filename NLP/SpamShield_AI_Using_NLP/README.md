# 🛡️ SpamShield AI
### Enterprise Email & SMS Spam Detection Platform using NLP, Machine Learning, Flask, Analytics & REST API

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange.svg)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

# 📌 Overview

SpamShield AI is a production-style Natural Language Processing (NLP) platform designed to detect spam emails and SMS messages using Machine Learning.

The system combines:

- Advanced NLP preprocessing
- TF-IDF Vectorization
- Calibrated Support Vector Machine (SVM)
- User Authentication
- Analytics Dashboard
- Word Cloud Visualization
- CSV Export
- REST API Integration
- Docker Containerization

The platform allows users to analyze messages in real time, store prediction history, visualize spam trends, and access the prediction engine through APIs.

---

# 🚀 Key Features

### 🔐 Authentication System

- User Registration
- Secure Login
- Password Hashing using BCrypt
- Session Management using Flask-Login
- Logout Functionality

---

### 🤖 AI Spam Detection

- Real-Time Message Analysis
- Email Spam Detection
- SMS Spam Detection
- Confidence Score Generation
- Machine Learning Prediction Engine

---

### 🧠 NLP Pipeline

- Text Cleaning
- Tokenization
- Stopword Removal
- TF-IDF Feature Extraction
- Feature Vector Generation

---

### 📊 Analytics Dashboard

- Total Predictions
- Spam Count
- Ham Count
- Prediction Statistics
- Recent Prediction History

---

### 📈 Data Visualization

- Spam vs Ham Pie Chart
- Spam Word Cloud
- Analytics Dashboard Charts

---

### 📁 Data Export

- Export Prediction Records
- CSV Download Support
- Business Reporting Ready

---

### 🌐 REST API

- JSON Request Support
- JSON Response Support
- External Application Integration
- Mobile App Integration

---

### 🐳 Deployment Ready

- Docker Support
- Production Architecture
- Modular Project Structure

---

# 🏗️ System Architecture

```text
User
 │
 ▼
Flask Web Application
 │
 ├── Authentication Layer
 │
 ├── Dashboard Layer
 │
 ├── Prediction Engine
 │
 ▼
TF-IDF Vectorizer
 │
 ▼
Calibrated SVM Model
 │
 ▼
Prediction Result
 │
 ▼
SQLite Database
 │
 ▼
Analytics Dashboard
 │
 ├── Pie Chart
 ├── Word Cloud
 └── History
```

---

# 🧠 Machine Learning Workflow

### Step 1: Dataset Loading

Dataset contains:

```text
Label | Message
```

Example:

```text
spam | Congratulations! You won ₹5000.
ham  | Let's meet tomorrow.
```

---

### Step 2: Text Processing

Messages are cleaned and transformed into machine-readable format.

```text
Raw Text
    ↓
Cleaning
    ↓
Tokenization
    ↓
TF-IDF Vectorization
```

---

### Step 3: Model Training

Algorithm Used:

```text
Calibrated Linear Support Vector Machine (SVM)
```

Advantages:

- High Accuracy
- Fast Prediction
- Suitable for Text Classification
- Confidence Probability Generation

---

### Step 4: Model Persistence

Saved Files:

```text
spam_model.pkl
vectorizer.pkl
```

These files are loaded by the Flask application during runtime.

---

# 📊 Dashboard Features

The Dashboard provides:

### Statistics

- Total Predictions
- Total Spam Messages
- Total Ham Messages

### Visual Analytics

- Spam/Ham Distribution Chart
- Word Cloud Visualization

### Monitoring

- Recent Prediction History
- Prediction Confidence Scores

---

# 🌐 REST API

## Endpoint

```http
POST /api/predict
```

---

### Request

```json
{
    "message": "Congratulations! You won ₹5000."
}
```

---

### Response

```json
{
    "prediction": "SPAM",
    "confidence": 99.31
}
```

---

# 📂 Project Structure

```text
SpamShield_AI_Using_NLP/
│
├── app.py
├── config.py
├── database_models.py
├── requirements.txt
├── README.md
├── Dockerfile
│
├── database/
│   └── spam.db
│
├── models/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── routes/
│   ├── auth.py
│   ├── prediction.py
│   ├── export.py
│   └── api.py
│
├── services/
│   ├── model_service.py
│   └── analytics.py
│
├── train/
│   ├── train_model.py
│   └── spam.csv
│
├── static/
│   ├── css/
│   ├── charts/
│   └── screenshots/
│
├── templates/
│   ├── index.html
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── predict.html
│   └── history.html
│
└── logs/
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/santhosh17905
cd SpamShield-AI
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🏋️ Train the Model

```bash
python train/train_model.py
```

Generated Files:

```text
models/
├── spam_model.pkl
└── vectorizer.pkl
```

---

# ▶️ Run Application

```bash
python app.py
```

Application:

```text
http://127.0.0.1:5000
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t spamshield-ai .
```

---

## Run Container

```bash
docker run -p 5000:5000 spamshield-ai
```

---

# 📸 Screenshots

## Landing Page

Add:

```text
static/screenshots/landing.png
```

---

## Dashboard

Add:

```text
static/screenshots/dashboard.png
```

---

## Prediction Page

Add:

```text
static/screenshots/predict.png
```

---

## Analytics Dashboard

Add:

```text
static/screenshots/analytics.png
```

---

## Word Cloud

Add:

```text
static/screenshots/wordcloud.png
```

---

# 📈 Performance

| Metric | Score |
|----------|----------|
| Accuracy | 97.40% |
| Precision | High |
| Recall | High |
| F1 Score | High |

---

# 💡 Real-World Applications

- Email Security Platforms
- SMS Filtering Systems
- Customer Support Automation
- Enterprise Communication Security
- Banking Fraud Detection Pipelines
- Messaging Applications

---

# 🛠️ Tech Stack

### Backend

- Flask
- SQLAlchemy
- Flask-Login
- Flask-Bcrypt

### Machine Learning

- Scikit-Learn
- TF-IDF
- SVM

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- WordCloud

### Database

- SQLite

### Deployment

- Docker

---

# 🎯 Learning Outcomes

Through this project, the following concepts were implemented:

- Natural Language Processing
- Text Vectorization
- TF-IDF
- Machine Learning Classification
- Model Persistence
- Flask Development
- Authentication Systems
- Database Integration
- REST API Development
- Data Visualization
- Docker Containerization
- Production Project Architecture

---

# 👨‍💻 Author

**Santhosh S**

AI & Machine Learning Enthusiast

100 Days AI/ML Challenge 🚀

---

# ⭐ Support

If you found this project useful:

⭐ Star the Repository

🍴 Fork the Repository

📢 Share with Others

Happy Coding 🚀