import numpy as np
import cv2
import argparse

from requests import request
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "path to the image")
arg = vars(ap.parse_args())

original = cv2.imread(arg["image"])
cv2.imshow("original", original)
flipped = imutils.Flipping(original, 1) # flipped horizontally
cv2.imshow("flipped horizontal",flipped)
flipped_vertically = imutils.Flipping(original, 0) #vertically
cv2.imwrite("flipped_vertically.jpg", flipped_vertically)
cv2.imshow("Vertically flipped", flipped_vertically)
flipped_both = imutils.Flipping(original, -1)
cv2.imshow("flipped both", flipped_both)
cv2.waitKey(0)