import cv2 as cv
import numpy as np
vd = cv.VideoCapture(0)
vd.set(cv.CAP_PROP_FRAME_HEIGHT,500) # thiet lap chieu dai
vd.set(cv.CAP_PROP_FRAME_WIDTH,320) # thiet lap chieu rong
while 1 :
    ret,frame = vd.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.namedWindow("nier",cv.WINDOW_NORMAL)

    cv.imshow("nier",gray)
    if cv.waitKey(20) & 0xFF == ord("s"):
         break
vd.release()
cv.destroyAllWindows()
 

