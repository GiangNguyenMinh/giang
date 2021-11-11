import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("anh_nhieu.jpg",1)
kernel = cv.getGaussianKernel(9,4,ktype=None)
dst = cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img[:,:,::-1]),plt.title("anhgoc"),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst[:,:,::-1]),plt.title("gaussianFilter"),plt.xticks([]),plt.yticks([])
plt.show()
cv.destroyAllWindows()