# Regression Model Selection for Energy Output Prediction

# This code implements multiple regression algorithms to predict the net hourly electrical energy output of a power plant based on various engine conditions. The dataset includes features such as ambient temperature, exhaust vacuum, ambient pressure, and relative humidity. The code evaluates the performance of each regression model using R-squared and other metrics, and allows for predictions based on new input data.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Uploading the dataset (make sure to upload 'dataset.csv' from your local machine)
# Note: In a local environment, you would typically use pd.read_csv('path_to_your_dataset.csv') instead of the file upload method used in Google Colab.
# If you're running this code in a local environment, you can comment out the file upload section and directly read the dataset from your local path.

# from google.colab import files
# uploaded = files.upload()

# Loading the dataset and separating features and target variable

# AT: Ambient Temperature (in °C)  |  
# V: Exhaust Vacuum (in cm Hg)  |  
# AP: Ambient Pressure (in millibar)  |  
# RH: Relative Humidity (in %)  |  
# PE: Net Hourly Electrical Energy Output (in MW)


dataset = pd.read_csv('dataset.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
ysvm = y.reshape(len(y),1)

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling is necessary for SVR to perform well, but not for other regression models. We will apply feature scaling only to the SVR model.

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

# Feature Scaling for SVR

from sklearn.preprocessing import StandardScaler

modelLR  = LinearRegression()

poly_reg = PolynomialFeatures(degree = 4)
X_poly   = poly_reg.fit_transform(X_train)
modelPLR = LinearRegression()

modelRFR = RandomForestRegressor(n_estimators = 200, random_state = 0)
modelDTR = DecisionTreeRegressor(random_state = 0)

sc_X = StandardScaler()
sc_y = StandardScaler()

X_train_scaled = sc_X.fit_transform(X_train)
X_test_scaled = sc_X.transform(X_test)

y_train_scaled = sc_y.fit_transform(ysvm)

modelSVR = SVR(kernel='rbf')

# Fitting the models to the Training set"

modelLR.fit(X_train, y_train)
modelPLR.fit(X_poly, y_train)
modelRFR.fit(X_train, y_train)
modelDTR.fit(X_train, y_train)

# Recalculate y_train_scaled using y_train to match the sample size of X_train_scaled

y_train_scaled = sc_y.fit_transform(y_train.reshape(-1, 1))
modelSVR.fit(X_train_scaled, y_train_scaled.ravel())

# Predicting the Test set results

modelLRy_pred  = modelLR.predict(X_test)
modelPLRy_pred = modelPLR.predict(poly_reg.transform(X_test))
modelRFRy_pred = modelRFR.predict(X_test)
modelDTRy_pred = modelDTR.predict(X_test)
modelSVRy_pred = modelSVR.predict(X_test)

# Evaluating the models using R-squared and other metrics

from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error, mean_squared_error

print("Linear Regression Accuracy: {}".format(r2_score(y_test, modelLRy_pred)))
print("Polynomial Regression Accuracy: {}".format(r2_score(y_test, modelPLRy_pred)))
print("Random Forest Regression Accuracy: {}".format(r2_score(y_test, modelRFRy_pred)))
print("Decision Treee Regression Accuracy: {}".format(r2_score(y_test, modelDTRy_pred)))
print("Support Vector Regression Accuracy: {}".format(r2_score(y_test, modelSVRy_pred)))

# Additional metrics for Random Forest Regression

print("\nRandom Forest RMSE:", np.sqrt(mean_squared_error(y_test, modelRFRy_pred)))
print("Random Forest MAE:", mean_absolute_error(y_test, modelRFRy_pred))

# Comparing the models and selecting the best one based on R-squared score

scores = {
"Linear Regression": r2_score(y_test, modelLRy_pred),
"Polynomial Regression": r2_score(y_test, modelPLRy_pred),
"Random Forest": r2_score(y_test, modelRFRy_pred),
"Decision Tree": r2_score(y_test, modelDTRy_pred),
"SVR": r2_score(y_test, modelSVRy_pred)
}

best_model = max(scores, key=scores.get)
print("\nBest Model:", best_model)

# Displaying the actual vs predicted values for the test set

results = pd.DataFrame({
    "Actual Value": y_test,
    "LR Prediction": modelLRy_pred,
    "Polynomial Prediction": modelPLRy_pred,
    "RandomForest Prediction": modelRFRy_pred,
    "DecisionTree Prediction": modelDTRy_pred,
    "SVR Prediction": modelSVRy_pred.flatten()
})

print(results.head(10))

# Making predictions based on new input data

print("\nEnter new engine conditions")

AT = float(input("Ambient Temperature: "))
V = float(input("Exhaust Vacuum: "))
AP = float(input("Ambient Pressure: "))
RH = float(input("Relative Humidity: "))

new_data = [[AT, V, AP, RH]]

print("\nPredictions:")

print("Linear Regression:", modelLR.predict(new_data))
print("Polynomial Regression:", modelPLR.predict(poly_reg.transform(new_data)))
print("Random Forest:", modelRFR.predict(new_data))
print("Decision Tree:", modelDTR.predict(new_data))

svr_scaled = sc_X.transform(new_data)
svr_pred = modelSVR.predict(svr_scaled)
print("SVR:", sc_y.inverse_transform(svr_pred.reshape(-1,1)))

# Visualizing the results for Random Forest Regression

plt.scatter(y_test, modelRFRy_pred)
plt.xlabel("Actual Energy Output")
plt.ylabel("Predicted Energy Output")
plt.title("Random Forest Prediction")
plt.show()