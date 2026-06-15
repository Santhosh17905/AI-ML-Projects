# 🌸 Clustering_PlantIris_Using_Principal_Component_Analysis

## 📌 Project Overview

This project demonstrates **Dimensionality Reduction using Principal Component Analysis (PCA)** combined with **K-Means Clustering** on the Iris dataset.

The goal is to:

* Reduce 4D data into 2D using PCA
* Perform clustering using K-Means
* Predict the species of a flower based on user input
* Visualize clusters along with user input in a 2D graph

---

## 🚀 Features

* ✅ Data Standardization using `StandardScaler`
* ✅ Dimensionality Reduction using `PCA`
* ✅ Clustering using `KMeans`
* ✅ Cluster-to-Species Mapping
* ✅ User Input Prediction
* ✅ Data Visualization using `Matplotlib`

---

## 📊 Dataset

The project uses the built-in **Iris dataset** from `sklearn.datasets`.

Features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Target Classes:

* Setosa
* Versicolor
* Virginica

---

## ⚙️ Technologies Used

* Python
* NumPy
* Matplotlib
* Scikit-learn

---

## 🧠 Machine Learning Workflow

1. Load Dataset
2. Standardize Features
3. Apply PCA (reduce dimensions from 4 → 2)
4. Apply K-Means Clustering
5. Map Clusters to Actual Species
6. Take User Input
7. Predict Cluster and Species
8. Visualize Results

---

## 📐 Core Concept

Principal Component Analysis transforms data using:

Z = XW

Where:

* X = Original Data
* W = Principal Components (Eigenvectors)
* Z = Transformed Data

---

## 🖥️ How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/Clustering_PlantIris_Using_Principal_Component_Analysis.git
cd vClustering_PlantIris_Using_Principal_Component_Analysis
```

### Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 3: Run the Script

```bash
python clustering_plantiris_using_principal_component_analysis.py
```

---

## ⌨️ Example Input

```
Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2
```

---

## 📈 Example Output

```
Explained Variance Ratio: [0.72 0.23]
User belongs to Cluster: 0
Predicted Species: setosa
```

---

## 📊 Output Visualization

* 2D PCA Scatter Plot
* Color-coded clusters
* User input plotted as a red "X"

---

## 📁 Project Structure

```
vClustering_PlantIris_Using_Principal_Component_Analysis/
│
├──Clustering_PlantIris_Using_Principal_Component_Analysis.ipynb
├── clustering_plantiris_using_principal_component_analysis.py
├── README.md
├── requirements.txt

```

---

## 🔥 Future Improvements

* Add Streamlit Web App UI
* Add Scree Plot Visualization
* Hyperparameter tuning for K-Means
* Save trained model using Pickle
* Deploy on cloud (Heroku / AWS)

---

## 🎯 Learning Outcomes

* Dimensionality Reduction
* PCA Mathematics (Eigenvalues & Eigenvectors)
* Clustering Concepts
* Data Visualization
* End-to-End ML Workflow

---

## 💼 Resume Description

"Implemented a machine learning pipeline using PCA and K-Means clustering to reduce dimensionality and classify Iris flower species with visualization and user input prediction."

---

## 📜 License

This project is open-source and free to use for learning purposes.

---

## 🙌 Acknowledgements

* Scikit-learn Documentation
* Iris Dataset (UCI Machine Learning Repository)

---
