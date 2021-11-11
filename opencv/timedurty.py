import cv2 as cv
import numpy as np
e1 = cv.getTickCount()
for i in range(3):
    print(i)
e2 = cv.getTickCount()
print("time is :" ,(e2-e1)/cv.getTickFrequency())