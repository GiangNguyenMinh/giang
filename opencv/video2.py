import cv2 as cv

vd = cv.VideoCapture("CADSV.mp4")
hight = int(vd.get(4))
width = int(vd.get(3))


# ma fourCC
fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter("MTP.mp4",fourcc,20,(width,hight))
while vd.isOpened() :
    ret , frame = vd.read()
    if ret == True :
        # frame = cv.flip(frame,0)
        out.write(frame)
        cv.imshow("sontung",frame)
        if cv.waitKey() & 0xFF == ord("s"):
            break
    else :
        break
vd.release()
out.release()
cv.destroyAllWindows()
