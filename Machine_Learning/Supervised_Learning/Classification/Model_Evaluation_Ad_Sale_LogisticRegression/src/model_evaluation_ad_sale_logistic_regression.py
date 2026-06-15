# **Model Evaluation - Ad. Sale Prediction from Existing customer - Logistic Regression**
# In this notebook, we will evaluate the performance of a Logistic Regression model that predicts whether an existing customer will buy a product based on their age and salary. We will use various evaluation metrics such as confusion matrix, accuracy score, classification report, ROC curve, cross-validation score, stratified K-fold cross-validation score, and cumulative accuracy profile (CAP) curve to assess the model's performance.

# Importing necessary libraries

import pandas as pd #useful for loading the dataset
import numpy as np #to perform array

# Load the dataset
# The dataset is expected to be in the same directory as this notebook and named 'DigitalAd_dataset.csv'. It should contain columns for 'Age', 'Salary', and 'Purchased' (the target variable).
# The 'Age' and 'Salary' columns will be used as features (X), while the 'Purchased' column will be used as the target variable (Y).


dataset = pd.read_csv('DigitalAd_dataset.csv')

# Display the shape of the dataset and the first 5 rows to understand its structure and contents.

print(dataset.shape)
print(dataset.head(5))

# Separate the features (X) and the target variable (Y) from the dataset. The features will include all columns except the last one, while the target variable will be the last column.

X = dataset.iloc[:, :-1].values

Y = dataset.iloc[:, -1].values

# Split the dataset into training and testing sets. We will use 75% of the data for training and 25% for testing. The random_state parameter is set to 0 to ensure reproducibility of the results.

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

# Feature Scaling is important for algorithms like Logistic Regression to ensure that all features contribute equally to the result. We will use StandardScaler to standardize the features by removing the mean and scaling to unit variance.
# We will fit the scaler on the training data and then transform both the training and testing data to ensure that the same scaling is applied to both sets.
# This step is crucial to prevent data leakage and to ensure that the model is trained on appropriately scaled data.
# After scaling, the features will have a mean of 0 and a standard deviation of 1, which can improve the performance of the Logistic Regression model.

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# **Model Training - Logistic Regression**

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(random_state = 0)
model.fit(X_train, y_train)

# Predict the target variable for the test set using the trained Logistic Regression model. The predicted values will be stored in the variable 'y_pred'. We will then concatenate the predicted values and the actual values from the test set to compare them side by side.

y_pred = model.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Now we will evaluate the performance of the Logistic Regression model using various metrics.

# **Model Evaluation Metrics**

#Confusion matrix is a table that is used to evaluate the performance of a classification model. It shows the number of true positives, true negatives, false positives, and false negatives. This helps us understand how well the model is performing in terms of correctly classifying the positive and negative classes.

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix: ")
print(cm)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix Visualization")
plt.show()

# Accuracy score is the ratio of correctly predicted observations to the total observations. It gives us an overall idea of how well the model is performing. However, it may not always be the best metric to use, especially in cases of imbalanced datasets.

from sklearn.metrics import accuracy_score
print("Accuracy: {0}%".format(accuracy_score(y_test, y_pred)*100))

from sklearn.metrics import classification_report

print("Classification Report:")
print(classification_report(y_test, y_pred))

# ROC AUC score is a performance measurement for classification problems at various threshold settings. It represents the degree or measure of separability. It tells how much the model is capable of distinguishing between classes. The higher the AUC, the better the model is at predicting 0s as 0s and 1s as 1s. The ROC curve is a graphical representation of the true positive rate against the false positive rate at various threshold settings.

from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

nsProbability = [0 for _ in range(len(y_test))]
lsProbability = model.predict_proba(X_test)
# keep probabilities for the positive outcome only
lsProbability = lsProbability[:, 1]
# calculate scores
nsAUC = roc_auc_score(y_test, nsProbability)
lrAUC = roc_auc_score(y_test, lsProbability)
# summarize scores
print('No Skill: ROC AUC=%.3f' % (nsAUC*100))
print('Logistic Skill: ROC AUC=%.3f' % (lrAUC*100))
# calculate roc curves
nsFP, nsTP, _ = roc_curve(y_test, nsProbability)
lrFP, lrTP, _ = roc_curve(y_test, lsProbability)
# plot the roc curve for the model
plt.plot(nsFP, nsTP, linestyle='--', label='No Skill')
plt.plot(lrFP, lrTP, marker='*', label='Logistic')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
# show the legend
plt.legend()
plt.show()

# cross validation score is a technique used to evaluate the performance of a machine learning model by splitting the dataset into multiple subsets (folds) and training and testing the model on different combinations of these subsets. This helps to ensure that the model's performance is not dependent on a particular train-test split and provides a more robust estimate of the model's generalization ability.

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
kfold = KFold(n_splits=10)
result = cross_val_score(model, X, Y, cv=kfold)
print("CROSS VALIDATION SCORE: %.2f%%" % (result.mean()*100.0))

# Stratified K-fold cross-validation is a variation of K-fold cross-validation that ensures that each fold has a representative distribution of the target variable. This is particularly useful when dealing with imbalanced datasets, as it helps to maintain the proportion of classes in each fold, leading to more reliable evaluation results.

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
skfold = StratifiedKFold(n_splits=3)
model_skfold = LogisticRegression()
results_skfold = cross_val_score(model_skfold, X, Y, cv=skfold)
print("STRATIFIED K-FOLD SCORE: %.2f%%" % (results_skfold.mean()*100.0))

# Cumulative Accuracy Profile (CAP) curve is a graphical representation of the cumulative accuracy of a classification model. It plots the cumulative number of true positives against the cumulative number of observations, allowing us to visualize how well the model is performing in terms of correctly classifying the positive class as we move through the dataset. The CAP curve can help us understand the model's performance and compare it to random and perfect models.

import matplotlib.pyplot as plt
#Calculate Totals and Class Counts
total = len(y_test)
print(total)
class_1_count = np.sum(y_test)
print(class_1_count)
class_0_count = total - class_1_count
##Plot Random Model Line
plt.plot([0, total], [0, class_1_count], c = 'r', linestyle = '--', label = 'Random Model')

##Plot Perfect Model Line
plt.plot([0, class_1_count, total],
         [0, class_1_count, class_1_count],
         c = 'grey',
         linewidth = 2,
         label = 'Perfect Model')
##Compute and Plot the Model's CAP Curve
probs = model.predict_proba(X_test)
probs = probs[:, 1]
model_y = [y for _, y in sorted(zip(probs, y_test), reverse = True)]
y_values = np.append([0], np.cumsum(model_y))
x_values = np.arange(0, total + 1)

plt.plot(x_values,
         y_values,
         c = 'b',
         label = 'LR Classifier',
         linewidth = 4)

index = int((50*total / 100))

## 50% Verticcal line from x-axis
plt.plot([index, index], [0, y_values[index]], c ='g', linestyle = '--')

## Horizontal line to y-axis from prediction model
plt.plot([0, index], [y_values[index], y_values[index]], c = 'g', linestyle = '--')

class_1_observed = y_values[index] * 100 / max(y_values)
plt.xlabel('Total observations')
plt.ylabel('Class 1 observations')
plt.title('Cumulative Accuracy Profile')
plt.legend(loc = 'lower right')

Age = int(input("Enter Age: "))
Salary = int(input("Enter Salary: "))

new_customer = [[Age, Salary]]

new_customer = sc.transform(new_customer)

prediction = model.predict(new_customer)

if prediction == 1:
    print("Customer will BUY the product")
else:
    print("Customer will NOT BUY the product")