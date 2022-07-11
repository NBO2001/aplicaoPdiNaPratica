import cv2
import numpy as np

#img = cv2.imread("./output/Image_Filtered_HP.png",0)

img = cv2.imread("./imgs/img5.jpeg",0)

kernel =np.ones((5,5), np.uint8)

#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

ero = cv2.erode(img,kernel,iterations=1)

cv2.imshow('dilata', ero)
cv2.imshow('sem dilata', img)

cv2.waitKey(0)
cv2.destroyAllWindows()