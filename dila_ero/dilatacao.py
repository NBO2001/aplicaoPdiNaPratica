import cv2
import numpy as np

img = cv2.imread("./imgs/img5.jpeg",0)

kernel =np.ones((3,3), np.uint8)

#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

dilata = cv2.dilate(img,kernel,iterations=1)

cv2.imshow('dilata', dilata)
cv2.imshow('sem dilata', img)

cv2.waitKey(0)
cv2.destroyAllWindows()