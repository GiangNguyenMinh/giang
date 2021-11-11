import cv2 as cv
import numpy as np
import os
img = cv.imread("kia.png", 1)
gray_img1 = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
gray_img = cv.resize(gray_img1, (14, 28))
cv.imshow("img", gray_img)
print(gray_img.shape)
cv.waitKey()

