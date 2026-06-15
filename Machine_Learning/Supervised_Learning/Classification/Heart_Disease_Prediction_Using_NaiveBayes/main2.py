# ================================
# HEART DISEASE PREDICTION PROJECT
# Industry Level ML Pipeline
# ================================

# ================================
# 1. Import Libraries
# ================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ================================
# 2. Load Dataset
# ================================

df = pd.read_csv('heart.csv')

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

categorical_columns = ['Sex','ChestPainType','RestingECG','ExerciseAngina','ST_Slope']

for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

# NOW correlation will work
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()


print("\nDataset Shape:", df.shape)

print("\nDataset Info:\n")
print(df.info())

print("\nMissing Values:\n")
print(df.isnull().sum())     #detect missing values


# ================================
# 3. Exploratory Data Analysis (EDA)
# ================================

# Correlation Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# Pie Chart for Heart Disease Distribution
labels = ['Yes','No']
values = df['HeartDisease'].value_counts().values

plt.pie(values, labels=labels, autopct='%1.0f%%')
plt.title('Heart Disease Distribution')
plt.show()

# Chest Pain Type vs Heart Disease
pd.crosstab(df.ChestPainType,df.HeartDisease).plot(kind="bar",figsize=(8,6))
plt.title('Heart Disease Frequency According to Chest Pain Type')
plt.xlabel('Chest Pain Type')
plt.xticks(np.arange(4),('typical angina','atypical angina','non-anginal pain','asymptomatic'),rotation=0)
plt.ylabel('Frequency')
plt.show()

# Age Statistics
print("Min age:",min(df['Age']))
print("Max age:",max(df['Age']))

# Heart Disease vs Gender
pd.crosstab(df.Sex,df.HeartDisease).plot(kind="bar",figsize=(8,6))
plt.title('Heart Disease According to Gender')
plt.xlabel('Male & Female')
plt.xticks(np.arange(2),('Male','Female'),rotation=0)
plt.ylabel('Count')
plt.show()

# Heart Disease vs Resting ECG
pd.crosstab(df.RestingECG,df.HeartDisease).plot(kind="bar",figsize=(8,6))
plt.title('Heart Disease According to RestingECG')
plt.xlabel('RestingECG')
plt.xticks(np.arange(3),('LV Hypertrophy','ST Elevation','Normal'),rotation=0)
plt.ylabel('Count')
plt.show()

# Heart Disease vs Exercise Angina
pd.crosstab(df.ExerciseAngina,df.HeartDisease).plot(kind="bar",figsize=(8,6))
plt.title('Heart Disease According to ExerciseAngina')
plt.xlabel('ExerciseAngina')
plt.xticks(np.arange(2),('No','Yes'),rotation=0)
plt.ylabel('Count')
plt.show()

# Age Distribution
sns.histplot(df[df['HeartDisease']==1]['Age'],color='red',label='Have Heart Disease',kde=True)
sns.histplot(df[df['HeartDisease']==0]['Age'],color='green',label='No Heart Disease',kde=True)

plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution based on Heart Disease')
plt.legend()
plt.show()

print('Min age of people with heart disease: ', min(df[df['HeartDisease'] == 1]['Age']))
print('Max age of people with heart disease: ', max(df[df['HeartDisease'] == 1]['Age']))

print('Min age of people without heart disease: ', min(df[df['HeartDisease'] == 0]['Age']))
print('Max age of people without heart disease: ', max(df[df['HeartDisease'] == 0]['Age']))

# ================================
# 4. Data Preprocessing
# ================================

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

categorical_columns = ['Sex','ChestPainType','RestingECG','ExerciseAngina','ST_Slope']

for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

print("\nEncoded Dataset:\n")
print(df.head())

# ================================
# 5. Feature Selection
# ================================

x = df.drop(columns=['HeartDisease'])
y = df['HeartDisease']

print("\nFeatures:\n",x.head())
print("\nTarget:\n",y.head())

# ================================
# 6. Feature Scaling
# ================================

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x = scaler.fit_transform(x)

# ================================
# 7. Train Test Split
# ================================

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTest Data Sample:\n",x_test[:5])
print("\nTest Labels:\n",y_test[:5])

from sklearn.naive_bayes import GaussianNB
NB = GaussianNB()

from sklearn.model_selection import cross_val_score
scores = cross_val_score(NB, x, y, cv=5)
print("Cross Validation Scores:", scores)
print("Average CV Score:", scores.mean())  # Print Average CV Score

# ================================
# 8. Model Training
# ================================

from sklearn.naive_bayes import GaussianNB

NB = GaussianNB()

NB.fit(x_train,y_train)

# Training Accuracy
from sklearn.metrics import accuracy_score

train_pred = NB.predict(x_train)

print("\nTraining Accuracy:",accuracy_score(y_train,train_pred))

# ================================
# 9. Model Testing
# ================================

y_pred = NB.predict(x_test)

print("\nPredictions:\n",y_pred)
print("\nActual Values:\n",y_test.values)

test_accuracy = accuracy_score(y_test,y_pred)

print("\nTest Accuracy:",test_accuracy)

# ================================
# 10. Model Evaluation
# ================================

from sklearn.metrics import classification_report

print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))

# Confusion Matrix

from sklearn.metrics import precision_score,recall_score,f1_score,confusion_matrix

cm = confusion_matrix(y_test,y_pred)

sns.heatmap(cm,annot=True,fmt='d',cmap='Blues')

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

precision = precision_score(y_test,y_pred)
recall = recall_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred)

print("Precision:",precision)
print("Recall:",recall)
print("F1 Score:",f1)

from sklearn.metrics import roc_curve, roc_auc_score

y_prob = NB.predict_proba(x_test)[:,1]

fpr, tpr, threshold = roc_curve(y_test, y_prob)

plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()

print("ROC AUC Score:", roc_auc_score(y_test, y_prob))   # Print ROC AUC Score

# ================================
# 11. Patient Prediction System
# ================================

age = int(input("Enter Age: "))
sex = int(input("Sex (1=Male,0=Female): "))
cp = int(input("Chest Pain Type (0-3): "))
bp = int(input("Resting BP: "))
chol = int(input("Cholesterol: "))
fast = int(input("FastingBS (0 or 1): "))
ecg = int(input("RestingECG (0-2): "))
hr = int(input("MaxHR: "))
angina = int(input("Exercise Angina (0/1): "))
oldpeak = float(input("Oldpeak: "))
slope = int(input("ST_Slope (0-2): "))

sample = [[age,sex,cp,bp,chol,fast,ecg,hr,angina,oldpeak,slope]]

sample = scaler.transform(sample)

prediction = NB.predict(sample)

if prediction[0]==1:
    print("⚠️ Heart Disease Risk")
else:
    print("✅ Healthy")

sample = scaler.transform(sample)

testPrediction = NB.predict(sample)

if testPrediction[0]==1:
    print("\n⚠️ The Patient Has Heart Disease. Please consult a Doctor")
else:
    print("\n✅ The Patient is Normal")

# ================================
# 12. Save Model (Deployment Ready)
# ================================

# import pickle

# pickle.dump(NB,open("heart_disease_model.pkl","wb"))
# pickle.dump(scaler,open("scaler.pkl","wb"))

# print("\nModel and Scaler Saved Successfully!")