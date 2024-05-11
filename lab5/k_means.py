import numpy as np

def initialize_centroids_forgy(data, k):
    # TODO implement random initialization
    par = data.shape[0]
    centroids = data[np.random.choice(par,k,replace=False)] 
    return centroids

def initialize_centroids_kmeans_pp(data, k): 
    # TODO implement kmeans++ initizalization 
    n_features = data.shape[1]
    centroids = np.zeros((k, n_features)) # k x d
    idx = np.random.choice(data.shape[0]) #wybor pierwszego
    centroids[0] = data[idx]
    for i in range(1, k):
        dist = np.zeros(data.shape[0]) # odleglosci od punktow
        for j in range(data.shape[0]):
            dist[j] = np.min(np.sum((data[j] - centroids[:i])**2, axis=1)) # odleglosc od najblizszego punktu
        dist = dist/np.sum(dist) # normalizacja odleglosci 
        centroids[i] = data[np.random.choice(data.shape[0], p=dist)] 
    return centroids

def assign_to_cluster(data, centroid):
    # TODO find the closest cluster for each data point
    dist  = np.sum((data[:, np.newaxis] - centroid)**2, axis=2)
    cluster = np.argmin(dist, axis=1) # indeksy najmniejszych odleglosci
    return cluster

def update_centroids(data, assignments):
    # TODO find new centroids based on the assignments
    cluster = np.unique(assignments) # unikalne indeksy
    centroids = np.zeros((len(cluster), data.shape[1])) # nowe centroidy    
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

