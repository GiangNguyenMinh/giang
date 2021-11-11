import cv2 as cv
import numpy as np
def callBackmouse(event,x,y,flag,prama):
    if event == cv.EVENT_LBUTTONDOWN :
        cv.circle(img,(x,y),50,(255,0,0),-1)
img = np.zeros((512,512,3),np.uint8)
cv.namedWindow("img",cv.WINDOW_NORMAL)
cv.setMouseCallback("img",callBackmouse)
while (1):
    cv.imshow("img",img)
    if cv.waitKey(20) & 0xFF == ord('s'):
        break
cv.destroyAllWindows()

