import cv2
print("package imported")
img=cv2.imread("Resources/g.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0)