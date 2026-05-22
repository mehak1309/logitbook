import random
import math

def euclidean(p1, p2):
  res = 0
  for xi, xj in zip(p1, p2):
    res += (xi-xj)**2
  return math.sqrt(res)

def get_mean(points): # list of points [[2, 3], [3, 4]]
  n, d = len(points), len(points[0])
  mean = []
  for i in range(d):
    s = 0
    for p in points:
      s += p[i]
    mean.append(s/n)
  return mean
      
def kmeans(X, k, max_iters):
  # initialize
  centroids = random.sample(X, k=k)

  for _ in range(max_iters):
    clusters = [[] for _ in range(k)]
    labels = []

    # calculate distance to centroid
    for point in X:
      dist = [euclidean(point, centroid) for centroid in centroids]
      cluster_id = dist.index(min(dist))
      clusters[cluster_id].append(point)
      labels.append(cluster_id)
    
    # re-calculate centroids
    new_centroids = [get_mean(cluster) if cluster else centroids[i] for i, cluster in enumerate(clusters) ]

    # convergence?
    if new_centroids == centroids:
      break

    centroids = new_centroids
  return labels, centroids


X = [[1,1], [1,2], [2,1],   # cluster A
     [8,8], [9,8], [8,9]]   # cluster B

labels, centroids = kmeans(X, k=2, max_iters=10)
print(labels)     # [0,0,0,1,1,1]  (or flipped)
print(centroids)  # [[1.33,1.33], [8.33,8.33]]