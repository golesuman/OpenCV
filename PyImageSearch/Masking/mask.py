import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to iamge")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
mask = np.zeros(image.shape[:2], dtype = 'uint8')
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask", mask)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imwrite("maskedImage.jpg", masked)
cv2.imshow("Mask applied Image", masked)
cv2.waitKey(0)