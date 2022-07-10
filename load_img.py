from __future__ import print_function
import cv2 as cv
import matplotlib.pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i" , "--image", required=True,
                help = "Path to the image")
args = vars(ap.parse_args())
image = cv.imread(args["image"])
print(f"width : {image.shape[1]}")
print(f"height: {image.shape[0]}")
print(f"Channels: {image.shape[2]}")

cv.imshow("Image", image)
cv.waitKey(0)
cv.imwrite("gole.jpg", image)