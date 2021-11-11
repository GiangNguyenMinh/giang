import cv2 as cv
import numpy as np
img = cv.imread("anh.png",1)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
thres,br = cv.threshold(gray,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
dst = cv.morphologyEx(br,cv.MORPH_GRADIENT,kernel)
cv.namedWindow("anh",cv.WINDOW_NORMAL)
cv.imshow("anh",dst)
cv.waitKey()
# tao kernel
print(cv.getStructuringElement(cv.MORPH_RECT,(5,5)))
print(cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)))
print(cv.getStructuringElement(cv.MORPH_CROSS,(5,5)))

