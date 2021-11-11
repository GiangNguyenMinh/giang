import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("E:/data/advertisingdata/archive/Advertising.csv",header=0)
X = data.values[:,1]
y = data.values[:,4]
# plt.scatter(X,y,marker="o")
# plt.show()
def predict (x_test,wight,bias):
    return x_test*wight+bias
def cost_funcion (X,y,wight,bias):
    n = len(X)
    sum = 0
    for i in range(n):
        sum += (y[i] - wight*X[i] + bias)**2
    return (1/(2*n))*sum
def update_wb(X,y,wight,bias,learning_rate):
    n = len(X)
    for i in range(n):
        wight_sum = -X[i]*(y[i]-(wight*X[i]+ bias))
        bias_sum = -(y[i]-(wight*X[i]+bias))
    wight -= wight_sum* learning_rate /(2*n)
    bias -= bias_sum * learning_rate/ (2*n)
    return wight,bias
def train(X,y,wight,bias,learning_rate,iter):
    cost_his = []
    for i in range(iter):
        wight, bias = update_wb(X, y, wight, bias, learning_rate)
        cost = cost_funcion(X,y,wight,bias)
        cost_his.append(cost)
    return wight,bias,cost_his
wight_train,bias_train,cost_lis = train(X,y,0.03,0.0014,0.001,60)
print(wight_train)
print(bias_train)
test = predict(227,wight_train,bias_train)
print(test)
