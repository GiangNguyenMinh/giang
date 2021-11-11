import cv2 as cv

vd = cv.VideoCapture("CADSV.mp4")

while True:
    ret , frame = vd.read()
    if ret == False :
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.namedWindow("MTP",cv.WINDOW_NORMAL)
    cv.imshow("MTP",gray)
    if cv.waitKey() & 0xFF == ord("s"):
        break
vd.release()
cv.destroyAllWindows()