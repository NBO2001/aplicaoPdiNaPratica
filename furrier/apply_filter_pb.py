import numpy as np
import cv2
from matplotlib import pyplot as plt


def createFilter(shape,center,radius,lpType = 2, n=2):
    
    rows, colluns = shape[:2]

    r,c = np.mgrid[0:rows:1, 0:colluns:1]

    c -= center[0]
    r -= center[1]

    d = np.power(c,2.0) + np.power(r, 2.0)

    lpFilter = np.exp(-d/(2*pow(radius,2.0)))

    return lpFilter 


box_img = cv2.imread("./imgs/img7.png",0)

rows, colls = box_img.shape[:2]
x,y = int(colls/2), int(rows/2)

filter = createFilter(box_img.shape,(x,y),10,2)

img_float32 = np.float32(box_img)

img_dft = cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)

img_dft_shift = np.fft.fftshift(img_dft)

img_complex = img_dft_shift[:,:,0]*1j + img_dft_shift[:,:,1]

img_filtered = filter * img_complex

invert_furrier = np.fft.ifft2(img_filtered)

img_f = np.abs(invert_furrier)
img_f -= img_f.min()
img_f = img_f*255/ img_f.max()
img_f = img_f.astype(np.uint8)

cv2.imwrite("./output/Imagem_Original.png", box_img)
cv2.imwrite("./output/Filtro.png", filter)
cv2.imwrite("./output/Image_Filtered.png", img_f)



