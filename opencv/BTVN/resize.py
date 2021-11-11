import cv2 as cv
import numpy as np
img = cv.imread("bo_bai.jpg")
w, h = 250, 350
pts1 = np.float32([[224, 44],[428, 60],[200, 331], [403, 350]])
pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
matrix = cv.getPerspectiveTransform(pts1, pts2)
output = cv.warpPerspective(img, matrix, (w, h))
cv.imshow("Image", img)
cv.imshow("Output", output)
cv.waitKey()