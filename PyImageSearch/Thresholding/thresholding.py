import cv2
from matplotlib.pyplot import imshow
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("image", image)
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imwrite("Threshold.jpg", thresh)
cv2.imshow("Threshold Binary", thresh)
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite("InvertedThreshold.jpg", threshInv)
cv2.imshow("Threshold inverted", threshInv)
cv2.waitKey(0)
