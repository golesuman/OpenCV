from cv2 import bitwise_and
import numpy as np
import cv2
import argparse
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)
circle = np.zeros((300, 300), dtype="uint8")

cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("circle", circle)
# cv2.waitKey(0)


bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwise_and)
cv2.imwrite("BitwiseAnd.jpg", bitwise_and)
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imwrite("BitwiseXor.jpg", bitwiseXor)

cv2.imshow("xor", bitwiseXor)
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imwrite("BitwiseOr.jpg", bitwiseOr)

cv2.imshow("OR", bitwiseOr)

cv2.waitKey(0)