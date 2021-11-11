import cv2 as cv
import numpy as np


def nothing(x):
    pass
img = np.zeros((512,512,3),np.uint8)
cv.namedWindow("nier",cv.WINDOW_NORMAL)

cv.createTrackbar("r","nier",0,255,nothing)
cv.createTrackbar("b","nier",0,255,nothing)
cv.createTrackbar("g","nier",0,255,nothing)
img = np.zeros((512,512,3),np.uint8)
cv.namedWindow("nier",cv.WINDOW_NORMAL)


while 1:
    r = cv.getTrackbarPos("r","nier")
    b = cv.getTrackbarPos("b","nier")
    g = cv.getTrackbarPos("g","nier")
    img[:,:,:] = [b,g,r]
    cv.imshow("nier",img)
    if cv.waitKey(20) & 0xFF == ord('s'):
        break
cv.destroyAllWindows()