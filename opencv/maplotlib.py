import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
# plt.scatter(14,15,250,"r","s")
# plt.scatter(35,34,250,"b","P")
# ig = np.random.randint(10,100,[4,3])
#
#
#
#
#
# plt.show()
# print(ig)
# print(ig.ravel())
# plt.figure(figsize=(15,5))
# plt.plot([1,2,3,4],[1,4,9,16])
# plt.xlabel("truc x")
# plt.ylabel("truc y")
# plt.title("do thi ")
# plt.show()
#
#
#
#
#
#
plt.figure(figsize=(15,15))
x = np.arange(3)
y = x**2
plt.subplot(1,2,1)
plt.plot([1,2,3,4],[1,4,9,16],"r")
plt.title("hang 1 ")
plt.subplot(1,2,2)
plt.plot(x,y,"*")
plt.title("hang 2")
plt.suptitle("hai bang")
plt.show()
