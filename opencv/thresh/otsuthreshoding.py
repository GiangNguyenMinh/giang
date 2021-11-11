import cv2 as cv
import numpy as np

im = cv.imread("nier1.jpg",cv.IMREAD_COLOR)
gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
reVal , frame = cv.threshold(gray,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
print(reVal)
cv.imshow("nier",frame)
cv.waitKey()
