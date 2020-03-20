import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
import Calculations

Market = pd.read_csv('ShareData/afi.csv')
# print(Market)

X = Market.iloc[2:,[2,3]].values

#X = Calculations.avg_per_day_per_share('afi.csv')

Calculations.avg_and_stdev_per_day_per_share()


#avg and teken for X

kmeans = KMeans(n_clusters=5)
y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], label = 'cluster1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], label = 'cluster2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], label = 'cluster3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], label = 'cluster4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], label = 'cluster5')

plt.title('Clusters')
plt.xlabel('AVG????')
plt.ylabel('TEKEN???')
plt.legend()

#plt.show()