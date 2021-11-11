import cv2 as cv
import numpy as np
img = np.zeros((512, 512, 3), dtype=np.uint8)
cv.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv.putText(img, "Giang", (300, 100), cv.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
cv.imshow("img", img)
cv.waitKey()

