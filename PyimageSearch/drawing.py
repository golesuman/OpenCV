import numpy as np
import cv2
import matplotlib.pyplot as plt
canvas = np.zeros((300,300,3), dtype="uint8")
green = (0, 255, 0)
cv2.line(canvas, (0,0), (300, 300), green)
# cv2.imshow("canvas", canvas)
# cv2.waitKey(0)

red = (0, 0, 255)
# cv2.line(canvas, (300,0), (0, 300), red, 2)
# cv2.imshow('canvas', canvas)
# cv2.rectangle(canvas, (10,10), (60, 60),green)
# cv2.circle(canvas, (200, 200), radius= 100, color = red)
# cv2.imshow('canvas', canvas)
for i in range(0, 25):
    radius = np.random.randint(5, high = 25)
    color = np.random.randint(0, high = 256, size = (3, )).tolist()
    pt = np.random.randint(0, high = 300, size = (2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imwrite("canvas.jpg", canvas)
cv2.imshow("Canvas", canvas)

cv2.waitKey(0)