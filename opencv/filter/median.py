import cv2 as cv
import numpy as np

img = cv.imread("thiennhien.jpg",1)
dst = cv.medianBlur(img,5)


cv.imshow("thiennhien",dst)
cv.waitKey()