# House Price Prediction using Linear Regression
# In this notebook, we will be using Linear Regression to predict house prices based on the area of the land. We will load the dataset, visualize it, and then train a linear regression model to make predictions.*

# Import necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Upload the dataset
# Note: In a local environment, you would typically use pd.read_csv('path_to_file.csv') to load your dataset.
# Since this code is intended to run in Google Colab, we will use the file upload feature to load the dataset.
# If you are running this code in a local environment, you can skip the file upload part and directly load the dataset using pd.read_csv() with the appropriate file path.

from google.colab import files
uploaded = files.upload()

# Load the dataset into a pandas DataFrame

dataset = pd.read_csv('Housing.csv')

# Display the shape and the first few rows of the dataset

print(dataset.shape)
print(dataset.head(5))

# Visualize the relationship between area and price

plt.scatter(dataset.area, dataset.price)
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()

# Prepare the data for modeling
X = dataset[['area']]


# The rest of the original code for categorical variable handling is now unnecessary
# as X will only contain 'area'
# If you intend to use multiple features, please adjust this cell accordingly.

# Identify categorical columns
categorical_cols = X.select_dtypes(include=['object']).columns

# Convert 'yes'/'no' columns to 1/0
for col in ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']:
    if col in categorical_cols:
        X[col] = X[col].apply(lambda x: 1 if x == 'yes' else 0)

# Apply one-hot encoding to 'furnishingstatus'
if 'furnishingstatus' in categorical_cols:
    X = pd.get_dummies(X, columns=['furnishingstatus'], drop_first=True)
    Y = dataset.price

# Split the dataset into training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Train the Linear Regression model

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, Y_train)  # train on train set

# Evaluate the model using R² Score, MAE, MSE, and RMSE

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

# Generate predictions
predictions = model.predict(X_test)

# Evaluate model
r2 = r2_score(Y_test, predictions)
mae = mean_absolute_error(Y_test, predictions)
mse = mean_squared_error(Y_test, predictions)
rmse = np.sqrt(mse)

print("R² Score:", r2)
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

"""### Let's check is our model is Right ?
### Theory Calculation
### Y = m * X + b (m is coefficient and b is intercept)

*Coefficient - m*
"""

m=model.coef_
print(m)

"""*Intercept - b*"""

b=model.intercept_
print(b)

"""### Y=mx+b
*x is Independant variable - Input - area*
"""

# Define the custom area value for prediction
x = 40000
manual_predicted_price = m * x + b
print(f"The Price of {x} Square feet Land (Manual Calculation) is: {manual_predicted_price[0]:,.2f}")
import pandas as pd
area_for_prediction = pd.DataFrame({'area': [x]})
model_predicted_price = model.predict(area_for_prediction)
print(f"The Price of {x} Square feet Land (Model Prediction) is: {model_predicted_price[0]:,.2f}")