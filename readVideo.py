import cv2
vid=cv2.VideoCapture("Resources/Aven.mp4")
while True:
    success,img= vid.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break