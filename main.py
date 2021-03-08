import cv2 as cv
vid=cv.VideoCapture(0)
forcc=cv.VideoWriter_fourcc('X','V','I','D')
out=cv.VideoWriter("suman.mp4",forcc,30.0,(640,480))

while(vid.isOpened()):
    ret,frame=vid.read()
    if ret ==True:
        print(vid.get(cv.CAP_PROP_FRAME_WIDTH))
        print(vid.get(cv.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow("frame",gray)
        if cv.waitKey(1)& 0xFF==ord("q"):
            break
    else:
        break
vid.release()
out.release()
cv.destroyAllWindows()