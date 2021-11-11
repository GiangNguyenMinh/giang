import cv2 as cv
import numpy as np
img = cv.imread("nier1.jpg",cv.IMREAD_COLOR)

row = img.shape[1]
col = img.shape[0]
M = np.array([[1,0,50],[0,1,-50]],dtype=np.float32)
dsr = cv.warpAffine(img,M,(row,col))
cv.namedWindow("nier",cv.WINDOW_NORMAL)
cv.imshow("nier",dsr)
cv.waitKey()
