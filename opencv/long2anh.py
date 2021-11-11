import cv2 as cv
import numpy
img = cv.imread("nier.jpg",cv.IMREAD_COLOR)
img1 = cv.imread("nier1.jpg",cv.IMREAD_COLOR)
cv.namedWindow("nier",cv.WINDOW_NORMAL)
cv.namedWindow("nier1",cv.WINDOW_NORMAL)
# cv.namedWindow("nier2",cv.WINDOW_NORMAL)
img = img[100:300,100:300]
img1 = img1[100:900,100:900]
# img2 = cv.add(img,img1)

cv.imshow("nier",img)
cv.imshow("nier1",img1)
# cv.imshow("nier2",img2)
cv.waitKey()
cv.destroyAllWindows()
