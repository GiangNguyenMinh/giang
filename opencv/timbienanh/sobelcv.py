import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("ronaldo.jpg",0)

sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
# plt.subplot(1,2,1),plt.imshow(sobelx,cmap="gray"),plt.xticks([]),plt.yticks([])
# plt.subplot(1,2,2),plt.imshow(sobely,cmap="gray"),plt.xticks([]),plt.yticks([])
# plt.show()
cv.imshow("x",sobelx)
cv.waitKey()
cv.destroyAllWindows()
plt.imshow(sobelx,cmap="gray")
plt.show()