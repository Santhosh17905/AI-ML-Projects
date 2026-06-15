#Salary Estimation | K-NEAREST NEIGHBOUR model

# KNN is a simple, easy-to-implement supervised machine learning algorithm that can be used to solve both classification and regression problems. It is based on the principle of similarity, where the algorithm classifies a new data point based on the majority class of its k nearest neighbors in the feature space. The value of k is a user-defined parameter that determines how many neighbors to consider when making a prediction. KNN is non-parametric, meaning it does not make any assumptions about the underlying data distribution, making it versatile for various types of datasets. However, it can be computationally expensive for large datasets and may struggle with high-dimensional data.
# importing necessary libraries

import pandas as pd #useful for loading the dataset
import numpy as np #to perform array



# loading the dataset

dataset = pd.read_csv('salary.csv')

# checking the shape of dataset and first 5 rows of dataset

print(dataset.shape)
print(dataset.head(5))

# checking for null values in dataset

print(dataset.isnull().sum())

income_set = set(dataset['income'])
dataset['income'] = dataset['income'].map({'<=50K': 0, '>50K': 1}).astype(int)
print(dataset.head)

# separating the features and target variable from dataset

X = dataset.iloc[:, :-1].values

Y = dataset.iloc[:, -1].values

# splitting the dataset into training and testing set, 75% for training and 25% for testing

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

# feature scaling is important for KNN algorithm because it is based on the distance between data points. If the features are on different scales, the distance calculation can be dominated by one feature, leading to biased predictions. By standardizing the features, we ensure that each feature contributes equally to the distance calculation, improving the performance of the KNN algorithm.

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# finding best K value for KNN model using Elbow method

error = []
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Calculating error for K values between 1 and 40

for i in range(1, 40):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train, y_train)
    pred_i = model.predict(X_test)
    error.append(np.mean(pred_i != y_test))

plt.figure(figsize=(12, 6))
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')

# training the KNN model with the best K value (6 in this case)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 6, metric = 'minkowski', p = 2)
model.fit(X_train, y_train)

# knn prediction for new data point with age 4 and mean values of other features (education, capital gain, hours per week)

import matplotlib.pyplot as plt
plt.scatter(X[:, 0], Y, color='blue', label='Data Points')
new_point_age = 4
mean_edu = dataset['education.num'].mean()
mean_cg = dataset['capital.gain'].mean()
mean_wh = dataset['hours.per.week'].mean()

new_sample_unscaled = np.array([[new_point_age, mean_edu, mean_cg, mean_wh]])
new_sample_scaled = sc.transform(new_sample_unscaled)
predicted_salary = model.predict(new_sample_scaled)

# Plot the predicted salary for the new_point_age

plt.scatter(new_point_age, predicted_salary[0], color='red', label='Prediction')

plt.xlabel("Experience (Years)")
plt.ylabel("Salary (LPA)")
plt.title("KNN Salary Prediction")
plt.legend()
plt.show()

#Predicting, wheather new customer with Age & Salary will Buy or Not

age = int(input("Enter New Employee's Age: "))
edu = int(input("Enter New Employee's Education: "))
cg = int(input("Enter New Employee's Captital Gain: "))
wh = int(input("Enter New Employee's Hour's Per week: "))
newEmp = [[age,edu,cg,wh]]
result = model.predict(sc.transform(newEmp))
print(result)

if result == 1:
  print("Employee might got Salary above 50K")
else:
  print("Customer might not got  Salary above 50K")

# Prediction for all Test Data

y_pred = model.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Evaluating Model - CONFUSION MATRIX

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix: ")
print(cm)

print("Accuracy of the Model: {0}%".format(accuracy_score(y_test, y_pred)*100))