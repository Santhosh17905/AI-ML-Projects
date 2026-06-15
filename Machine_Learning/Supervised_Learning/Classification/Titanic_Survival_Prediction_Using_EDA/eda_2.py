import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

# ---------------------------
# 1️⃣ Data Cleaning
# ---------------------------

# Fill Embarked
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])



# Fill Age
df['Age'] = df['Age'].fillna(df['Age'].median())


# Drop Cabin (too many missing)
df.drop("Cabin", axis=1, inplace=True)

# ---------------------------
# 2️⃣ Feature Engineering 🔥
# ---------------------------

# Create Family Size
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Create IsAlone feature
df["IsAlone"] = 0
df.loc[df["FamilySize"] == 1, "IsAlone"] = 1

# Extract Title from Name
df["Title"] = df["Name"].str.extract(r" ([A-Za-z]+)\.", expand=False)


# Replace rare titles
df["Title"] = df["Title"].replace(
    ['Lady','Countess','Capt','Col','Don','Dr',
     'Major','Rev','Sir','Jonkheer','Dona'], 'Rare'
)

df["Title"] = df["Title"].replace(['Mlle','Ms'], 'Miss')
df["Title"] = df["Title"].replace('Mme', 'Mrs')

# ---------------------------
# 3️⃣ Drop Unnecessary Columns
# ---------------------------

df.drop(["PassengerId","Name","Ticket"], axis=1, inplace=True)

# ---------------------------
# 4️⃣ Encoding
# ---------------------------

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df["Sex"] = le.fit_transform(df["Sex"])
df["Embarked"] = le.fit_transform(df["Embarked"])
df["Title"] = le.fit_transform(df["Title"])

# ---------------------------
# 5️⃣ Define X and y
# ---------------------------

X = df.drop("Survived", axis=1)
y = df["Survived"]

# ---------------------------
# 6️⃣ Train Test Split
# ---------------------------

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------
# 7️⃣ Model - Random Forest 🔥
# ---------------------------

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=400,
    max_depth=7,
    min_samples_split=4,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------------------
# 8️⃣ Prediction
# ---------------------------

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Plot
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Reds",
            xticklabels=["Died", "Survived"],
            yticklabels=["Died", "Survived"])

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix\n\n"
          f"Accuracy = {acc:.2f}\n"
          f"Precision = {prec:.2f}   Recall = {rec:.2f}   F1-Score = {f1:.2f}")

plt.show()

