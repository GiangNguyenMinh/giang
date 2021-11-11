import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread("anh1.jpg",1)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i,j,:] = [255-img[i,j,0],255-img[i,j,1],255-img[i,j,2]]
C = img[:,:,2]
M = img[:,:,1]
Y = img[:,:,0]
CMY = cv.merge((Y,M,C))
K = np.min(CMY,axis=2)
Ck = C
Mk = M
Yk = Y
print(C)
for k in range(img.shape[0]):
    for m in range(img.shape[1]):
        # if(K[i,j] == 0 ):
        #     Ck[i,j] =  0
        #     Mk[i, j] = 0
        #     Yk[i, j] = 0
        # else:
        #     Ck[i, j] = (C[i, j] - K[i, j]) / (255 - K[i, j])
        #

        try:
            Ck[i,j] = (C[i,j] - K[i,j])/(255-K[i,j])
        except RuntimeWarning:
            Ck[i,j] = 0
            Mk [i,j] =0
            Yk[i, j] = 0
        try:
            Mk[i,j] = (M[i,j] - K[i,j])/(255-K[i,j])
        except RuntimeWarning:
            Mk[i,j] = 0
            Ck[i, j] = 0
            Yk[i, j] = 0
        try:
            Yk[i,j] = (Y[i,j] - K[i,j])/(255-K[i,j])

        except RuntimeWarning:
            Yk[i, j] = 0
            Ck[i, j] = 0
            Mk[i, j] = 0

# Ck = (C-K)/(np.full((img.shape[0],img.shape[1]),7,dtype=np.uint8)-K)
# Mk = (M-K)/(np.full((img.shape[0],img.shape[1]),7,dtype=np.uint8)-K)
# Yk = (Y-K)/(np.full((img.shape[0],img.shape[1]),7,dtype=np.uint8)-K)
#
CMYK = np.dstack((Ck,Mk,Yk,K))
cv.imshow("CMYK",CMYK)
cv.waitKey()