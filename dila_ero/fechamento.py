import cv2
import numpy as np

img = cv2.imread("./imgs/img6.jpeg",0)

(thresh, blackAndWhiteImage) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

wid, hei = blackAndWhiteImage.shape

for i in range(wid):
    for j in range(hei):
        blackAndWhiteImage[i][j] = 255 if blackAndWhiteImage[i][j] == 0 else 0

cv2.imwrite('./output/wb.png', blackAndWhiteImage)



#kernel =np.ones((10,10), np.uint8)

#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

#abetrua = cv2.morphologyEx(blackAndWhiteImage, cv2.MORPH_CLOSE,kernel)

#cv2.imwrite('./output/fechad.png', abetrua)