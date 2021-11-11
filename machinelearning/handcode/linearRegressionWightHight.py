import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("E:/data/chieucaocannang/chieucaocannang.csv",header=0)
X = np.array([data.values[:,0]]).T
y = np.array([data.values[:,1]]).T
# plt.scatter(X,y,100,'r','o')
# plt.show()
one = np.ones((X.shape[0],1),dtype= np.uint8)
Xbar = np.concatenate((one,X),axis=1)
A = np.dot((Xbar.T),Xbar)
B = np.dot((Xbar.T),y)
w = np.dot(np.linalg.pinv(A),B)
bias = w[0,0]
wight = w[1][0]
x0 = np.linspace(145,2,180)
y0 = wight * x0 + bias
plt.plot(x0,y0)
plt.show()
def predict (x_test,wight,bias):
    return x_test*wight+bias
print(predict(169,wight,bias))