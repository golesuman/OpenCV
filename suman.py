import cv2
img=cv2.imread('Resources/Su.jpg')
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(img,(5,5),0)
# cv2.imshow('suman',imgGray)
cv2.imshow('Su',imgBlur)
cv2.waitKey(0)