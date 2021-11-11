import cv2 as cv

img = cv.imread("thiennhien.jpg",1)
# dst = cv.GaussianBlur(img,(5,5),0)
# cv.imshow('thiennhien',dst)
kernel = cv.getGaussianKernel(5,0)
dst = cv.filter2D(img,-1,kernel)
cv.imshow('thiennhien',dst)
cv.waitKey()