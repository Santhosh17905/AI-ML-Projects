# 🧠 Breast Cancer Detection using Various Machine Learning Algorithms

## 📌 Project Overview

This project focuses on detecting whether a tumor is **Malignant (Cancerous)** or **Benign (Non-Cancerous)** using multiple Machine Learning algorithms.

The goal is to compare different models and select the best-performing one for accurate prediction.

---

## 🎯 Objectives

* Perform data preprocessing and feature scaling
* Train multiple ML algorithms
* Compare model performance
* Build an interactive prediction system
* Deploy the model as a web application

---

## 📂 Dataset

* Dataset used: **Breast Cancer Wisconsin Dataset**
* Features: 30 numerical features describing tumor characteristics
* Target Variable:

  * `0` → Benign (No Cancer)
  * `1` → Malignant (Cancer)

---

## ⚙️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit (for deployment)

---

## 🤖 Machine Learning Algorithms Used

* Logistic Regression
* Linear Discriminant Analysis (LDA)
* K-Nearest Neighbors (KNN)
* Decision Tree
* Naive Bayes
* Support Vector Machine (SVM)
* Random Forest

---

## 🔄 Project Workflow

1. Import Libraries
2. Load Dataset
3. Data Preprocessing
4. Feature Scaling
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Algorithm Comparison
9. Best Model Selection
10. Prediction System
11. Model Saving
12. Deployment

---

## 📊 Model Evaluation Metrics

* Accuracy Score
* Confusion Matrix
* Classification Report
* ROC Curve

---

## 📈 Results

* Compared multiple ML algorithms
* Selected best-performing model (SVM / Random Forest)
* Achieved high accuracy (~95% - 98%)

---

## 🖥️ How to Run the Project

### ▶️ Step 1: Clone Repository

```bash
git clone https://github.com/your-username/BreastCancerDetection_VariousMLAlgorithm.git
cd BreastCancerDetection_VariousMLAlgorithm
```

### ▶️ Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Step 3: Run Jupyter Notebook

```bash
jupyter notebook
```

### ▶️ Step 4: Run Streamlit App (Optional)

```bash
streamlit run app.py
```

---

## 🧪 Sample Input (User Prediction)

Example:

* Radius Mean: 17.99
* Texture Mean: 10.38
* Perimeter Mean: 122
* Area Mean: 1001

### Output:

* 🔴 Malignant (Cancer Detected)
  or
* 🟢 Benign (No Cancer)

---

## 💾 Model Saving

The trained model is saved using:

```python
joblib.dump(model, "breast_cancer_model.pkl")
```

---

## 📁 Project Structure

```
BreastCancerDetection_VariousMLAlgorithm/
│
├── BreastCancerDetection_VariousMLAlgorithm.ipynb
├── app.py
├── breast_cancer_model.pkl
├── requirements.txt
├── README.md
└── dataset/
    └── data.csv
```

---

## 🚀 Future Improvements

* Add more feature selection techniques
* Improve model accuracy using hyperparameter tuning
* Deploy using FastAPI + Docker
* Integrate with real-time medical systems

---

## 👨‍💻 Author

**Santhosh S**

GitHub: https://github.com/Santhosh17905

---

## ⭐ Acknowledgements

* Scikit-learn documentation
* Open datasets for machine learning
* Community tutorials and resources

---

## 📌 Conclusion

This project demonstrates how Machine Learning can assist in **early detection of breast cancer**, helping in faster diagnosis and better medical decisions.

---
