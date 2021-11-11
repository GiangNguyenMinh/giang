import cv2 as cv
import numpy as np

def thres_hole(_):
    pass

img = cv.imread("nier.jpg",cv.IMREAD_COLOR)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.namedWindow("nier",cv.WINDOW_NORMAL)
cv.createTrackbar("thres","nier",0,255,thres_hole)
while 1 :
    thres = cv.getTrackbarPos("thres","nier")
    ret , frame = cv.threshold(gray,thres,255,cv.THRESH_BINARY)
    cv.imshow("nier",frame)
    if cv.waitKey(20) & 0xFF == ord("s"):
        break
cv.destroyAllWindows()



