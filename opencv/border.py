import cv2 as cv
import numpy as np
img  = cv.imread("nier1.jpg")
img = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_CONSTANT,value =(0,0,255))
# img = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REPLICATE)
# img = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REFLECT)
# img = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REFLECT_101)
# img = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_WRAP)
# img = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_DEFAULT)

cv.namedWindow("nier",cv.WINDOW_NORMAL)
cv.imshow("nier",img)
cv.waitKey()