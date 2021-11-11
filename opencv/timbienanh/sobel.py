import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("ronaldo.jpg",0)

sobelx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]],dtype=np.float64)
sobely = np.array([[-1,-2,-1],[0,0,0],[1,2,1]],dtype=np.float64)
dstx = cv.filter2D(img,-1,sobelx)
dsty = cv.filter2D(img,-1,sobely)
plt.subplot(1,2,1),plt.imshow(dstx,cmap="gray")
plt.subplot(1,2,2),plt.imshow(dsty,cmap="gray")
plt.show()
# cv.imshow("sobel",dsty)
# cv.waitKey()
# cv.destroyAllWindows()