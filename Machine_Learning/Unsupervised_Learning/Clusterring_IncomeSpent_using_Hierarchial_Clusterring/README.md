# 📊 Clusterring_IncomeSpent_using_Hierarchial_Clusterring

## 🚀 Project Overview

This project performs **Customer Segmentation** using **Hierarchical Clustering** based on customer income and spending behavior. The goal is to identify distinct customer groups to help businesses make data-driven marketing decisions.

---

## 🎯 Objective

* Segment customers into groups based on:

  * Annual Income
  * Spending Score
* Use **Hierarchical Clustering (Agglomerative)** to form clusters
* Visualize clusters and analyze customer behavior patterns

---

## 📁 Dataset

The dataset contains customer information such as:

* Customer ID
* Gender
* Age
* Annual Income (k$)
* Spending Score (1–100)

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* SciPy

---

## 📌 Project Workflow

1. **Import Libraries**
2. **Load Dataset**
3. **Exploratory Data Analysis (EDA)**

   * Missing values check
   * Data distribution
   * Correlation heatmap
4. **Data Preprocessing**

   * Label Encoding (Gender)
5. **Feature Selection**

   * Annual Income
   * Spending Score
6. **Feature Scaling**

   * StandardScaler
7. **Dendrogram Visualization**

   * To find optimal number of clusters
8. **Model Training**

   * Agglomerative Hierarchical Clustering
9. **Model Evaluation**

   * Silhouette Score
10. **Visualization**

* Customer segmentation using Seaborn

---

## 📊 Results

The model segments customers into 5 clusters such as:

* High Income – High Spending
* High Income – Low Spending
* Low Income – High Spending
* Low Income – Low Spending
* Medium Income – Medium Spending

---

## 📈 Sample Output

* Dendrogram showing cluster hierarchy
* Scatter plot of customer segments

---

## 🧠 Key Learnings

* Understanding hierarchical clustering
* Importance of feature scaling in distance-based algorithms
* Using dendrograms to determine cluster count
* Evaluating clustering using silhouette score

---

## 📂 Project Structure

```
Clusterring_IncomeSpent_using_Hierarchial_Clusterring/
│
├── dataset.csv
├── hierarchical_clustering.ipynb
├── hierarchical_clustering.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Clusterring_IncomeSpent_using_Hierarchial_Clusterring.git
```

2. Navigate to project folder:

```bash
cd Clusterring_IncomeSpent_using_Hierarchial_Clusterring
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Python script:

```bash
python hierarchical_clustering.py
```

Or open the notebook:

```bash
jupyter notebook hierarchical_clustering.ipynb
```

---

## 📦 Requirements.txt

```
pandas
numpy
matplotlib
seaborn
scikit-learn
scipy
```

---

## 🚫 .gitignore

```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Jupyter Notebook
.ipynb_checkpoints

# Environment
env/
venv/

# OS files
.DS_Store
Thumbs.db

# Logs
*.log
```

---

## 💼 Resume Description

**Customer Segmentation using Hierarchical Clustering**

* Developed a customer segmentation model using Agglomerative Hierarchical Clustering.
* Performed EDA and feature scaling to improve clustering performance.
* Used dendrogram analysis to determine optimal clusters.
* Evaluated model using Silhouette Score and visualized results using Seaborn.

---

## ⭐ Future Improvements

* Compare with K-Means clustering
* Deploy using Streamlit dashboard
* Add real-time customer prediction

---

## 🤝 Contributing

Feel free to fork this repo and improve the project.

---

## 📜 License

This project is open-source and free to use.

---

## 🙌 Acknowledgment

Inspired by real-world customer segmentation use cases in marketing analytics.

---
