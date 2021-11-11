import cv2 as cv

img = cv.imread("smoky.jpg",1)
ret ,thres = cv.threshold(img,127,255,0,cv.THRESH_BINARY)
