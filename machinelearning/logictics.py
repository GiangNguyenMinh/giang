import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
np.random.seed(2)


X = np.array([[0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50,
              2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]])
y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

X = np.concatenate((np.ones((1, X.shape[1])), X), axis=0)
X0 = X[1, np.where(y == 0)][0]
y0 = y[np.where(y == 0)]
X1 = X[1, np.where(y == 1)][0]
y1 = y[np.where(y == 1)]

w_init = np.random.randn(X.shape[0], 1)
eta = .05


def sigmor_function(s):
    return 1/(1 + np.exp(-s))

def logictic(X, y, w_init, eta, tol = 1e-4, max_count = 10000):
    w = [w_init]
    N = X.shape[1]
    d = X.shape[0]
    count = 0
    check_w_after = 20
    while count < max_count:
        mix_id = np.random.permutation(N)
        for i in mix_id:
            xi = X[:, i].reshape(d, 1)
            yi = y[i]
            zi = sigmor_function(np.dot(w[-1].T, xi))
            w_new = w[-1] + eta*(yi - zi) * xi
            count += 1
            if count % check_w_after == 0:
                if np.linalg.norm(w_new - w[-check_w_after]) < tol:
                    return w, count
            w.append(w_new)
    return w, count
fig = plt.figure()
w, count = logictic(X, y, w_init, eta)
xx = np.linspace(0, 6, 1000)
print(w[-1])

# def sigmoid(s):
#     return 1/(1 + np.exp(-s))
#
# def logistic_sigmoid_regression(X, y, w_init, eta, tol = 1e-4, max_count = 10000):
#     w = [w_init]
#     it = 0
#     N = X.shape[1]
#     d = X.shape[0]
#     count = 0
#     check_w_after = 20
#     while count < max_count:
#         # mix data
#         mix_id = np.random.permutation(N)
#         for i in mix_id:
#             xi = X[:, i].reshape(d, 1)
#             yi = y[i]
#             zi = sigmoid(np.dot(w[-1].T, xi))
#             w_new = w[-1] + eta*(yi - zi)*xi
#             count += 1
#             # stopping criteria
#             if count%check_w_after == 0:
#                 if np.linalg.norm(w_new - w[-check_w_after]) < tol:
#                     return w
#             w.append(w_new)
#     return w
# eta = .05
# d = X.shape[0]
# w_init = np.random.randn(d, 1)
#
# w = logistic_sigmoid_regression(X, y, w_init, eta)
# print(w[-1])

def draw_function(w):
    yy = sigmor_function(w[0, 0] + w[1, 0]*xx)
    plt.plot(xx, yy, 'g-', linewidth=2)


def animation(i):
    plt.cla()
    plt.axis([-2, 8, -1, 2])
    plt.plot(X0, y0, 'bo')
    plt.plot(X1, y1, 'ro')
    plt.xlabel("X")
    plt.ylabel('Y')
    plt.title('lan thu: {}'.format(i))
    draw_function(w[i])



anim = FuncAnimation(fig, animation, frames=count, interval=200)
plt.show()
