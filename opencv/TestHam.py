import cv2 as cv
import numpy as np
img = cv.imread("nier.jpg",1)
img1 = cv.imread("nier1.jpg",1)
print(img.shape)
img2 = img1[0:300,0:620]
dst = cv.subtract(img,img2)
cv.imshow("nier",dst)
cv.waitKey()
cv.destroyAllWindows()
for i in range(5,0,-1):
    print(i)