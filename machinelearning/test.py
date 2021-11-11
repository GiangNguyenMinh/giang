import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# fig = plt.figure()
# axits = plt.axes(xlim=(0, 12), ylim=(0, 12))
# x = np.linspace(0, 10, 100)
# y = np.sqrt(100 - x*x)
# plt.plot(x, y, x, -y)
# plt.grid()
#
# [X0, Y0] = [0, 10]
# [Xf, Yf] = [10, 10]
# deltaX = 2*X0 + 1
# deltaY = -2*Y0 + 1
# Xout = [X0]
# Yout = [Y0]
# D = 0
# while(Xf!=0 and Yf!=0):
#     if D > 0:
#         D = D + deltaY
#         deltaY = deltaY + 2
#         Y0 = Y0 - 1
#         Yout.append(Y0)
#         Yf = Yf - 1
#     else:
#         D = D + deltaX
#         deltaX = deltaX + 2
#         X0 = X0 + 1
#         Xout.append(X0)
#         Xf = Xf - 1
# print(Yout)
# plt.plot(Xout, Yout, "r.", 50)
# plt.show()
#
#
# def animation(i):
#     pass

xm = np.arange(-2, 11, 0.025)
xlen = len(xm)
ym = np.arange(-3, 10, 0.025)
ylen = len(ym)
xx, yy = np.meshgrid(xm, ym)


# xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
# xx.ravel(), yy.ravel()
print(np.ones((1, xx.size)).shape)
xx1 = xx.ravel().reshape(1, xx.size)
yy1 = yy.ravel().reshape(1, yy.size)
print(xx1)
