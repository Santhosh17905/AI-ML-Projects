# *Exam Marks Prediction using Linear Regression*
## *Predicting Exam Marks based on Study Hours, Age, and Internet Access*

### *Import Libraries*

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# *Upload Dataset*
# Note: In a local environment, you would use pd.read_csv('path_to_your_file.csv') instead of uploading.
# For example: dataset = pd.read_csv('data.csv')
# In Google Colab, you can upload files directly from your local machine.

from google.colab import files
uploaded = files.upload()

# Load the dataset into a DataFrame

dataset = pd.read_csv('data.csv')

# *Explore Dataset*

print("Dataset Shape:", dataset.shape)
print(dataset.head(5))

# *Check for Missing Values*

dataset.columns[dataset.isna().any()]

dataset.hours = dataset.hours.fillna(dataset.hours.mean())

# *Prepare Data for Modeling*

X = dataset.iloc[:, :-1].values
print(X.shape)
Y = dataset.iloc[:, -1].values

# *Split Data into Training and Testing Sets*

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.25, random_state=0
)

# *Train the Linear Regression Model*

model = LinearRegression()
model.fit(X,Y)

# *Make Predictions*

y_pred = model.predict(X_test)

# *Predict for Custom Input*

a=[[9.2,20,0]]
PredictedmodelResult = model.predict(a)
print(PredictedmodelResult)

# *Evaluate Model Performance*

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

# *Predicting Exam Marks for a New Student*

hours_age_internet = np.array([[6, 20, 0]]) # Assuming 6 hours, 20 years old, no internet
predicted_marks = model.predict(hours_age_internet)
print(f"Predicted Exam Marks for 6 hours (age 20, no internet): {predicted_marks[0]:.2f}")

# *Visualize Results*

# 1️⃣ Import Visualization Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style for industry-level look
sns.set_style("whitegrid")
plt.figure(figsize=(10,6))

# 2️⃣ Scatter Plot of Actual Data
plt.scatter(X[:, 0], Y, color='blue', label='Actual Marks', s=100, alpha=0.7)

# 3️⃣ Regression Line
plt.plot(X[:, 0], model.predict(X), color='red', linewidth=3, label='Regression Line')

# 4️⃣ Predicted Points (Optional: Highlight test set predictions)
plt.scatter(X_test[:, 0], y_pred, color='green', label='Predicted Marks (Test Set)', s=100, marker='X')

# 5️⃣ Annotate Predictions (for test set)
for i, j in zip(X_test[:, 0], y_pred):
    plt.text(i, j+1, f"{j:.0f}", fontsize=9, color='green', ha='center')

# 6️⃣ Labels & Title
plt.xlabel("Study Hours", fontsize=14)
plt.ylabel("Exam Marks", fontsize=14)
plt.title("Exam Marks Prediction using Linear Regression", fontsize=16, fontweight='bold')
plt.legend(fontsize=12)
plt.tight_layout()

# 7️⃣ Show Plot
plt.show()