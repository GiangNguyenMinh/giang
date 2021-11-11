import cv2 as cv

img = cv.imread("anh1.jpg",1)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)
cv.waitKey()