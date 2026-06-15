# Stock_prediction_using_SVM_REGRESSION

## Project Overview
This project predicts **stock prices using Support Vector Regression (SVR)**, a machine learning algorithm from the Support Vector Machine family. The model uses historical stock data, feature engineering, and scaling to accurately predict future stock prices.  

The main goal is to provide a **user-friendly interface** where the user can enter a day index and get the predicted stock price.

---

## Features

- Predict stock prices using **SVR**.
- Uses multiple features for better accuracy:  
  - Day Index  
  - Previous Close Price  
  - 5-day Moving Average  
  - High, Low, Volume  
- Feature scaling for SVR performance.
- Train-Test split for realistic evaluation.
- User input for predicting future stock price.
- Visualization of **actual vs predicted prices**.

---

## Folder Structure

Stock_prediction_using_SVM_REGRESSION/
│
├── data/
│ └── aapl_ticker.csv # Historical stock dataset (Apple)
├──notebook/
  └── Stock_prediction_using_SVM_REGRESSION.ipynb
├── src/
│ └── stock_svr_prediction.py # Main Python code
│
├── README.md
├── requirements.txt
└── .gitignore



---

## Dataset

The project uses Apple stock historical data (AAPL). You can download the dataset here:

**Dataset link:** [AAPL Stock Prices CSV](https://github.com/msabid/stock_data/blob/main/aapl_ticker.csv)  

Place the downloaded CSV in the `data/` folder.

---

## Installation & Requirements

Create a virtual environment (recommended) and install the required packages:

```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# requirements.txt

numpy
pandas
matplotlib
scikit-learn

# Usage

1. Make sure the dataset aapl_ticker.csv is placed in data/ folder.

2. Run the main script:
Usage

Make sure the dataset aapl_ticker.csv is placed in data/ folder.

python src/stock_svr_predictionstock_svr_prediction.py

3. Enter a future day index when prompted. 
Example:
Enter future day index (>= 249): 250
Predicted Stock Price on day 250: $172.56

4. The program will also display a plot showing:

--Red: Actual stock prices
--Blue: SVR predicted trend

Example Output:

  Root Mean Square Error: 3.75
  R2 Score: 0.96
  Enter future day index (>= 249): 250
  Predicted Stock Price on day 250: $172.56

The visualization clearly shows how the predicted trend closely follows the actual stock prices.

# How the Model Works

*Feature Engineering:

     1.Prev_Close: Previous day’s closing price

     2.MA5: 5-day moving average

     3.High, Low, Volume: Additional market features

     4.Day_Index: Sequential day number for trend

*Scaling:

     1.SVR is sensitive to scale. Both input features and output are scaled using StandardScaler.

*SVR Training:

     2.Kernel: RBF

     3.Hyperparameters: C=100, gamma=0.1, epsilon=0.01

     4.Train-test split: 80%-20%

*Prediction:

     1.Model predicts stock price for a given day index using scaled features.

     2.Inverse transforms the output to get actual price.

*Visualization:

     1.Compares predicted trend with actual closing prices.

# Notes

SVR works best for short-term trends rather than long-term predictions.

Accuracy can be improved by adding more features like technical indicators (RSI, MACD, Bollinger Bands).

This project demonstrates the workflow used in real ML stock prediction systems.



Author

Santhosh S.

GitHub:https://github.com/Santhosh17905