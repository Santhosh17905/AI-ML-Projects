# Market Basket Analysis using Apriori Algorithm
# Market Basket Analysis is a technique used in data mining to discover associations between items in large datasets. The Apriori algorithm is a popular method for finding frequent itemsets and generating association rules. In this code, we will perform Market Basket Analysis using the Apriori algorithm on a dataset of transactions.

#Importing necessary libraries
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Uploading the dataset
# The dataset should be in CSV format and contain transactions with items. Each row represents a transaction, and each column represents an item. The values in the dataset should indicate whether an item was purchased in a transaction (e.g., 1 for purchased, 0 for not purchased).
# You can upload your dataset using the file upload feature in Google Colab. Make sure to name your dataset 'dataset.csv' or adjust the code accordingly to match the name of your uploaded file.

# from google.colab import files
# uploaded = files.upload()

"""### Importing the dataset"""

dataset = pd.read_csv('dataset.csv')

print("Shape:", dataset.shape)
print(dataset.head())

"""## *Dynamic Transaction Creation*
# *Data Pre-Processing*
"""

transactions = dataset.apply(lambda row: row.dropna().tolist(), axis=1).tolist()

"""### Training APRIORI"""

# pip install apyori

from apyori import apriori

rules = apriori(
    transactions=transactions,
    min_support=0.003,
    min_confidence=0.2,
    min_lift=3,
    min_length=2,
    max_length=2
)

"""# *Convert Results to Clean DataFrame*"""

results = list(rules)

clean_results = []

for result in results:
    for relation in result.ordered_statistics:
        clean_results.append([
            tuple(relation.items_base),
            tuple(relation.items_add),
            result.support,
            relation.confidence,
            relation.lift
        ])

df_results = pd.DataFrame(clean_results, columns=[
    'LHS', 'RHS', 'Support', 'Confidence', 'Lift'
])

print(df_results.head())

"""### Results in Dataframe"""

lhs         = [tuple(result[2][0][0])[0] for result in results]
rhs         = [tuple(result[2][0][1])[0] for result in results]
supports    = [result[1] for result in results]
confidences = [result[2][0][2] for result in results]
lifts       = [result[2][0][3] for result in results]
resultsinDataFrame = pd.DataFrame(zip(lhs, rhs, supports, confidences, lifts), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])
resultsinDataFrame

"""# *Sort Best Rules*"""

df_results = df_results.sort_values(by='Lift', ascending=False)
print(df_results.head(10))

"""# *Filter Strong Rules*"""

strong_rules = df_results[
    (df_results['Confidence'] > 0.5) &
    (df_results['Lift'] > 3)
]

print(strong_rules)

"""# *Visualization*"""

import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt

plt.scatter(df_results['Support'], df_results['Confidence'])
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.title('Market Basket Analysis')
plt.show()

"""# Applying Apriori using MLXTEND (Industry Approach)

# *Convert to One-Hot Encoding*
"""

from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)

df = pd.DataFrame(te_array, columns=te.columns_)

df.head()

"""# *apply apriori*"""

from mlxtend.frequent_patterns import apriori, association_rules

frequent_items = apriori(df, min_support=0.003, use_colnames=True)

rules = association_rules(frequent_items, metric="lift", min_threshold=3)

print(rules.head())

"""# *Generate Rules*"""

from mlxtend.frequent_patterns import association_rules

rules = association_rules(frequent_items, metric="lift", min_threshold=3)

rules.head()

"""# *Sort Rules*"""

rules = rules.sort_values(by='lift', ascending=False)
rules.head(10)

input_item = 'milk'

filtered_rules = rules[rules['antecedents'].apply(lambda x: input_item in x)]

filtered_rules[['antecedents', 'consequents', 'confidence', 'lift']]