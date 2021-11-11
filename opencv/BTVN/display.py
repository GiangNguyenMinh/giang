import cv2 as cv
img = cv.imread("anh1.jpg",1)
cv.namedWindow("img",cv.WINDOW_NORMAL)
cv.imshow("img",img)
cv.waitKey()
cv.destroyAllWindows()