#Agglomerative clustering
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

def agglomerative_clustering(data_path):
    data = pd.read_csv(data_path)
    X = data.select_dtypes(include='number')
    X_scaled = StandardScaler().fit_transform(X)

    for method in ['single', 'complete']:
        model = AgglomerativeClustering(n_clusters=3, linkage=method)
        labels = model.fit_predict(X_scaled)
        print(f"\nLinkage: {method}")
        print(pd.Series(labels).value_counts())

        # Plot dendrogram
        Z = linkage(X_scaled, method=method)
        plt.figure(figsize=(8, 4))
        dendrogram(Z, truncate_mode='lastp', p=12)
        plt.title(f"{method.capitalize()} Linkage Dendrogram")
        plt.show()

# Example usage
agglomerative_clustering("glass.csv")
agglomerative_clustering("fruits.csv")
agglomerative_clustering("IRIS.csv")
