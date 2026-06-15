# 🧠  Character Recognition using Support Vector Machine (SVM)

## 📌 Project Overview

This project demonstrates **Character Recognition** using the **Support Vector Machine (SVM)** algorithm. The model is trained to recognize handwritten digits from image data and predict the correct character.

Character Recognition is widely used in:

* 🏦 Banking (Cheque Processing)
* 📮 Postal Code Recognition
* 🚗 License Plate Detection
* 📱 OCR Applications

---

## 🎯 Objective

To build a Machine Learning model that can:

* Read image data (digits/characters)
* Convert images into numerical features
* Train using SVM
* Predict the correct character from unseen images

---

## 🧠 Algorithm Used

* Support Vector Machine (SVM)

---

## 📂 Dataset

We use the built-in **Digits Dataset** from `sklearn`.

* Total Samples: 1797
* Image Size: 8x8 pixels
* Classes: 0–9 digits

---

## 🛠️ Technologies Used

* Python 🐍
* Scikit-learn
* NumPy
* Matplotlib (optional for visualization)

---

## 📁 Project Structure

```
Handwritten_DigitRecognition_SVM/
│
├── dataset/
│   └── (optional custom dataset)
│
├── notebook/
│   └── Handwritten_DigitRecognition_SVM.ipynb
│
├── src/
│   └── handwrittendigitrecognition_svm.py
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```
git clone https://github.com/your-username/Handwritten_DigitRecognition_SVM.git
cd Handwritten_DigitRecognition_SVM
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run Python Script

```
python src/handwrittendigitrecognition_svm.py
```

### OR Run Jupyter Notebook

```
jupyter notebook
```

Open:

```
notebook/Handwritten_DigitRecognition_SVM.ipynb
```

---

## 🧪 Sample Code

```python
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
digits = datasets.load_digits()

X = digits.data
y = digits.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = svm.SVC()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, predictions))
```

---

## 📊 Output

```
Accuracy: ~97%
```

---

## 📸 Visualization (Optional)

You can visualize digit predictions using matplotlib.

---

## 🚀 Features

* High accuracy digit recognition
* Simple and efficient implementation
* Beginner-friendly project
* Can be extended to full OCR systems

---

## 🔮 Future Improvements

* Add GUI using Streamlit
* Use custom handwritten dataset
* Improve accuracy with hyperparameter tuning
* Extend to alphabet recognition (A-Z)

---

## 📦 requirements.txt

```
numpy
scikit-learn
matplotlib
jupyter
```

---

## 🙌 Acknowledgements

* Scikit-learn for dataset and tools
* Open-source community

---

## 📌 Author

**Santhosh S**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
