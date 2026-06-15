# Stock Price Prediction using Support Vector Regression (SVR)
# This notebook demonstrates how to use Support Vector Regression (SVR) to predict stock prices based on historical data. We will use the Apple Inc. (AAPL) stock data for this example.


# Import necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset

# Download CSV from: https://github.com/msabid/stock_data/blob/main/aapl_ticker.csv
df = pd.read_csv("aapl_ticker.csv")
print(df.columns)

# Keep recent 250 days
df = df.tail(250).copy()

# Create a day index for the time series
# This will serve as a simple time feature for the model, allowing it to learn trends over time.

df['Day_Index'] = np.arange(len(df))

# Create additional features

df['Prev_Close'] = df['Close'].shift(1)         # Previous day's close
df['MA5'] = df['Close'].rolling(5).mean()      # 5-day moving average
df = df.dropna()

# Display the first few rows to verify the features

# Features: Day index + Prev_Close + MA5 + High + Low + Volume
X = df[['Day_Index', 'Prev_Close', 'MA5', 'High', 'Low', 'Volume']].values
y = df['Close'].values

# Scale features and target variable

sc_X = StandardScaler()
sc_y = StandardScaler()
X_scaled = sc_X.fit_transform(X)
y_scaled = sc_y.fit_transform(y.reshape(-1,1))

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, shuffle=False)

# Train the SVR model

svr_model = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.01)
svr_model.fit(X_train, y_train.ravel())

# Predict on the test set and inverse transform the predictions to get actual price values

y_pred_scaled = svr_model.predict(X_test)
y_pred = sc_y.inverse_transform(y_pred_scaled.reshape(-1,1))
y_test_actual = sc_y.inverse_transform(y_test.reshape(-1,1))

# Evaluate the model using Root Mean Square Error (RMSE) and R2 Score

rmse = np.sqrt(mean_squared_error(y_test_actual, y_pred))
r2 = r2_score(y_test_actual, y_pred)
print(f"Root Mean Square Error: {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")

"""### *Prediction for all test data for validation*
### *SSres is the sum of squares of the residual errors.*
### *SStot is the total sum of the errors.*
# ![image.png](data:image/png;base64,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)

# *user input prediction*
"""

# User input prediction (Step 11)
day_input = int(input(f"Enter future day index (>= {len(df)}): "))
prev_close = df['Close'].iloc[-1]
ma5 = df['Close'].tail(5).mean()
high = df['High'].iloc[-1]    # last high
low = df['Low'].iloc[-1]      # last low
volume = df['Volume'].iloc[-1] # last volume

user_features = np.array([[day_input, prev_close, ma5, high, low, volume]])
user_scaled = sc_X.transform(user_features)
pred_scaled = svr_model.predict(user_scaled)
pred_price = sc_y.inverse_transform(pred_scaled.reshape(-1,1))
print(f"Predicted Stock Price on day {day_input}: ${pred_price[0][0]:.2f}")

# Visualize the actual vs predicted prices for the test set

plt.figure(figsize=(10,6))
plt.plot(df['Day_Index'], df['Close'], color='red', label='Actual Price')
plt.plot(df['Day_Index'].iloc[-len(y_test):], y_pred, color='blue', label='Predicted Trend')
plt.title("Stock Price Prediction using SVR")
plt.xlabel("Day Index")
plt.ylabel("Close Price")
plt.legend()
plt.show()