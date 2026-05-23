import math
from collections import Counter

def euclidean(a, b):
  return math.sqrt(sum([(x-y)**2 for x, y in zip(a, b)]))

def knn_predict(X_train, y_train, new_point, k):
  # compute distances to all training points
  dists = []
  for point in X_train:
    dists.append(euclidean(point, new_point))

  # sort by distance => grab k nearest labels
  paired = sorted(zip(dists, y_train))[:k]
  top_k_labels = [y for dist, y in paired]

  # majority vote
  freq = Counter(top_k_labels)
  return max(freq, key=freq.get)

X_train = [[1,1], [2,1], [1,2],   # class 0
           [8,8], [9,8], [8,9]]   # class 1
y_train = [0, 0, 0, 1, 1, 1]

print(knn_predict(X_train, y_train, [1.5, 1.5], k=3))  # 0
print(knn_predict(X_train, y_train, [8.5, 8.5], k=3))  # 1