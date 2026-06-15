# Hierarchical Clustering on Customer Data


# Importing necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Uploading the dataset
# Note: In a local environment, you would typically use pd.read_csv('path_to_file.csv') to load your dataset.
# Since this code is intended for Google Colab, we use the files.upload() method to upload the dataset directly from the local machine.

# from google.colab import files
# uploaded = files.upload()

# After uploading, you can read the dataset using pd.read_csv() as shown below.

dataset = pd.read_csv('dataset.csv')

# Initial Data Exploration

print("\nMissing Values:\n", dataset.isnull().sum())

print("\nData Types:\n", dataset.dtypes)

# Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(dataset.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# Distribution plots
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.histplot(dataset['Annual Income (k$)'], kde=True)
plt.title("Income Distribution")

plt.subplot(1,2,2)
sns.histplot(dataset['Spending Score'], kde=True)
plt.title("Spending Score Distribution")

plt.show()

# Gender vs Spending
plt.figure(figsize=(6,4))
sns.boxplot(x='Gender', y='Spending Score', data=dataset)
plt.title("Spending Score by Gender")
plt.show()

# Pairplot to visualize relationships
sns.pairplot(dataset, hue='Gender', vars=['Annual Income (k$)', 'Spending Score'])
plt.suptitle("Pairplot of Income and Spending Score", y=1.02)
plt.show()

# Selecting only important features
X_vis = dataset.iloc[:, [3,4]].values

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X_vis)

# Visualize the scaled data

print(dataset.shape)
print(dataset.describe())
print(dataset.head(5))

# Encoding the Gender column to numeric values for clustering analysis

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
dataset['Gender'] = label_encoder.fit_transform(dataset['Gender'])
print("\nEncoded Gender Values:\n", dataset['Gender'].value_counts())
dataset.head()

# Selecting only relevant features
X = dataset[['Annual Income (k$)', 'Spending Score']].values

# Scaling the features to ensure that they are on the same scale for clustering analysis

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Visualize the scaled data

import scipy.cluster.hierarchy as clus
import matplotlib.pyplot as plt

plt.figure(1, figsize = (16 ,8))
dendrogram = clus.dendrogram(clus.linkage(X_scaled, method="ward"))

plt.title('Dendrogram Tree Graph')
plt.xlabel('Customers')
plt.ylabel('Distances')
plt.show()

# From the dendrogram, we can see that there are 5 distinct clusters of customers based on their annual income and spending score. The vertical lines in the dendrogram represent the distances between clusters, and the horizontal lines represent the clusters themselves. By cutting the dendrogram at a certain distance, we can determine the optimal number of clusters for our analysis. In this case, cutting the dendrogram at a distance that results in 5 clusters seems to be a reasonable choice based on the visual representation.

# Hierarchical Clustering

from sklearn.cluster import AgglomerativeClustering

model = AgglomerativeClustering(n_clusters=5, metric='euclidean', linkage='ward')
y_means = model.fit_predict(X)

print(y_means)

# Evaluating the clustering results using silhouette score

from sklearn.metrics import silhouette_score

score = silhouette_score(X_scaled, y_means)
print("\nSilhouette Score:", score)

# The silhouette score is a measure of how well the clusters are separated and how cohesive they are. A higher silhouette score indicates that the clusters are well-defined and distinct from each other. In this case, the silhouette score can help us assess the quality of our hierarchical clustering results and determine if the chosen number of clusters (n=5) is appropriate for our dataset.

from sklearn.metrics import silhouette_score

score = silhouette_score(X, y_means)
print("Silhouette Score:", score)

plt.figure(figsize=(8,6))

#   

"""Cluster 1: Customers with Medium Income and Medium Spending

Cluster 2: Customers with High Income and High Spending

Cluster 3: Customers with Low Income and Low Spending

Cluster 4: Customers with High Income and Low Spending

Cluster 5: Customers with Low Income and High Spending
"""

# Convert to DataFrame for better plotting
df_vis = pd.DataFrame(X, columns=['Income', 'Spending'])
df_vis['Cluster'] = y_means

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df_vis,
    x='Income',
    y='Spending',
    hue='Cluster',
    palette='Set1',
    s=100
)

plt.title("Customer Segments (Hierarchical Clustering)")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")

plt.legend()
plt.show()