# Salary Prediction using Polynomial Regression
#

# *Importing Libraries*

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# *Upload Dataset*
# *Click on Choose Files and select the Position_Salaries.csv file from your local machine to upload it to Colab.*
# *After uploading, the dataset will be available in the Colab environment, and you can proceed with loading and analyzing it.*
# *Note: If you are running this code in a local environment, you can directly read the dataset using pd.read_csv() without uploading it to Colab.*

# from google.colab import files
# uploaded = files.upload()

# *Load Dataset*

dataset = pd.read_csv('Position_Salaries.csv')

# *Exploratory Data Analysis*

print(dataset.shape)
print(dataset.head(5))
print(dataset.info())
print(dataset.describe())

# *Split Dataset into Independent and Dependent Variables*

X = dataset.iloc[:, :-1].values

Y = dataset.iloc[:, -1].values

# *Train Linear Regression Model*

from sklearn.linear_model import LinearRegression
modelLR = LinearRegression()

# Convert the 'Level' column of X to a numeric format suitable for Linear Regression
X = X[:, 1].reshape(-1, 1)
modelLR.fit(X,Y)

# *model accuracy*

print("Linear Regression Model Accuracy (R²):", round(modelLR.score(X,Y),4))

# *Visualizing Linear Regression results*

import matplotlib.pyplot as plt
plt.scatter(X,Y, color="red")
plt.plot(X, modelLR.predict(X))
plt.title("Linear Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()

"""### *fit() - Training Model - Calculating the initial parameters*

### *transform() - After Training we gonna transform Data by using above calculated values*

### *fit_transform() - First fit & Transform*

###*Convert X to Polynomial Format (X^n)*
###*n-degree*
###*n=2 consist x & x^2*
###*n=3 consist x & x^2 & x^3*
"""

from sklearn.preprocessing import PolynomialFeatures
modelPR = PolynomialFeatures(degree = 4)
xPoly = modelPR.fit_transform(X)

# *Train Polynomial Regression Model*

modelPLR = LinearRegression()
modelPLR.fit(xPoly,Y)

# *model accuracy*

print("Polynomial Regression Model Accuracy (R²):", round(modelPLR.score(xPoly,Y),4))

# *Visualizing Polynomial Regression results*

X_grid = np.arange(min(X), max(X), 0.1).reshape(-1,1)

plt.scatter(X,Y, color="red")
plt.plot(X_grid, modelPLR.predict(modelPR.transform(X_grid)), color="blue")
plt.title("Polynomial Regression (Smooth Curve)")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()

# *Predicting Salary for a specific level*

x = float(input("Enter Level of Employee: "))
salaryPred = modelPLR.predict(modelPR.transform([[x]]))
print("Predicted Salary for Level", x, "is", round(salaryPred[0],2))