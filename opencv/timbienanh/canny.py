import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("ronaldo.jpg",1)
dst = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(dst,cmap="gray"),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(img[:,:,::-1]),plt.xticks([]),plt.yticks([])
plt.show()
