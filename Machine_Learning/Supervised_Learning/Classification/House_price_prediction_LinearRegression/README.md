# House_price_prediction_LinearRegression

## Project Overview
This project demonstrates **House Price Prediction using Multiple Linear Regression**. The model predicts house prices based on multiple features such as **area, bedrooms, bathrooms, and age of the property**. This project is designed as an industry-level Machine Learning project, similar to real IT companies.

The goal is to **train a model using historical house data** and predict prices for new properties. This project also evaluates the model using standard regression metrics such as **R² score, MAE, and RMSE**.

---

## Dataset

The dataset should be a CSV file (e.g., `house_price_dataset.csv`) containing the following columns:

| Column      | Description                       |
|------------|-----------------------------------|
| `area`     | House area in square feet          |
| `bedrooms` | Number of bedrooms                 |
| `bathrooms`| Number of bathrooms                |
| `age`      | Age of the house in years          |
| `price`    | Price of the house (target/output) |

**Example:**

| area | bedrooms | bathrooms | age | price     |
|------|----------|-----------|-----|-----------|
| 1200 | 2        | 2         | 10  | 5000000   |
| 1500 | 3        | 2         | 8   | 6500000   |
| 2000 | 3        | 3         | 5   | 9500000   |

---

## Project Structure

```
House_price_prediction_LinearRegression/
│
├── House_price_prediction_LinearRegression.ipynb   # Jupyter Notebook source
├── house_price_model.pkl                             # Saved trained model (optional)
├── requirements.txt                                 # Python dependencies
├── .gitignore                                       # Git ignore file
└── README.md                                        # Project documentation
```

---

## Installation & Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd House_price_prediction_LinearRegression
```

2. Create a virtual environment (optional):

```bash
python -m venv env
source env/bin/activate      # Linux/Mac
env\Scripts\activate         # Windows
```

3. Install required libraries:

```bash
pip install -r requirements.txt
```

---

## Requirements

**requirements.txt**

```
pandas==2.1.1
numpy==1.26.0
scikit-learn==1.3.0
matplotlib==3.8.0
joblib==1.3.2
# Optional for web app
streamlit==1.29.0
```

---

## .gitignore

**.gitignore**

```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
env/
*.sqlite3

# Jupyter Notebook
.ipynb_checkpoints

# VSCode
.vscode/

# Python environment
.env
*.egg-info/

# Model files
*.pkl
```

---

## How to Run the Project

### Using Jupyter Notebook

1. Open the notebook:

```bash
jupyter notebook House_price_prediction_LinearRegression.ipynb
```

2. Upload the dataset when prompted.
3. Run all cells sequentially:
   - Load dataset
   - Explore dataset
   - Train the **Linear Regression model**
   - Evaluate the model (R², MAE, RMSE)
   - Predict house prices using user inputs

### Predicting Custom House Price

```python
area = 2000
bedrooms = 3
bathrooms = 3
age = 5

predicted_price = model.predict([[area, bedrooms, bathrooms, age]])
print("Predicted House Price:", predicted_price[0])
```

---

## Model Evaluation Metrics

- **R² Score** – How well the model fits the data (closer to 1 is better)  
- **Mean Absolute Error (MAE)** – Average absolute difference between predicted and actual values  
- **Root Mean Squared Error (RMSE)** – Square root of MSE; penalizes large errors

Example:

```
R² Score: 0.92
MAE: 250000
RMSE: 353553
```

---

## Saving and Loading the Model

```python
import joblib

# Save the model
joblib.dump(model, "house_price_model.pkl")

# Load the model
model = joblib.load("house_price_model.pkl")
```

---

## Visualizations

- Scatter plot of **Area vs Price**
- Optional: Explore correlation between **features and target**
- Helps visualize **linear relationship** for regression

---

## Future Improvements

1. Include more features like location score, parking, furnishing status  
2. Use Polynomial Regression for non-linear patterns  
3. Use advanced models: Random Forest, XGBoost, Neural Networks  
4. Hyperparameter tuning & cross-validation  
5. Deploy model as a **Web App** using Streamlit/Flask/FastAPI  

---

## References

- [Scikit-learn Linear Regression Documentation](https://scikit-learn.org/stable/modules/linear_model.html#linear-regression)  
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)  
- [Python Pandas Documentation](https://pandas.pydata.org/docs/)