# Breast Cancer Detection using Various Machine Learning Algorithms
# This notebook demonstrates the application of various machine learning algorithms to detect breast cancer using a dataset. The dataset contains features extracted from breast mass images, and the goal is to classify the masses as benign or malignant.

# Importing necessary libraries
import pandas as pd #useful for loading the dataset
import numpy as np #to perform array
from matplotlib import pyplot

# Uploading the dataset from local system
# Note: In a local environment, you would typically use pd.read_csv('path_to_your_file.csv') to load the dataset. However, since this code is intended for Google Colab, we will use the file upload feature to load the dataset.
# The dataset should be in CSV format and should contain the necessary features for breast cancer detection. Make sure to upload the correct file when prompted.
# After uploading the file, we can read it into a pandas DataFrame. The file name should match the name of the uploaded file.

dataset = pd.read_csv('data.csv')

#summary of the dataset

print(dataset.shape)
print(dataset.head(5))

#mapping the diagnosis column to binary values (B: Benign = 0, M: Malignant = 1) for easier processing in machine learning algorithms. We also handle any missing values in the diagnosis column and ensure that the data type is integer for modeling purposes.

dataset['diagnosis'] = dataset['diagnosis'].map({'B': 0, 'M': 1})
dataset.dropna(subset=['diagnosis'], inplace=True)
dataset['diagnosis'] = dataset['diagnosis'].astype(int)
print(dataset.head())

#Segregate Dataset into X(Input/IndependentVariable) & Y(Output/DependentVariable)

X = dataset.iloc[:, 2:32].values

Y = dataset.iloc[:,1].values

#Splitting the dataset into training and testing sets to evaluate the performance of our machine learning models. We use a test size of 25% and a random state of 0 for reproducibility. This allows us to train our models on the training set and evaluate their performance on the unseen test set.

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

#Feature Scaling is a crucial step in the preprocessing of data for machine learning algorithms. It ensures that all features contribute equally to the model's performance by standardizing the range of the features. In this code, we use StandardScaler from scikit-learn to scale the features of our training and testing datasets. This helps improve the performance of many machine learning algorithms, especially those that rely on distance calculations, such as Support Vector Machines (SVM) and K-Nearest Neighbors (KNN).
# We fit the scaler on the training data and then transform both the training and testing data to ensure that they are on the same scale. This step is essential for achieving better accuracy and convergence of the models we will be using later in the code.
# Note: It's important to fit the scaler only on the training data to avoid data leakage, which can lead to overly optimistic performance estimates on the test set.
# After scaling, the features will have a mean of 0 and a standard deviation of 1, which can help improve the performance of many machine learning algorithms.

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Now that we have preprocessed our data, we can proceed to train and evaluate various machine learning algorithms to determine which one performs best for breast cancer detection. We will be using the following algorithms:

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

models = []
models.append(('LR', LogisticRegression(solver='liblinear')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

results = []
names = []
res = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=None)
    cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    res.append(cv_results.mean())
    print('%s: %f' % (name, cv_results.mean()))

pyplot.ylim(.900, .999)
pyplot.bar(names, res, color ='maroon', width = 0.6)

pyplot.title('Algorithm Comparison')
pyplot.show()

# training the Support Vector Machine (SVM) model with a radial basis function (RBF) kernel. The SVM algorithm is a powerful classification technique that works well for both linear and non-linear data. By setting the kernel to 'rbf', we allow the model to capture complex relationships between the features in our dataset, which can improve its ability to distinguish between benign and malignant tumors.
# We also set the probability parameter to True, which enables the model to output probability estimates for

from sklearn.svm import SVC

model = SVC(kernel='rbf', probability=True)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# -------- User Input (4 Features) --------

print("Enter Tumor Details")

radius = float(input("Enter Radius Mean: "))
texture = float(input("Enter Texture Mean: "))
perimeter = float(input("Enter Perimeter Mean: "))
area = float(input("Enter Area Mean: "))

# create input array (30 features required)
sample = np.zeros((1,30))

sample[0][0] = radius
sample[0][1] = texture
sample[0][2] = perimeter
sample[0][3] = area

# scale input
sample = sc.transform(sample)

# prediction
prediction = model.predict(sample)

# result
if prediction[0] == 1:
    print("🔴 Malignant (Cancer Detected)")
else:
    print("🟢 Benign (No Cancer)")

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(cm, annot=True, fmt='d')

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))