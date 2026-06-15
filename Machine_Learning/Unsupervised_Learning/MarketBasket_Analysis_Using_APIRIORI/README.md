# 🛒 Market Basket Analysis Using Apriori

## 📌 Project Overview

This project implements **Market Basket Analysis** using the **Apriori Algorithm** to discover relationships between products frequently purchased together.

It helps businesses understand **customer buying patterns** and enables:

* Product recommendations
* Cross-selling strategies
* Store layout optimization

---

## 🎯 Objective

To identify **frequent itemsets** and generate **association rules** using:

* Apriori Algorithm (basic approach)
* Apriori using MLxtend (industry-level approach)

---

## 📂 Dataset

* Transactional dataset containing items purchased together
* Each row represents a transaction
* Each column represents an item

Example:

| Item1 | Item2 | Item3  |
| ----- | ----- | ------ |
| Milk  | Bread | Butter |

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Apyori
* MLxtend

---

## 🔄 Project Workflow

```
Data Loading
↓
Data Preprocessing
↓
Transaction Creation
↓
Apriori Algorithm (apyori)
↓
Association Rules Generation
↓
Visualization
↓
MLxtend Implementation (One-Hot Encoding)
↓
Final Rules & Recommendations
```

---

## 🧠 Apriori Algorithm Explained

The Apriori algorithm identifies **frequent itemsets** based on:

### 🔹 Support

Frequency of item occurrence

### 🔹 Confidence

Likelihood of buying item B if item A is purchased

### 🔹 Lift

Strength of relationship between items

---

## 📊 Sample Output

```
Input: Milk
Output: Bread, Butter
```

```
(light cream) → (chicken)
Confidence: 0.29
Lift: 4.84
```

---

## 📈 Visualization

A scatter plot is used to show:

* Support vs Confidence

---

## 🧪 How to Run

### Step 1: Clone Repository

```
git clone https://github.com/your-username/MarketBasket_Analysis_Using_APIRIORI.git
cd MarketBasket_Analysis_Using_APIRIORI
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### Step 3: Run Notebook

```
jupyter notebook
```

---

## 🔍 Testing Input & Output

You can test recommendations using:

```python
recommend_products('milk')
```

---

## 🚀 Features

* Apriori implementation from scratch (apyori)
* Industry-level approach using MLxtend
* Dynamic dataset handling
* Strong rule filtering
* Visualization of results
* Product recommendation logic

---

## 📊 Business Use Cases

* 🛒 Supermarket product placement
* 🛍 E-commerce recommendations
* 🍔 Restaurant combo suggestions
* 📦 Inventory optimization

---

## ⚡ Key Insights

* Customers who buy *light cream* also tend to buy *chicken*
* Strong relationships identified using lift metric
* Helps increase revenue via cross-selling

---

## 📁 Project Structure

```
MarketBasket_Analysis_Using_APIRIORI/
│
├── dataset.csv
├── MarketBasket_Analysis_Using_APIRIORI.ipynb
├── marketbasket_analysis_using_apiriori.py
├── README.md
├── requirements.txt
├── .gitignore
```

---

## 👨‍💻 Author

Santhosh S

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
