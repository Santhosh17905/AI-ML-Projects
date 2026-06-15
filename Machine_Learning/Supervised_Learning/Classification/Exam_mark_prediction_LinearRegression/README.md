# Exam_mark_prediction_Linear_Regression

## Project Overview
This project predicts **students' exam marks based on study hours** using **Linear Regression**, one of the simplest yet powerful regression algorithms in machine learning.  
It includes data preprocessing, training/testing, evaluation, prediction, and professional-grade visualization.

---

## Problem Statement
Predict the expected exam marks of a student given the number of hours they studied.  

**Example:**
- Input: 6 hours of study  
- Output: Predicted Marks = 70  

This is a **Regression Problem** because the output is a numerical value.

---

## Dataset
The dataset `data.csv` includes the following columns:

| Column Name | Description |
|-------------|-------------|
| hours       | Number of study hours |
| marks       | Exam marks scored by the student |

You can replace `data.csv` with your own dataset following the same structure.

---

## Technologies & Libraries
- **Python 3.x**  
- **Pandas** – Data manipulation  
- **NumPy** – Numerical computation  
- **Scikit-learn** – Machine Learning algorithms  
- **Matplotlib & Seaborn** – Data visualization  

---

## Project Pipeline
1. **Import Libraries** – Load all necessary Python libraries  
2. **Load Dataset** – Read CSV data  
3. **Handle Missing Values** – Fill any NA values in features  
4. **Split Dataset** – Divide into training and test sets  
5. **Train Linear Regression Model** – Fit model to training data  
6. **Predict Marks** – Predict test set and custom input  
7. **Evaluate Model** – Calculate MAE, MSE, RMSE, R²  
8. **Visualize Results** – Scatter plot, regression line, predicted values  

---

## Model Evaluation
The model is evaluated using the following metrics:

| Metric | Description |
|--------|-------------|
| MAE    | Mean Absolute Error |
| MSE    | Mean Squared Error |
| RMSE   | Root Mean Squared Error |
| R²     | Coefficient of Determination |

**Example Output:**

Mean Absolute Error (MAE): 2.00
Mean Squared Error (MSE): 4.00
Root Mean Squared Error (RMSE): 2.00
R² Score: 0.98


---

## Visualization
- **Blue Dots:** Actual dataset marks  
- **Red Line:** Linear Regression line  
- **Green X markers:** Predicted marks for test data  
- **Annotations:** Each predicted value displayed above marker  

**Industry-Level Plot Example:**
![Example Visualization](exam_marks_regression.png)

---

## Usage

1. Clone this repository:
```bash
git clone https://github.com/Santhosh17905/Exam_mark_prediction_Linear_Regression.git

2. Navigate to project folder:
```bash
cd Exam_mark_prediction_Linear_Regression

3. Install required packages:
```bash
pip install -r requirements.txt

4. Run the Python script:
```bash
python exam_mark_prediction.py

5. Enter the study hours when prompted to get predicted marks.

**Future Improvements**

--Deploy as a Streamlit Web App for interactive prediction

--Use a larger real-world dataset with multiple features (sleep hours, practice tests)

--Save model using joblib for later use

--Add interactive visualization with Plotly

--Include cross-validation for robust evaluation


Author

Santhosh S 
GitHub:https://github.com/Santhosh17905