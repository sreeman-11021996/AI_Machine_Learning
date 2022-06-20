import random
import numpy as np

class KMeans:
    def __init__(self,n_clusters=2,max_iter=200,tol = 0.00001):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        #self.tol = tol

    def fit_predict(self,X):
        X = np.array(X)
        # 1. initialize centroids
        random_indexes = random.sample(range(X.shape[0]),self.n_clusters)
        self.centroids = X[random_indexes]

        for iter in range(self.max_iter):
            # 2. assign clusters
            cluster_group = self.assign_clusters(X)
            old_centroids = np.array(self.centroids)
            # 3. move the clusters
            self.centroids = self.get_new_centroids(X,cluster_group)

            # 4. final check
            if (old_centroids == self.centroids).all():
                # calculate the inertia_
                self.inertia_ = self.cal_inertia(X,cluster_group)
                break
            """optimized = True
            for k in range(len(self.centroids)):
                orig_centroid = old_centroids[k]
                curr_centroid = self.centroids[k]
                if np.sum((curr_centroid-orig_centroid)/orig_centroid*100) > self.tol:
                    optimized = False
            if optimized:
                break"""

        return cluster_group

    def assign_clusters(self,X):
        distance = []
        cluster_group = []
        for point in X:
            for centroid in self.centroids:
                # get the euclidean dist
                distance.append(np.sqrt(np.dot(point-centroid,point-centroid)))
            min_distance = min(distance)
            cluster_group.append(distance.index(min_distance))
            distance.clear()

        return np.array(cluster_group)

    def get_new_centroids (self,X,cluster_group):

        new_centroids = []
        cluster_type = np.unique(cluster_group)
        # get the centroids from clusters
        for type in cluster_type:
            new_centroids.append(X[cluster_group == type].mean(axis=0))

        return np.array(new_centroids)

    def cal_inertia (self,X,cluster_group):
        distance = []
        inertia_cluster = []
        cluster_type = np.unique(cluster_group)
        for type in cluster_type:
            for point in X[cluster_group == type]:
                # get the euclidean dist
                distance.append(np.sqrt(np.dot(point-self.centroids[type],
                                               point- self.centroids[type])))
            inertia_cluster.append(np.sum(np.power(distance, 2)))
            distance.clear()

        return np.sum(inertia_cluster)