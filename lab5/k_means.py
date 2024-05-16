import numpy as np

def initialize_centroids_forgy(data, k):
    # TODO implement random initialization
    par = data.shape[0] 
    centroids = data[np.random.choice(par,k,replace=False)] 
    return centroids

def initialize_centroids_kmeans_pp(data, k): 
    # TODO implement kmeans++ initizalization 
    n_samples, n_features = data.shape
    centroids = np.zeros((k, n_features))

    first_centroid_idx = np.random.choice(n_samples)
    centroids[0] = data[first_centroid_idx]

    for i in range(1, k):
        distances = np.zeros(n_samples)
        for j in range(n_samples): 
            distances[j] = np.sum((data[j] - centroids[:i]) ** 2, axis=1).min()
        next_centroid_idx = np.argmax(distances)
        centroids[i] = data[next_centroid_idx]

    return centroids

def assign_to_cluster(data, centroid):
    # TODO find the closest cluster for each data point
    dist  = np.sum((data[:, np.newaxis] - centroid)**2, axis=2)
    cluster = np.argmin(dist, axis=1) 
    return cluster

def update_centroids(data, assignments):
    # TODO find new centroids based on the assignments
    cluster = np.unique(assignments) 
    centroids = np.zeros((len(cluster), data.shape[1]))  
    for i in cluster:
        centroids[i] = np.mean(data[assignments==i], axis=0)
    return centroids

def mean_intra_distance(data, assignments, centroids):
    return np.sqrt(np.sum((data - centroids[assignments, :])**2))

def k_means(data, num_centroids, kmeansplusplus= False):
    # centroids initizalization
    if kmeansplusplus:
        centroids = initialize_centroids_kmeans_pp(data, num_centroids)
    else: 
        centroids = initialize_centroids_forgy(data, num_centroids)

    
    assignments  = assign_to_cluster(data, centroids)
    for i in range(100): # max number of iteration = 100
        print(f"Intra distance after {i} iterations: {mean_intra_distance(data, assignments, centroids)}")
        centroids = update_centroids(data, assignments)
        new_assignments = assign_to_cluster(data, centroids)
        if np.all(new_assignments == assignments): # stop if nothing changed
            break
        else:
            assignments = new_assignments

    return new_assignments, centroids, mean_intra_distance(data, new_assignments, centroids)         

