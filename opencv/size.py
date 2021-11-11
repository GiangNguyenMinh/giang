import cv2 as cv
import numpy as np

img = cv.imread("nier.jpg",cv.IMREAD_COLOR)
img1 = cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
cv.imshow("nier",img1)
cv.imshow("nier1",img)
cv.waitKey()
cv.destroyAllWindows()
