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
fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0 , 256])
p = ax.imshow(hist, interpolation = 'nearest')
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar()
ax = fig.add_subpot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = 'nearest')
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)
print(f"2D histogram shape : {hist.shape} with values {hist.flatten().shape[0]}")
cv2.waitKey(0)