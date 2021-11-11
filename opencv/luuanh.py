import cv2 as cv
import numpy
img = cv.imread("nier.jpg",cv.IMREAD_COLOR)
cv.line(img,(0,0),(200,200),(0,0,255),5)
img[100:200,100:200,1] = 255
for i in range(200):
    for j in range(200):
        if img[i,j,1] > 30:
            img[i,j] = 1

for k in range(100):
    for n in range(100):
        img[k,n,:] = [23,133,32]



# img = img[:,:,0]

cv.namedWindow("nier",cv.WINDOW_NORMAL)
cv.imshow("nier",img)
cv.waitKey(0)
cv.imwrite("niercopy.jpg",img)
cv.destroyAllWindows()