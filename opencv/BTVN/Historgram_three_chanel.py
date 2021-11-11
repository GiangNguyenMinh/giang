import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("anh1.jpg",1)
# b,g,r = cv.split(img)
blue = cv.calcHist([img],[0],None,[256],[0,256])
green = cv.calcHist([img],[1],None,[256],[0,256])
red = cv.calcHist([img],[2],None,[256],[0,256])
plt.plot(blue,"b")
plt.plot(green,"g")
plt.plot(red,"r")
plt.show()
