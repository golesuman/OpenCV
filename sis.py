import cv2
img=cv2.VideoCapture(0)
while True:
    succes,vid=img.read();
    cv2.imshow('Sum',vid)
    if cv2.waitKey(3) & 0xFF==ord('1'):
        break