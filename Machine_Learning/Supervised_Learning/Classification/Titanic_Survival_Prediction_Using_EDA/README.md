# 🚢 Titanic Survival Prediction using EDA

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)

## 📌 Project Overview

The Titanic Survival Prediction project is a complete Machine Learning workflow that predicts whether a passenger survived the Titanic disaster based on demographic and travel-related information.

This project demonstrates the entire machine learning pipeline, including:

- Data Collection
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Feature Engineering
- Data Preprocessing
- Model Training
- Performance Evaluation
- Visualization and Interpretation

The goal is to build an intelligent classification model capable of predicting passenger survival using historical Titanic passenger records.

---

## 🎯 Objectives

- Analyze the Titanic dataset using EDA techniques.
- Handle missing values and inconsistent data.
- Engineer meaningful features to improve model performance.
- Train a machine learning classifier.
- Evaluate the model using multiple metrics.
- Visualize results through confusion matrices and performance charts.
- Understand factors that influenced passenger survival.

---

## 📊 Dataset Information

The dataset contains passenger information collected from the Titanic voyage.

### Features Used

| Feature | Description |
|----------|-------------|
| Pclass | Passenger Class |
| Sex | Gender |
| Age | Passenger Age |
| SibSp | Number of Siblings/Spouses Aboard |
| Parch | Number of Parents/Children Aboard |
| Fare | Ticket Fare |
| Embarked | Port of Embarkation |
| FamilySize | Total Family Members |
| IsAlone | Passenger Traveling Alone |
| Title | Extracted Passenger Title |

### Target Variable

| Value | Meaning |
|---------|---------|
| 0 | Did Not Survive |
| 1 | Survived |

---

# 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Missingno
- Scikit-Learn

---

# 📂 Project Structure

```text
Titanic Survival Prediction using EDA
│
├── eda_.py
├── eda_2.py
├── Model1.py
├── model.pkl
├── README.md
├── requirements.txt
└── titanic.csv
```

---

# 🔍 Exploratory Data Analysis

The project includes extensive EDA to understand passenger behavior and survival trends.

### Analysis Performed

✅ Missing Value Analysis

✅ Survival Distribution

✅ Gender-Based Survival Analysis

✅ Passenger Class Analysis

✅ Age Distribution

✅ Correlation Analysis

✅ Feature Importance Investigation

### Key Insights

- Female passengers had significantly higher survival rates.
- First-class passengers survived more frequently than third-class passengers.
- Younger passengers showed better survival probability.
- Family relationships influenced survival outcomes.
- Fare amount indirectly reflected survival chances.

---

# 🧹 Data Preprocessing

Several preprocessing techniques were applied:

### Missing Value Handling

#### Age

```python
Median Imputation
```

#### Embarked

```python
Mode Imputation
```

#### Cabin

```python
Dropped due to excessive missing values
```

---

# ⚡ Feature Engineering

To improve prediction accuracy, additional features were created.

### Family Size

```python
FamilySize = SibSp + Parch + 1
```

### Is Alone

```python
IsAlone = 1 if FamilySize == 1 else 0
```

### Title Extraction

Titles were extracted from passenger names:

Examples:

- Mr
- Mrs
- Miss
- Master
- Rare Titles

These titles provide important social and demographic information.

---

# 🤖 Machine Learning Model

## Random Forest Classifier

The final model uses a Random Forest algorithm due to its:

- High accuracy
- Robustness
- Low overfitting tendency
- Ability to handle mixed feature types

### Hyperparameters

```python
RandomForestClassifier(
    n_estimators=400,
    max_depth=7,
    min_samples_split=4,
    random_state=42
)
```

---

# 📈 Model Evaluation

The model is evaluated using:

### Accuracy

Measures overall prediction correctness.

### Precision

Measures correctness of positive predictions.

### Recall

Measures ability to identify actual survivors.

### F1 Score

Balances Precision and Recall.

### Confusion Matrix

Provides detailed classification results.

---

# 📊 Sample Performance

| Metric | Score |
|----------|--------|
| Accuracy | 82% – 88% |
| Precision | High |
| Recall | High |
| F1 Score | Balanced |

> Actual results may vary depending on train-test split and random seed.

---

# 📉 Confusion Matrix

The confusion matrix visualizes:

- True Positives
- True Negatives
- False Positives
- False Negatives

This helps understand model strengths and weaknesses beyond simple accuracy.

---

# 🚀 How to Run

## Clone Repository

```bash
git clone https://github.com/santhosh17905
```

## Navigate

```bash
cd Titanic-Survival-Prediction
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run

```bash
python eda_.py
```

When a plot appears, press `s` then Enter to save the current plot screenshot to the `screenshots/` folder.

---

# 📸 Screenshots

This project does not include a dedicated `screenshots/` folder, but you can add visual outputs from the analysis and modeling steps here for documentation purposes.

Suggested screenshot file names:

- `missing_values.png` — missing value heatmap or matrix
- `survival_distribution.png` — survival count plot or bar chart
- `confusion_matrix.png` — model confusion matrix heatmap

> If you create these plots in `eda_.py` or `Model1.py`, save them manually in a local `screenshots/` folder.

---

# 📝 Output

The primary outputs of this project are:

- `model.pkl` — trained machine learning model file
- analysis results printed during execution of `eda_.py` / `eda_2.py`
- plotted figures showing feature distributions, survival trends, and model performance

## Expected runtime behavior

Running the scripts should:

- load `titanic.csv`
- perform exploratory data analysis
- train a classification model
- produce evaluation metrics such as accuracy, precision, recall, and F1 score
- display or save visualizations for missing values, survival distribution, and confusion matrix

---

# 💡 Learning Outcomes

Through this project, the following concepts were learned:

- Exploratory Data Analysis
- Data Cleaning
- Feature Engineering
- Label Encoding
- Classification Algorithms
- Random Forest Modeling
- Performance Evaluation
- Visualization Techniques

---

# 🔮 Future Improvements

- Hyperparameter Optimization
- Cross Validation
- Ensemble Learning
- XGBoost Integration
- Streamlit Deployment
- Flask Deployment
- Model Serialization
- Feature Importance Dashboard

---

# 🎓 Academic Relevance

This project is highly suitable for:

- Machine Learning Mini Projects
- Data Science Portfolios
- College Demonstrations
- Resume Projects
- Interview Discussions
- Kaggle Practice

---

# ⭐ Project Highlights

✔ Complete End-to-End Machine Learning Pipeline

✔ Advanced Feature Engineering

✔ Random Forest Optimization

✔ Comprehensive EDA

✔ Professional Evaluation Metrics

✔ Industry-Oriented Workflow

✔ Portfolio Ready Project

---

# 👨‍💻 Author

**Santhosh S**

Machine Learning Enthusiast | AI Developer | Data Science Learner

---

# 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.

---

## 🌟 If you found this project useful, consider giving it a star on GitHub!