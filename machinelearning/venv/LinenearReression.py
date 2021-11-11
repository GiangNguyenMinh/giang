import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
np.random.seed(2)

X = np.random.rand(1000, 1)
one = np.ones((1000, 1))
X_train = np.concatenate((X, one), axis=1) # X train data

y = 3*X + 4
Y_train = 3*X + 4 + .2*np.random.randn(1000, 1)


w_init = np.array([[5], [1]])
N = 1000
def gradient(w, X_train, Y_train):
    gradient = -(1/N) * X_train.T.dot(Y_train - X_train.dot(w))
    return gradient
def myRegressLinear(eta, w_init, X_train, Y_train):
    w = [w_init]
    i = 0
    for it in range(100):
        w_new = w[-1] - eta* gradient(w[-1], X_train, Y_train)
        if np.linalg.norm(gradient(w_new, X_train, Y_train)) / len(w_new) < 1e-3:
            break
        w.append(w_new)
    return(w, it)


(w, it) = myRegressLinear(1, w_init, X_train, Y_train)
fig = plt.figure()


def line_draw(w):
    x = (0, 1)
    y = x*w[0] + w[1]
    plt.plot(x, y, 'b')

def animation(i):
    plt.cla()
    plt.axis([0, 1, 0, 10])
    plt.plot(X, Y_train, 'r.')
    plt.title('lan thu : {}'.format(i))
    line_draw(w[i])



ani = FuncAnimation(fig, animation, frames=it, interval=500)

plt.show()
# print(w[-1], i)
# print(X_train)
# print(Y_train)

# plt.show()
#
