import numpy as np
import cv2

def rotate(image, degree, size):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, degree, size)
    rotated = cv2.warpAffine(image, M , (w, h))
    return rotated
