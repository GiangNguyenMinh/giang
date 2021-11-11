import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("thiennhien.jpg",cv.IMREAD_COLOR)
kernel = np.ones((5,5),dtype= np.float32)/25
dst = cv.filter2D(img,-1,kernel)
cv.imshow("thiennhien",dst)
cv.waitKey()