import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("anhgai.jpg",1)
dst = cv.boxFilter(img,ddepth=-1,ksize=(11,11),normalize=True)
plt.subplot(121),plt.imshow(img[:,:,::-1]),plt.title("anhgoc"),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst[:,:,::-1]),plt.title("boxFilter"),plt.xticks([]),plt.yticks([])
plt.show()
cv.destroyAllWindows()
