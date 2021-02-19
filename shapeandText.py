import cv2 as cv
import numpy as np
img=np.zeros((500,500,3),np.uint8)
cv.line(img,(0,0),(500,500),(0,0,555),2)
cv.imshow('Empty',img)
cv.waitKey(0)