import numpy  as np
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model
np.random.seed(2)
x = np.random.rand(1000,1)
y = 4*x + 3 + .2*np.random.randn(1000, 1)
one = np.ones((x.shape[0], 1))
Xbar = np.concatenate((one, x), axis= 1)
# def gradient(w):
#     N = x.shape[0]
#     return 1/N * Xbar.T.dot(Xbar.dot(w)-y)
# def GD(w, gradient, eta):
#     w_unit = [w]
#     for i in range(50):
#         w_new = w_unit[-1] - eta*gradient(w_unit[-1])
#         if np.linalg.norm(gradient(w_new))/len(w_new)<1e-3:
#             break
#         w_unit.append(w_new)
#     return (w_unit, i)
# w = np.array([[2], [1]])
# wb ,i = GD(w, gradient, 1)
# print('gia tri cua w la:', wb[-1], ',sau %d lan'%i)
# plt.figure()
# plt.axes(xlim=(0, 1),ylim=(0, 10))
# plt.plot(x.T, y.T, "b.")
# x_test = np.linspace(0, 1, 100)
# plt.plot(x_test, (wb[-1][0, 0] + wb[-1][1, 0]*x_test).T, "r")
# plt.plot(x_test, 4*x_test+3, 'y')
# plt.show()
lre = linear_model.LinearRegression(fit_intercept=False)
lre.fit(Xbar, y)
print(lre.coef_)