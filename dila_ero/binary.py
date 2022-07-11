import cv2
import numpy as np

img = cv2.imread("./imgs/img5.jpeg",0)

	
(thresh, blackAndWhiteImage) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

	
cv2.imshow('Black white image', blackAndWhiteImage)

cv2.imshow('Original image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()