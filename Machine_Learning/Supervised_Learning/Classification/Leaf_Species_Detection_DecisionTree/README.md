# 🌿 Leaf Species Detection using Decision Tree

## 📌 Project Overview

This project focuses on predicting the species of an Iris flower using Machine Learning. The model is built using the Decision Tree algorithm and trained on the famous Iris dataset.

Based on four input features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

the model predicts the flower species as:

* Setosa
* Versicolor
* Virginica

---

## 🎯 Objective

To build a classification model that can accurately identify Iris flower species based on input measurements.

---

## 📊 Dataset Information

* Dataset: Iris Dataset
* Total Samples: 150
* Features: 4
* Classes: 3

### Features Description:

| Feature      | Description           |
| ------------ | --------------------- |
| Sepal Length | Length of sepal in cm |
| Sepal Width  | Width of sepal in cm  |
| Petal Length | Length of petal in cm |
| Petal Width  | Width of petal in cm  |

---

## ⚙️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Jupyter Notebook / Google Colab

---

## 🚀 Project Workflow

```
Load Dataset
↓
Data Preprocessing
↓
Train-Test Split
↓
Model Training (Decision Tree)
↓
Hyperparameter Tuning (Max Depth)
↓
Prediction
↓
Accuracy Evaluation
↓
Visualization
```

---

## 🧠 Algorithm Used: Decision Tree

Decision Tree is a supervised machine learning algorithm used for classification and regression tasks.

### Key Concepts:

* Root Node: Starting point of the tree
* Decision Node: Condition-based splitting
* Leaf Node: Final output (class label)

The model uses **entropy** to find the best splits based on information gain.

---

## 📈 Model Performance

* Accuracy: ~95% to 100% (depends on split)
* Evaluated using accuracy score

---

## 📉 Visualization

The Decision Tree structure is visualized using `plot_tree()` to understand how the model makes decisions.

---

## 🧪 How to Run the Project

### Step 1: Clone Repository

```
git clone https://github.com/your-Santhosh17905/LeafSpeciesDetection_DECISIONTREE.git
cd LeafSpeciesDetection_DECISIONTREE
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### Step 3: Run Notebook

Open:

```
LeafSpeciesDetection_DECISIONTREE.ipynb
```

in Jupyter Notebook or Google Colab and run all cells.

---

## 💡 Example Prediction

Input:

```
Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2
```

Output:

```
Predicted Species: Setosa
```

---

## 📁 Project Structure

```
LeafSpeciesDetection_DECISIONTREE/
│
├── LeafSpeciesDetection_DECISIONTREE.ipynb
├──leafspeciesdetection_decisiontree.py
├── README.md
└── requirements.txt
```

---

## 📦 requirements.txt

Create a file named `requirements.txt` and add:

```
numpy
pandas
matplotlib
scikit-learn
```

---

## 🔍 Key Learnings

* Understanding Decision Tree algorithm
* Feature selection and dataset handling
* Model evaluation using accuracy
* Visualization of ML models
* Hyperparameter tuning (max_depth)

---

## 🧑‍💻 Author

Santhosh S

---

## ⭐ Future Improvements

* Convert into web app using Streamlit
* Add more datasets
* Use Random Forest for better accuracy
* Deploy model online

---

## 📌 Conclusion

This project demonstrates how a simple Decision Tree model can effectively classify Iris flower species with high accuracy. It is a beginner-friendly yet powerful introduction to machine learning classification.

---
