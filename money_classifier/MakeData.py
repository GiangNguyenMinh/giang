import cv2 as cv
import numpy as np
import os
import sys

# ['0000', '1000', '5000', '20000', '50000']
lable = '0000'
link = './data/'
if not os.path.exists(link):
    os.mkdir(link)
if not os.path.exists(os.path.join(link, lable)):
    os.mkdir(os.path.join(link, lable))

cap = cv.VideoCapture(0)
i = 1
while 1:
    i += 1
    ret, frame = cap.read()
    if not ret:
        break
    cv.imshow('window', frame)

    if i > 60 and i <= 1060:
        print('cap count:', i-60)
        frame = cv.resize(frame, dsize=(224, 224))
        cv.imwrite(os.path.join(link, lable, '{}.png'.format(i-60)), frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
