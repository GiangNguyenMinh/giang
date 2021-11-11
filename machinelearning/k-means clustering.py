
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
np.random.seed(11)
M = np.array([[2, 2], [8, 3], [3, 6]])
cov = np.array([[1, 0], [0, 1]])
N = 500
X0 = np.random.multivariate_normal(M[0, :], cov, N)
X1 = np.random.multivariate_normal(M[1, :], cov, N)
X2 = np.random.multivariate_normal(M[2, :], cov, N)
X = np.concatenate((X0, X1, X2), axis=0)
K = 3
y = np.array([0]*N + [1]*N + [2]*N).T
def show_mathplot(X, y):
    X0 = X[y == 0, :]
    X1 = X[y == 1, :]
    X2 = X[y == 2, :]
    plt.plot(X0[:, 0], X0[:, 1], "b^", markersize=4, alpha=.8)
    plt.plot(X1[:, 0], X1[:, 1], "ro", markersize=4, alpha=.8)
    plt.plot(X2[:, 0], X2[:, 1], "gs", markersize=4, alpha=.8)
    plt.axis("equal")
    # plt.plot
    plt.show()

def chose_center(X ,k):
    return X[np.random.choice(X.shape[0], k, replace=False)]
def update_cluster(center):
    dis0 = cdist(X, np.array([center[0]]))
    dis1 = cdist(X, np.array([center[1]]))
    dis2 = cdist(X, np.array([center[2]]))
    X_dist = np.concatenate((dis0, dis1, dis2), axis=1)
    y_new = np.argmin(X_dist, axis=1).T
    return y_new
def update_center(X, y, K):
    center = np.zeros((K, X.shape[1]))
    for k in range(K):
        Xk = X[y == k, :]
        center[k, :] = np.mean(Xk, axis=0)
    return center
def stop_k(center, new_center):
    return set([tuple(a) for a in center]) == set([tuple(b) for b in new_center])
def Kmean(X, K):
    center_start = chose_center(X, K)
    center = [center_start]
    y = []
    while True:
        y_new = update_cluster(center[-1])
        y.append(y_new)
        new_center = update_center(X, y[-1], K)
        if stop_k(center[-1], new_center) == True:
            break
        center.append(new_center)
    return center, y
center_out, y_out = Kmean(X, K)
print(center_out[-1])
# show_mathplot(X, y_out[-1])
kmean = KMeans(n_clusters=3, random_state=0).fit(X)
print(kmean.cluster_centers_)
y_kmean = kmean.predict(X)
show_mathplot(X, y_kmean)