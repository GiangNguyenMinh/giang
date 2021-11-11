import cv2 as cv


img = cv.imread("thiennhien.jpg",1)
dst = cv.bilateralFilter(img,9,75,75)
cv.imshow("thiennhien",dst)
cv.waitKey()