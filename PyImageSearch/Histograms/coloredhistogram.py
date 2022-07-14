from __future__ import print_function
import cv2 
import numpy as np
import argparse
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("Flattened Colroed Histogram")
plt.xlabel("Bins")
plt.ylabe("# of Pixels")
for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)