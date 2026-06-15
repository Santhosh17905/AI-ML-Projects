#Leaf Species Detection | DECISION TREE**

### *Import basic Libraries*


from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

# Load the Iris dataset

dataset = load_iris()

# Print the dataset description

print(dataset.data)
print(dataset.target)

print(dataset.data.shape)

#Segregate Dataset into X(Input/IndependentVariable) & Y(Output/DependentVariable)

X = pd.DataFrame(dataset.data, columns=dataset.feature_names)

Y = dataset.target

# Splitting the dataset into training and testing set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)
print(X_train.shape)
print(X_test.shape)

# Finding best Max_Depth for Decision Tree Classifier

accuracy = []
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

for i in range(1, 10):
    model = DecisionTreeClassifier(max_depth = i, random_state = 0)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    score = accuracy_score(y_test, pred)
    accuracy.append(score)

plt.figure(figsize=(12, 6))
plt.plot(range(1, 10), accuracy, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Finding best Max_Depth')
plt.xlabel('pred')
plt.ylabel('score')

# Building the Decision Tree Classifier Model

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion = 'entropy',max_depth = 3, random_state = 0)
model.fit(X_train,y_train)

# User input
sepal_length = float(input("Enter Sepal Length: "))
sepal_width = float(input("Enter Sepal Width: "))
petal_length = float(input("Enter Petal Length: "))
petal_width = float(input("Enter Petal Width: "))

# Convert input into array
user_input = [[sepal_length, sepal_width, petal_length, petal_width]]

# Prediction
prediction = model.predict(user_input)

print("Prediction Value:", prediction[0])

# Convert number to species
if prediction[0] == 0:
    print("Flower Species: Setosa")
elif prediction[0] == 1:
    print("Flower Species: Versicolor")
else:
    print("Flower Species: Virginica")

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))

plot_tree(model,
          feature_names=dataset.feature_names,
          class_names=dataset.target_names,
          filled=True)

plt.show()

# Predicting the Test set results

y_pred = model.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Evaluating the Model Performance

from sklearn.metrics import accuracy_score
print("Accuracy of the Model: {0}%".format(accuracy_score(y_test, y_pred)*100))