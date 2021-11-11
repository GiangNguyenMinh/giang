import cv2 as cv
import numpy

img = cv.imread("nier.jpg",cv.IMREAD_COLOR) #dinh dang mau truc tiep
img1 = cv.imread("nier1.jpg",cv.IMREAD_COLOR)
# img  = cv.cvtColor(img,cv.COLOR_BGR2GRAY) chuyen thanh dinh dang may toi
# img2 = img[100:200,100:200] // tạo ảnh từ vị trí dã chọn
# cv.imshow('nier',img2)



cv.namedWindow("nier",cv.WINDOW_NORMAL)
cv.namedWindow("nier1",cv.WINDOW_NORMAL)


cv.imshow("nier",img)
cv.imshow("nier1",img1)
cv.waitKey()
print("chieu dai la %d" %img.shape[0])
print("chieu rong la %d " %img.shape[1])
print(img.size)
print("chieu dai 1 la %d" %img1.shape[0])
print("chieu rong 1 la %d " %img1.shape[1])
print(img1.size)
cv.destroyAllWindows()



