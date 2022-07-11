import cv2
import numpy as np

img = cv2.imread("./output/wb.png",0)

kernel =np.ones((25,25), np.uint8)

wid, hei = img.shape

abertura = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel)

for i in range(wid):
    for j in range(hei):
        img[i][j] = 0 if abertura[i][j] == 255 else img[i][j]


for i in range(wid):
    for j in range(hei):
        img[i][j] = 255 if img[i][j] == 0 else 0


kernel =np.ones((4,4), np.uint8)
dilata = cv2.dilate(img,kernel,iterations=1)

kernel =np.ones((5,5), np.uint8)
ero = cv2.erode(dilata,kernel,iterations=1)

cv2.imwrite('./output/Erode.png', ero)



#kernel =np.ones((5,5), np.uint8)
#abertura2 = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel)


#img2 = cv2.imread("./output/wb.png",0)
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

#img = cv2.imread("./imgs/img5.jpeg",-1)

# cv2.imshow('Aberta', abetrua)
# cv2.imshow('Dilatta', dilata)
# 
# cv2.imshow('Filte', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()