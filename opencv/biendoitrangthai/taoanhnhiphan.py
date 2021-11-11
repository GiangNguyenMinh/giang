import cv2 as cv



img = cv.imread("anh.png",1)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
thresh , frame = cv.threshold(gray,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imshow("gray",frame)
print(thresh)
cv.imwrite("anhnhiphan.jpg",frame)