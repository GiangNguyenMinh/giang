#lam avegaring lam min trumg binh
import cv2 as cv
import numpy as np


#la covolution2D nhung su dung ham viet san cv.blur() va cv.boxFilter()

img = cv.imread("thiennhien.jpg",1)
dst = cv.blur(img,(5,5))
# dst = cv.boxFilter(img,-1,(5,5),normalize=True)
cv.imshow("thiennhien",dst)
cv.waitKey()