import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("anh1.jpg",0)
hist = cv.calcHist([img],[0],None,histSize= [256],ranges=[0,256])
plt.plot(hist,"gray")
plt.show()
cv.waitKey()
cv.destroyAllWindows()