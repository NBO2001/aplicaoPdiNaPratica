import cv2
import numpy as np

img = cv2.imread('./output/Image_Filtered_HP.png',0)

(thresh, blackAndWhiteImage) = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)

wid, hei = img.shape

kernel =np.ones((3,3), np.uint8)
dilata = cv2.dilate(blackAndWhiteImage,kernel,iterations=1)


for i in range(wid):
    for j in range(hei):
        dilata[i][j] = 0 if dilata[i][j] == 255 else 255

kernel =np.ones((3,3), np.uint8)

wid, hei = img.shape

abertura = cv2.morphologyEx(blackAndWhiteImage, cv2.MORPH_OPEN,kernel)



cv2.imshow('entrada', img)
cv2.imshow('wb', blackAndWhiteImage)
cv2.imshow('Abertura', dilata)
cv2.waitKey(0)
cv2.destroyAllWindows()