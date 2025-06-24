
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def kmeans_clustering(data_path, n_clusters=3):
    # Load the data
    data = pd.read_csv(data_path)
    
    # Select numeric columns only
    x = data.select_dtypes(include='number')
    
    # Scale features
    x_scaled = StandardScaler().fit_transform(x)
    
    # Fit KMeans model and get cluster labels
    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(x_scaled)
    
    # Add cluster labels to the original dataframe
    data['cluster'] = labels
    
    # Print count of each cluster
    print(data['cluster'].value_counts())
    
    # Plot the first two scaled features colored by cluster label
    plt.scatter(x_scaled[:, 0], x_scaled[:, 1], c=labels, cmap='viridis')
    plt.title("KMeans Clustering")
    plt.xlabel("Feature 1 (scaled)")
    plt.ylabel("Feature 2 (scaled)")
    plt.show()

# Example usage
kmeans_clustering("fruitsagn.csv", n_clusters=3)
