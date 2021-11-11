import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# means = [[2, 2], [4, 2]]
# cov = [[.3, .2], [.2, .3]]
# N = 10
# X0 = np.random.multivariate_normal(means[0], cov, N)
# X1 = np.random.multivariate_normal(means[1], cov, N)
fig, ax = plt.subplots(figsize=(5, 5))
x = np.linspace(0, 100, 100)

def animation(i):
    anim = plt.cla()
    y = 2*np.cos(2*x - np.pi*i)
    anim = plt.plot(x, y, 'r')
    return anim
anima = FuncAnimation(fig, animation, frames= 10, interval=200)
plt.show()

