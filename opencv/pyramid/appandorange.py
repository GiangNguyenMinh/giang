import cv2 as cv
import numpy as np
ap = cv.imread("app.jpg",1)
og = cv.imread("orange.jpg",1)
G = ap.copy()

#pyramids Gaussian ap 6 lan
GA = [G]

for i in range(6):
    G = cv.pyrDown(G)
    GA.append(G)
print(GA)
# pyramids Gaussian orange 6 lan
G = og.copy()
GB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    GB.append(G)



LA = [GA[5]]
for i in range(4,0,-1):
    la = cv.pyrUp(GA[i])
    print(la.shape)
    # lsa = cv.subtract(GA[i-1],la)
    # LA.append(lsa)

LB =[GB[5]]
for m in range(5,0,-1):
    lb = cv.pyrUp(GB[i])
    # lsb = cv.subtract(GB[i-1],lb)
    # LB.append(lsb)

LS =[]
for la , lb in zip(LA,LB):
    row, col , deept = la.shape
    ls = np.hstack((la[:,0:col//2],lb[:,col//2:]))
    LS.append(ls)




ls_ = LS[0]
cv.namedWindow("img",cv.WINDOW_NORMAL)
cv.imshow("img",ls_)
cv.waitKey()
cv.destroyAllWindows()
