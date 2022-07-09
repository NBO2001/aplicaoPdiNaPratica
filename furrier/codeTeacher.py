import numpy as np
import cv2
from matplotlib import pyplot as plt

def createLPFilter(shape, center, radius, lpType=2, n=2):

    rows, cols = shape[:2]
    r, c = np.mgrid[0:rows:1, 0:cols:1]
    c -= center[0]
    r -= center[1]
    d = np.power(c, 2.0) + np.power(r, 2.0)
    lpFilter = np.exp(-d/(2*pow(radius, 2.0)))

    return lpFilter

img = cv2.imread('./imgs/img7.png',0)

rows, cols = img.shape[:2]
x, y = int(cols/2), int(rows/2)              # Encontra posições centrais
filt = createLPFilter(img.shape, (x, y), 50, 2)        # Calcula o filtro

f = cv2.dft(img.astype(np.float32), flags=cv2.DFT_COMPLEX_OUTPUT)
f_shifted = np.fft.fftshift(f)
f_complex = f_shifted[:,:,0]*1j + f_shifted[:,:,1]

f_filtered = filt * f_complex
inv_img = np.fft.ifft2(f_filtered) # inverse F.T.

filtered_img = np.abs(inv_img)
filtered_img -= filtered_img.min()
filtered_img = filtered_img*255 / filtered_img.max()
filtered_img = filtered_img.astype(np.uint8)

cv2.namedWindow('Imagem original', cv2.WINDOW_NORMAL)
cv2.imshow("Imagem original", img)                # Mostra a imagem original

cv2.namedWindow('Imagem filtrada', cv2.WINDOW_NORMAL)
cv2.imshow("Imagem filtrada", filtered_img)        # Mostra a imagem filtrada

cv2.namedWindow('Imagem filter', cv2.WINDOW_NORMAL)
cv2.imshow("Imagem filter", filt)                # Mostra a imagem filtrada

cv2.waitKey(0)
cv2.destroyAllWindows()