# 🔷 Customer Spend Analysis using K-Means Clustering

## 📌 Project Overview

This project focuses on **customer segmentation** using the **K-Means Clustering algorithm**. The goal is to group customers based on their **Income** and **Spending behavior**, helping businesses understand different customer types and improve marketing strategies.

---

## 🎯 Objective

* Segment customers into different groups
* Identify high-value customers
* Analyze spending patterns
* Support targeted marketing decisions

---

## 🧠 Algorithm Used

* K-Means Clustering (Unsupervised Machine Learning)

---

## 📂 Dataset

The dataset contains the following features:

* **INCOME** – Customer annual income
* **SPEND** – Customer spending score

---

## ⚙️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

---

## 📁 Project Structure

```
Customer_Spend_Analysis_using_K-Means_Clustering/

│── dataset/
│     └── dataset.csv
│
│── notebook/
│     └── clustering.ipynb
│
│── output/
│     └── clustered_customers.csv
│
│── README.md
│── requirements.txt
│── .gitignore
```

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```
git clone https://github.com/your-username/Customer_Spend_Analysis_using_K-Means_Clustering.git
```

### Step 2: Navigate to Project Folder

```
cd Customer_Spend_Analysis_using_K-Means_Clustering
```

### Step 3: Install Dependencies

```
pip install -r requirements.txt
```

### Step 4: Run the Notebook

Open:

```
notebook/clustering.ipynb
```

---

## 📊 Steps Performed

1. Import Libraries
2. Load Dataset
3. Data Exploration
4. Feature Selection
5. Elbow Method to find optimal K
6. Apply K-Means Clustering
7. Visualize Clusters
8. Predict new customer cluster

---

## 📈 Output

* Customer clusters visualization
* Cluster centroids
* Customer classification based on spending behavior

---

## 🧾 Example Output

```
Enter Customer Income: 60
Enter Customer Spending: 70

Customer belongs to Cluster: 2
Customer Type: High Income - High Spend
```

---

## 💡 Business Insights

* High Income & High Spending → Target customers
* Low Income & Low Spending → Low priority
* Medium segments → Potential growth customers

---

## 🔮 Future Improvements

* Add Streamlit Web App
* Add real-time prediction UI
* Use more features (Age, Gender)
* Try other clustering algorithms

---

## 📌 Applications

* Customer segmentation
* Marketing strategy
* Recommendation systems
* Business analytics

---

## 🙌 Conclusion

This project demonstrates how unsupervised learning can be used to extract meaningful insights from customer data and improve decision-making in businesses.

---


