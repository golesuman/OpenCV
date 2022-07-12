import cv2 
import numpy as np

def Resize(image,newx, newy):
    resized = cv2.resize(image, (newx, newy), interpolation = cv2.INTER_AREA)
    return resized 