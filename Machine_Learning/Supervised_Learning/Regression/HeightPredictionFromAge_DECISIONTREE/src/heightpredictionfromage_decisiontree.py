# Height Prediction from Age using Decision Tree Regressor
# This code implements a Decision Tree Regressor to predict height based on age. The dataset is loaded from a local directory, and the model is trained and evaluated using standard metrics.
# The code also includes visualization of the decision tree and the predicted values against the actual values.

# Importing necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Uploading the dataset from local directory
# The dataset should be in CSV format and named 'dataset.csv'. It should contain two columns: 'Age' and 'Height'.
# The 'Age' column will be used as the input feature (X) and the 'Height' column will be used as the target variable (Y).

     #from google.colab import files
     #uploaded = files.upload()

# Loading the dataset into a pandas DataFrame

dataset = pd.read_csv('dataset.csv')

# Displaying the shape of the dataset and the first 5 rows to understand the structure of the data

print(dataset.shape)
print(dataset.head(5))

# Separating the dataset into input features (X) and target variable (Y). The input features are all columns except the last one, and the target variable is the last column.

X = dataset.iloc[:, :-1].values

Y = dataset.iloc[:, -1].values

# Splitting the dataset into training and testing sets. 


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.20,random_state=0)

# Training the Decision Tree Regressor model on the training data

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(
    max_depth=5,
    random_state=0
)

model.fit(x_train, y_train)

from sklearn.tree import plot_tree

plt.figure(figsize=(10,6))
plot_tree(model, filled=True)
plt.show()

age = int(input("Enter Age: "))

predicted_height = model.predict([[age]])

print("Predicted Height:", predicted_height[0])

# Visualizing the training data and the predicted values from the model. 


X_val = np.arange(min(x_train), max(x_train), 0.1)
X_val = X_val.reshape((len(X_val), 1))

plt.scatter(x_train, y_train)
plt.plot(X_val, model.predict(X_val))

plt.title('Height Prediction using Decision Tree')
plt.xlabel('Age')
plt.ylabel('Height')

plt.show()

# Predicting the target variable for the test set and evaluating the model's performance using Mean Squared Error (MSE), R2 Score, and Root Mean Square Error (RMSE).

ypred = model.predict(x_test)

from sklearn.metrics import r2_score,mean_squared_error
mse = mean_squared_error(y_test,ypred)
r2score = r2_score(y_test, ypred)
rmse=np.sqrt(mse)
print("Root Mean Square Error:", rmse)
print("R2 Score:", r2score)
print("Model Accuracy:", r2score*100, "%")