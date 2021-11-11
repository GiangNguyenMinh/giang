import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
#
# theta = 1
# w_start = np.array([[1], [5]])
# x = np.random.randn(1, 1000)
# N = x.shape[1]
# one = np.ones((1, 1000))
# X = np.concatenate((x, one), axis=0).T
# x0 = np.linspace(1, 20, 2)
# y0 = x0 + 6
# y = x + 6
# y_train = (x + 6 + np.random.randn(1, 1000)).T
# def gradient(w):
#     gra = (1/N) * X.T.dot((X.dot(w) - y_train))
#     return gra
# # def GD(w, theta, X, y_train, N):
# #     w_new = w - theta*gradient(X, y_train, w, N)
# #     return w_new
# # w_unit = [w_start]
# # for i in range(100):
# #     w_new = GD(w_unit[-1], theta, X, y_train, N)
# #     if np.linalg.norm(gradient(X, y_train, w_new, N)) / len(w_new) < 1e-3:
# #         break
# #     w_unit.append(w_new)
# #
# # print(w_unit[-1])
# # print(y_train)
# # print(y)
# #
# #
# def myGD(gradient, eta, w_start):
#     w_init = [w_start]
#     for i in range(100):
#         w_new = w_init[-1] - eta*gradient(w_init[-1])
#         if np.linalg.norm(gradient(w_new)) / len(w_new) < 1e-3:
#             break
#         w_init.append(w_new)
#     return w_init
# w_stop = myGD(gradient, theta, w_start)
# print(w_stop[-1])
#
#
#
#
# plt.plot(x0, y0)
# plt.plot(x, y_train)
# plt.show()
np.random.seed(11)
means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

X = np.concatenate((X0, X1, X2), axis = 0)
k = 3

original_label = np.asarray([0]*N + [1]*N + [2]*N).T
center = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(center[0], cov, N)
X1 = np.random.multivariate_normal(center[1], cov, N)
X2 = np.random.multivariate_normal(center[2], cov, N)
X = np.concatenate((X0, X1, X2), axis=0)
lable = np.array([0]*N + [1]*N + [2]*N).T
K = 3

def start_center(X, k):
    return X[np.random.choice(X.shape[0], k, replace=False)]
def update_cluster(X, center):
    D = cdist(X, center)
    return np.argmin(D, axis=1)
def update_center(new_lable, X, k):
    cen_new = np.zeros((k, X.shape[1]))
    for i in range(k):
        cen_new[i, :] = np.mean(X[new_lable == i, :], axis=0)
    return cen_new
def end(cen_new, center):
    return (set([tuple(a) for a in center])) == (set([tuple(a) for a in cen_new]))
def kmean(X, k):
    center_list = [start_center(X, k)]
    lable = []
    while True:
        lable.append(update_cluster(X, center_list[-1]))
        cen_new = update_center(lable[-1], X, k)
        if end(cen_new, center_list[-1]):
            break
        center_list.append(cen_new)
    return center_list
all_center = kmean(X, k)
print(all_center[-1])
print(lable)
# def kmeans_init_centers(X, k):
#     # randomly pick k rows of X as initial centers
#     return X[np.random.choice(X.shape[0], k, replace=False)]
#
# def kmeans_assign_labels(X, centers):
#     # calculate pairwise distances btw data and centers
#     D = cdist(X, centers)
#     # return index of the closest center
#     return np.argmin(D, axis = 1)
#
# def kmeans_update_centers(X, labels, K):
#     centers = np.zeros((K, X.shape[1]))
#     for k in range(K):
#         # collect all points assigned to the k-th cluster
#         Xk = X[labels == k, :]
#         # take average
#         centers[k,:] = np.mean(Xk, axis = 0)
#     return centers
#
# def has_converged(centers, new_centers):
#     # return True if two sets of centers are the same
#     return (set([tuple(a) for a in centers]) ==
#         set([tuple(a) for a in new_centers]))
# def kmeans(X, K):
#     centers = [kmeans_init_centers(X, K)]
#     labels = []
#     it = 0
#     while True:
#         labels.append(kmeans_assign_labels(X, centers[-1]))
#         new_centers = kmeans_update_centers(X, labels[-1], K)
#         if has_converged(centers[-1], new_centers):
#             break
#         centers.append(new_centers)
#         it += 1
#     return (centers, labels, it)
# (centers, labels, it) = kmeans(X, K)
# print('Centers found by our algorithm:')
# print(centers[-1])
kmeann = KMeans(n_clusters=3, random_state=0).fit(X)
print(kmeann.cluster_centers_)
print(kmeann.predict(X))
