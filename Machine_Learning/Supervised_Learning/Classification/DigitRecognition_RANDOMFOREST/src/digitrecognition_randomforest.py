# Digit Recognition using RANDOM FOREST**

# *Importing Basic Library*


import pandas as pd
import numpy as np

# *Importing Dataset*

# The dataset is available in the Kaggle and can be downloaded from the below link:
# https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format?select=digit.csv

dataset = pd.read_csv('digit.csv')

# *Exploring Dataset*

print(dataset.shape)
print(dataset.head(5))

#Segregate Dataset into X(Input/IndependentVariable) & Y(Output/DependentVariable)

X = dataset.iloc[:,1:]
print(X)
print(X.shape)

Y = dataset.iloc[:,0]
print(Y)
print(Y.shape)

#Splitting the dataset into training and testing set with 75% of the data for training and 25% for testing

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

# *Model Building*

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=0
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Accuracy of the Model"""

from sklearn.metrics import accuracy_score
print("Accuracy of the Model: {0}%".format(accuracy_score(y_test, y_pred)*100))

# Classification Report

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


# visualization of the predicted and actual digit

import matplotlib.pyplot as plt
index = 0 # Changed from 2000 to a valid index
print("Actual Digit:", y_test.iloc[index])
print("Predicted Digit:", model.predict(X_test)[index])
plt.axis('off')
plt.imshow(X_test.iloc[index].values.reshape((28,28)),cmap='gray')