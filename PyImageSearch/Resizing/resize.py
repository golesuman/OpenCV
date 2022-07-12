import numpy as np
import cv2
import argparse

# from pyparsing import original_text_for
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

original_image = cv2.imread(args['image'])
cv2.imshow("Original", original_image)
resized = imutils.Resize(original_image, 100, 100)
cv2.imshow("resized", resized)
cv2.waitKey(0)