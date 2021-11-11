import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("anh.png",1)
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# thres,igbr = cv.threshold(gray,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
kernel = np.ones((5,5),dtype= np.uint8)
newigbr = cv.erode(img,kernel,iterations=1)
dilate = cv.dilate(img,kernel,iterations=1)
# cv.imshow("anh",igbr)
# cv.imshow("dilate",dilate)
# cv.imshow("erode",newigbr)
# cv.waitKey()
fig,ax = plt.subplots(2,2)
ax[0,0].imshow(img),plt.xticks([]),plt.yticks([])
ax[1,0].imshow(newigbr),plt.xticks([]),plt.yticks([])
ax[0,1].imshow(dilate),plt.xticks([]),plt.yticks([])
plt.show()
# plt.subplot(222),plt.imshow(igbr[:,:,::-1]),plt.xticks([]),plt.yticks([])
cv.destroyAllWindows()

