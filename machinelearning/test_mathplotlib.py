import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
high = np.random.randn(100)*10
widh = np.random.randn(100)*10
z = np.random.randn(100)*10
ax = plt.axes(projection='3d')
ax.scatter3D(high, widh,z)
ax.set_xlable = "height"
ax.set_ylable = 'wight'
plt.show()



# fig = plt.figure()
# axit = plt.axes(xlim=(), ylim=())
# x = 0
# x = 2*x + 5*np.cos(x)
# y = x**2 + 5*np.sin(x)
