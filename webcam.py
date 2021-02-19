import cv2
cap=cv2.VideoCapture(0)
while True:
    success,vid=cap.read()
    cv2.imshow("videos",vid)
    if cv2.waitKey(2) & 0xFF==ord('s'):
        break