# 📊 Sentimental_Analysis_NLP

A Machine Learning project that performs **Sentiment Analysis using Natural Language Processing (NLP)** to classify text data into **Positive 😊, Negative 😡, or Neutral 😐 sentiments**.

---

## 🚀 Project Overview

This project uses **TF-IDF Vectorization** and **Machine Learning algorithms** to analyze textual data such as reviews, tweets, or comments and predict their sentiment.

---

## 🎯 Features

* Text preprocessing (cleaning, stopword removal)
* TF-IDF feature extraction
* Machine Learning model training
* Sentiment prediction (Positive / Negative / Neutral)
* Emoji-based output 😊😡😐
* Confusion Matrix & Accuracy evaluation

---

## 🧠 Technologies Used

* Python 🐍
* NumPy
* Pandas
* NLTK
* Scikit-learn
* Matplotlib

---

## 📁 Project Structure

```
Sentimental_Analysis_NLP/
│
├── notebook/
│   └── 26_SentimentalAnalysisNLP.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── predict.py
│
├── dataset/
│   └── dataset.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📥 Dataset

* Input dataset should be a `.csv` file
* Must contain:

  * Text column (e.g., `text`)
  * Label column (e.g., `sentiment`)

Example:

| text                  | sentiment |
| --------------------- | --------- |
| I love this product   | 1         |
| Worst experience ever | 0         |

---

## ⚙️ Installation

### Step 1: Clone the Repository

```
git clone https://github.com/santhosh17905
cd Sentimental_Analysis_NLP
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run Notebook

Open:

```
notebook/26_SentimentalAnalysisNLP.ipynb
```

### OR Run Python Script

```
python src/train_model.py
```

---

## 🔄 Workflow

1. Load dataset
2. Clean text (remove special characters, stopwords)
3. Convert text → TF-IDF vectors
4. Split dataset (Train/Test)
5. Train model (Logistic Regression / Random Forest)
6. Evaluate model
7. Predict new input

---

## 🤖 Model Used

* Logistic Regression (Recommended)
* Random Forest Classifier

---

## 📊 Output Example

```
Input: "This airline service is amazing!"
Output: 😊 Positive (Confidence: 91.25%)

Input: "Worst flight ever"
Output: 😡 Negative (Confidence: 88.40%)
```

---

## 🧪 Sample Prediction Code

```python
sample = ["This service is terrible"]
sample_clean = [clean_text(sample[0])]
sample_vec = vectorizer.transform(sample_clean).toarray()

prediction = model.predict(sample_vec)

if prediction == 1:
    print("😊 Positive")
else:
    print("😡 Negative")
```

---

## 📈 Evaluation Metrics

* Accuracy Score
* Confusion Matrix

---

## 📦 requirements.txt

```
numpy
pandas
matplotlib
nltk
scikit-learn
```

---

## 🚫 .gitignore

```
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
*.sqlite3
.env
.venv
env/
venv/
.ipynb_checkpoints/
```

---

## 🌟 Future Improvements

* Deploy using Streamlit 🌐
* Add real-time sentiment detection
* Use Deep Learning (LSTM / BERT)
* Build interactive UI

---

## 👨‍💻 Author

Santhosh S

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
