# main.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Calculations
from sklearn.cluster import KMeans, SpectralClustering

# Calculations.avg_and_stdev_per_day_per_share() #Creating the calculated file for Seif A
# Calculations.avg_and_beta_per_day_per_share() #Creating the calculated file for Seif B

Market = pd.read_csv('avg_and_stdev_per_day_per_share.csv')

# Using the K-Means algorithm with the calculated data:
X = Market.iloc[2:, [2, 3]].values


# kmeans = KMeans(n_clusters=5,)
# y_kmeans = kmeans.fit_predict(X)



model = SpectralClustering(n_clusters=2, affinity='nearest_neighbors',
                           assign_labels='kmeans')
y_kmeans = model.fit_predict(X)


# Creating a chart of the calculated K-means algorithm:  REGARDING Seif A & B
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], label = 'cluster1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], label = 'cluster2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], label = 'cluster3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], label = 'cluster4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], label = 'cluster5')
plt.title('Average and Standard Deviation Table')
plt.xlabel('Average')
plt.ylabel('Standard Deviation')
plt.legend()

plt.show()



