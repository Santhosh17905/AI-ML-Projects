# 🧠 Digit Recognition using Random Forest

## 📌 Project Overview

This project focuses on recognizing handwritten digits (0–9) using the **Random Forest Algorithm**.
The model is trained on pixel values of digit images and predicts the correct digit with high accuracy.

---

## 🚀 Algorithm Used

* Random Forest Classifier (Ensemble Learning)

---

## 📂 Dataset

* The dataset contains handwritten digit images.
* Each image is represented as **28 × 28 pixels (784 features)**.
* First column → Digit label (0–9)
* Remaining columns → Pixel values

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## 📁 Project Structure

```
DigitRecognition_RANDOMFOREST/
│
├── digit.csv
├── DigitRecognition_RANDOMFOREST.ipynb
├── digitrecognition_randomforest.py (optional)
├── requirements.txt
└── README.md
```

---

## 🔧 Installation

1. Clone the repository:

```
git clone https://github.com/Santhosh17905/DigitRecognition_RANDOMFOREST.git
```

2. Navigate to the project folder:

```
cd DigitRecognition_RANDOMFOREST
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Option 1: Using Jupyter Notebook / Google Colab

* Open `.ipynb` file
* Run all cells

### Option 2: Using Python Script

```
python digitrecognition_randomforest.py
```

---

## 🧪 Model Workflow

1. Load dataset
2. Split into input (X) and output (Y)
3. Train-test split
4. Train Random Forest model
5. Predict digits
6. Evaluate accuracy
7. Visualize digit image

---

## 📊 Model Performance

* Accuracy: ~95% to 98% (depends on dataset)

---

## 📈 Evaluation Metrics

* Accuracy Score
* Confusion Matrix
* Classification Report

---

## 🖼️ Sample Output

* Model predicts the digit correctly
* Displays the image using matplotlib

---

## 🔍 Key Features

* Image classification using ML
* High accuracy with Random Forest
* Visualization of digits
* Easy to understand pipeline

---

## 💡 Future Improvements

* Add Hyperparameter Tuning
* Deploy using Flask / Streamlit
* Real-time digit drawing input
* Improve UI visualization

---

## 🙌 Author

**Santhosh S**

---

## ⭐ Conclusion

This project demonstrates how machine learning can be used for image classification tasks like handwritten digit recognition using Random Forest.

---

## 📜 License

This project is open-source and free to use.
