import cv2 as cv
import numpy as np
img = cv.imread("nier.jpg",1)
row = img.shape[0]
col = img.shape[1]
M = cv.getRotationMatrix2D((col/2,row/2),90,1)
imgro = cv.warpAffine(img,M,(col,row))
cv.imshow("nier",imgro)
cv.waitKey()