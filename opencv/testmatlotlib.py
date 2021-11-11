import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("nier.jpg",1)
# img1 = cv.imread("nier1.jpg",cv.IMREAD_COLOR)
# plt.subplot(1,2,1),plt.imshow(img),plt.title("anh nier ")
# plt.subplot(1,2,2),plt.imshow(img1),plt.title("anh nier1")
plt.imshow(img[:,:,::-1])
plt.show()