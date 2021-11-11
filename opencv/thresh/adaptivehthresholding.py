import cv2 as cv
import numpy as np

img = cv.imread("nier1.jpg",cv.IMREAD_COLOR)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
thr1 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,0)
cv.namedWindow("nier",cv.WINDOW_NORMAL)
cv.imshow("nier",thr1)
cv.waitKey()
cv.destroyAllWindows()
