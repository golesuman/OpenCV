import cv2
import numpy as np
import argparse
import imutils


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
cv2.imshow("Original",image)
shifted = imutils.translate(image, 0, 100)
# shifted = cv2.warpAffine(image, M , (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down", shifted)
# cv2.imwrite("shiftedimage.jpg",shifted )
cv2.waitKey(0)