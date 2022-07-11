import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image) # showing the original image
rotated = imutils.rotate(image, 45, 2)
cv2.imshow("rotated",rotated)
cv2.waitKey(0)