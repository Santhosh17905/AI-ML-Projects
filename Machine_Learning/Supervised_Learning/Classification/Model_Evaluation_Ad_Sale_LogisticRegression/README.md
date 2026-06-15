# 📊 Model Evaluation - Ad Sale Prediction using Logistic Regression

👤 **Author:** Santhosh S
🔗 **GitHub:** https://github.com/Santhosh17905

---

## 📌 Project Overview

This project focuses on **evaluating a classification model** built using **Logistic Regression** for predicting whether an existing customer will purchase a product based on their **Age** and **Estimated Salary**.

Unlike basic prediction models, this project emphasizes **model validation and performance evaluation** using multiple industry-standard metrics.

---

## 🎯 Objective

* Predict whether a customer will **buy a product or not**
* Evaluate model performance using advanced **evaluation metrics**
* Understand model reliability and accuracy

---

## 📂 Dataset Information

The dataset contains customer information:

* **Age**
* **Estimated Salary**
* **Purchased (Target Variable)**

  * 0 → Not Purchased
  * 1 → Purchased

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

---

## 🧠 Machine Learning Algorithm

* **Logistic Regression**

Used for binary classification problems where the output is either **0 or 1**.

---

## 🔄 Project Workflow

1. Import Libraries
2. Load Dataset
3. Data Preprocessing
4. Feature Scaling
5. Train-Test Split
6. Model Training (Logistic Regression)
7. Prediction
8. Model Evaluation

---

## 📊 Model Evaluation Techniques

This project uses multiple evaluation methods:

### ✅ Confusion Matrix

* Shows correct and incorrect predictions
* Includes:

  * True Positive (TP)
  * True Negative (TN)
  * False Positive (FP)
  * False Negative (FN)

---

### ✅ Accuracy Score

* Measures overall correctness of the model

---

### ✅ Precision, Recall, F1-Score

* **Precision** → How many predicted positives are correct
* **Recall** → How many actual positives are detected
* **F1 Score** → Balance between Precision & Recall

---

### ✅ ROC Curve & AUC Score

* Evaluates model performance at different thresholds
* AUC closer to **1** indicates a better model

---

### ✅ Cross Validation (K-Fold)

* Validates model stability across multiple splits

---

### ✅ Stratified K-Fold

* Maintains class balance in each split
* Provides more reliable evaluation

---

### ✅ CAP Curve (Cumulative Accuracy Profile)

* Compares model performance with:

  * Random Model
  * Perfect Model
* Helps understand real-world effectiveness

---

## 📈 Output

* Customer purchase prediction (0 or 1)
* Confusion Matrix Visualization
* Accuracy Score
* Precision, Recall, F1 Score
* ROC Curve
* Cross Validation Score
* CAP Curve

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/Santhosh17905/Model_Evaluation_Ad_Sale_Logistic_Regression.git
```

2. Navigate to project folder:

```bash
cd Model_Evaluation_Ad_Sale_Logistic_Regression
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Jupyter Notebook:

```bash
jupyter notebook
```

---

## 📁 Project Structure

```
Model_Evaluation_Ad_Sale_Logistic_Regression/
│
├── Model_Evaluation_Ad_Sale_Logistic_Regression.ipynb
├── model_evaluation_ad_sale_logistic_regression.py
├── DigitalAd_dataset.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📌 Key Highlights

✔ Complete Model Evaluation Pipeline
✔ Real-world classification problem
✔ Multiple evaluation metrics used
✔ Clean and understandable implementation
✔ Suitable for beginners and portfolio

---

## 📚 Future Improvements

* Add Hyperparameter Tuning
* Deploy using Flask / Streamlit
* Add UI for user input
* Improve visualization

---

## ⭐ Conclusion

This project demonstrates how to not only build a machine learning model but also **evaluate its performance effectively using multiple techniques**, making it more reliable for real-world applications.

---

## 🙌 Support

If you like this project, give it a ⭐ on GitHub!

---
