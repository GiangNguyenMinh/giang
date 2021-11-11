import cv2 as cv
import numpy as np


ig = cv.imread("ve.png",cv.IMREAD_COLOR)
cv.namedWindow("ve",cv.WINDOW_NORMAL)

min_mau = np.array([231,162,0])
max_mau = np.array([233,162,0])
final = cv.inRange(ig,min_mau,max_mau)
tach = cv.bitwise_and(ig,ig,mask = final)



cv.imshow("nier",tach)
cv.imshow("ve",final)
cv.waitKey()
