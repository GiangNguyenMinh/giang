import cv2 as cv
import numpy as np
img = cv.imread("open.png",1)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
thres,br = cv.threshold(gray,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
kernel = np.ones((11,11),dtype=np.uint8)
dst = cv.morphologyEx(br,cv.MORPH_OPEN,kernel)# erode truoc roi dilate
dst = cv.morphologyEx(br,cv.MORPH_CLOSE,kernel)
# cv.namedWindow("open",cv.WINDOW_NORMAL)# dilate trc roif erode
cv.imshow("open",dst)
cv.waitKey()