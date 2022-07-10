from __future__ import print_function
from ast import arg
from urllib.robotparser import RequestRate
import cv2
import argparse

from numpy import var

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
(b,g,r) = image[0,0]
print(f"Pixel at (0,0) - Red: {r}, Green: {g}, Blue : {b}")
image[0,0] = (0,0,255)
print(f"Pixel at (0,0) - Red: {r}, Green: {g}, and Blue: {b}")
cv2.imshow("original", image)
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)
image[0:100, 0:100] = (0,255, 0)
cv2.imshow("updated", image)
cv2.imwrite("updatedimage.jpg",image)
cv2.waitKey(0)
