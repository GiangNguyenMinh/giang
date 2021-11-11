import cv2 as cv
import numpy as np

ig = np.zeros((512,512,3))
cv.line(ig,(0,0),(512,512),(255,0,0),5)
cv.circle(ig,(200,400),100,(0,255,0),-1)
cv.rectangle(ig,(200,100),(100,200),(0,0,255),5)
cv.ellipse(ig,(156,156),(100,50),90,0,360,(45,12,98),5)# ve duong ellip neu chi so thu 3 bang nhau thi ve duong tron
cv.imshow("draw",ig)
cv.waitKey()
cv.destroyAllWindows()