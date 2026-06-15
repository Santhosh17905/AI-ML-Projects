# Salary Prediction using POLYNOMIAL REGRESSION

## Project Overview

This project predicts the **salary of an employee** based on their **experience level** using **Polynomial Regression**, a machine learning technique for modeling **non-linear relationships**.  

Unlike Linear Regression, Polynomial Regression can fit **curved trends** in data, making it suitable for real-world scenarios like salary growth which often increases non-linearly with experience.

**Key Features:**
- Data visualization of Linear vs Polynomial Regression
- Smooth curve prediction using Polynomial features
- User input for interactive salary prediction
- Model accuracy evaluation (R² score)
- Compare Linear Regression vs Polynomial Regression performance

---

## Project Folder Structure
Salary_prediction_using_POLYNOMIAL_REGRESSION/
│
├── Salary_prediction_using_POLYNOMIAL_REGRESSION.ipynb
├── salary_prediction_using_polynomial_regression.py
├── README.md
├── requirements.txt
└── .gitignore


---

## Dataset

The dataset contains:

| Level (Experience) | Salary (LPA) |
|-------------------|--------------|
| 1                 | 3            |
| 2                 | 4            |
| 3                 | 5            |
| 4                 | 7            |
| 5                 | 10           |
| 6                 | 15           |
| 7                 | 21           |

- `Level` → Independent variable (X)  
- `Salary` → Dependent variable (Y)

---

## Python Libraries Required

Add the following in **requirements.txt**:

numpy
pandas
matplotlib
scikit-learn


Install all libraries using:

```bash
pip install -r requirements.txt

## **How to Run the Project**

1. Clone the repository:

git clone https://github.com/Santhosh17905/Salary_Prediction_Polynomial_Regression.git

2. Navigate to project folder:
```bash
cd Salary_Prediction_Polynomial_Regression

3.Open the notebook in Google Colab or Jupyter Notebook:
```bash
jupyter notebook Salary_prediction_using_POLYNOMIAL_REGRESSION.ipynb

4. Run all cells.

5. Input Level when prompted to predict salary.

# Key Code Sections

1.Import Libraries

2.Load Dataset

3.Visualize Linear Regression

4.Polynomial Feature Transformation

5.Train Polynomial Regression

6.Smooth Curve Visualization

7.Predict Salary (User Input)

8.Model Accuracy (R² Score)

# Model Accuracy

*Polynomial Regression R² Score: ~0.98

*Linear Regression R² Score: ~0.85

*Polynomial Regression fits non-linear salary trends better than Linear Regression.

# Example output

Enter Level of Employee: 6
Predicted Salary for Level 6 is 15.12 LPA
Polynomial Regression Model Accuracy (R²): 0.980

Author
Santhosh S

GitHub:https://github.com/Santhosh17905