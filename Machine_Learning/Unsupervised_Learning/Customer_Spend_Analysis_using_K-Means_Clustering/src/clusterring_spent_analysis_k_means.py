# Clustering Spent Analysis using K-Means

## Importing the basic librarie

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Uploading the dataset from local system
# Note: In Google Colab, you can use the following code to upload files from your local system.
# If you're running this code in a different environment, make sure to adjust the file path accordingly.

# from google.colab import files
# uploaded = files.upload()

# Assuming the dataset is named 'dataset.csv' and is in the same directory as this script

dataset = pd.read_csv('dataset.csv')

# Displaying basic information about the dataset

print(dataset.shape)
print(dataset.info())
print(dataset.describe())
print(dataset.head())

# Selecting the relevant features for clustering

X = dataset[['INCOME','SPEND']].values

# Using the Elbow Method to find the optimal number of clusters (k)

from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
  km = KMeans(n_clusters=i, init="k-means++", n_init=10, random_state=0)
  km.fit(X)
  wcss.append(km.inertia_)
plt.figure(figsize=(8,5))
plt.plot(range(1,11),wcss,color="red", marker ="8")
plt.title('Optimal K Value')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

# Based on the Elbow Method, we can choose k=4 for clustering.

model=KMeans(n_clusters=4, random_state=0)
y_means = model.fit_predict(X)

# Visualizing the clusters and their centroids

"""Cluster 1: Customers with medium income and low spend

Cluster 2: Customers with high income and medium to high spend

Cluster 3: Customers with low income

Cluster 4: Customers with medium income but high spend
"""

plt.figure(figsize=(8,6))

colors = ['brown','blue','green','cyan']

for i in range(4):
    plt.scatter(X[y_means==i,0],
                X[y_means==i,1],
                s=60,
                c=colors[i],
                label=f'Cluster {i+1}')

plt.scatter(model.cluster_centers_[:,0],
            model.cluster_centers_[:,1],
            s=200,
            c='yellow',
            marker='X',
            label='Centroids')

plt.title("Customer Income-Spend Clustering")
plt.xlabel("Income")
plt.ylabel("Spend")
plt.legend()
plt.show()


# ---------- User Input ----------

income = float(input("Enter Customer Income: "))
splend = float(input("Enter Customer Spending: "))

new_customer = np.array([[income, splend]])

# Predict cluster
cluster = model.predict(new_customer)

print("\nCustomer belongs to Cluster:", cluster[0]+1)

if cluster[0] == 0:
    print("Customer Type: Medium Income - Low Spend")
elif cluster[0] == 1:
    print("Customer Type: High Income - High Spend")
elif cluster[0] == 2:
    print("Customer Type: Low Income Customer")
elif cluster[0] == 3:
    print("Customer Type: Medium Income - High Spend")