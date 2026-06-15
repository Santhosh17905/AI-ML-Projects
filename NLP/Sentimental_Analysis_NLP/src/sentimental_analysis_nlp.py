# Sentimental Analysis using NLP
# This code performs sentimental analysis on a dataset of airline reviews. It preprocesses the text data, extracts features using TF-IDF vectorization, and trains a Logistic Regression model to classify the sentiments as positive, negative, or neutral. Finally, it evaluates the model's performance and makes predictions on new input data.
# Note: Make sure to have the dataset.csv file in your local directory before running this code. The dataset should contain the reviews and their corresponding sentiments.

#!pip install nltk

"""### Importing Libraries"""

import numpy as np
import pandas as pd
import re #Regular expressions
import nltk
import matplotlib.pyplot as plt

from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split

# Uploading the dataset from local directory
# Note: Make sure to have the dataset.csv file in your local directory before running this code. The dataset should contain the reviews and their corresponding sentiments.
# If you are using Google Colab, you can upload the dataset using the following code:

# from google.colab import files
# uploaded = files.upload()

"""### Importing Dataset"""

dataset = pd.read_csv('dataset.csv')
print(dataset.shape)
print(dataset.head(5))

"""###Segregating Dataset into Input & Output"""

features = dataset.iloc[:, 10].values
labels = dataset.iloc[:, 1].values
print(labels)

"""###Removing the Special Character"""

processed_features = []

for sentence in range(0, len(features)):
    # Remove all the special characters
    processed_feature = re.sub(r'\W', ' ', str(features[sentence]))

    # remove all single characters
    processed_feature= re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_feature)

    # Remove single characters from the start
    processed_feature = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_feature)

    # Substituting multiple spaces with single space
    processed_feature = re.sub(r'\s+', ' ', processed_feature, flags=re.I)

    # Removing prefixed 'b'
    processed_feature = re.sub(r'^b\s+', '', processed_feature)

    # Converting to Lowercase
    processed_feature = processed_feature.lower()

    processed_features.append(processed_feature)

"""###Feature Extraction from text

"""

nltk.download('stopwords')
vectorizer = TfidfVectorizer (max_features=2500, min_df=7, max_df=0.8, stop_words=stopwords.words('english'))
processed_features = vectorizer.fit_transform(processed_features).toarray()
print(processed_features)

"""###Splitting Dataset into Train & Test"""

X_train, X_test, y_train, y_test = train_test_split(processed_features, labels, test_size=0.2, random_state=0)

"""# *Any algorithm*"""

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
model.fit(X_train, y_train)

"""###Predicting the Test data with Trained Model"""

predictions = model.predict(X_test)

"""###Score of the Model"""

print(accuracy_score(y_test, predictions))

"""###Confusion Matrix"""

from sklearn import metrics
cm = metrics.confusion_matrix(y_test, predictions)
print(cm)

"""##Prediction"""

new_input = ["the airline is amazing"]
new_input_vectorized = vectorizer.transform(new_input).toarray()

new_prediction = model.predict(new_input_vectorized)

proba = model.predict_proba(new_input_vectorized)

confidence = max(proba[0]) * 100
prediction = new_prediction[0]

if prediction == 'positive':
    result = f"😊 Positive ({confidence:.2f}%)"
elif prediction == 'negative':
    result = f"😡 Negative ({confidence:.2f}%)"
else:
    result = f"😐 Neutral ({confidence:.2f}%)"

print(result)
print("Prediction:", result)