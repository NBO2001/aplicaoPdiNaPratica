from sys import flags
import numpy as np
import cv2
from matplotlib import pyplot as plt

fist_box = cv2.imread("./imgs/img6.jpeg", 0)

# Chance image for real numbers

float_32 = np.float32(fist_box)

# Calcula o coefiente dos values e faz o shirt

img_diff = cv2.dft(float_32, flags=cv2.DFT_COMPLEX_OUTPUT)

im_diff_shirt = np.fft.fftshift(img_diff)

# Cria imagem com os coeficientes de furrier na base 20log
magnitude_spc = 20*np.log(cv2.magnitude(im_diff_shirt[:,:,0], im_diff_shirt[:,:,1]))

plt.subplot(121),plt.imshow(fist_box,cmap = 'gray')

plt.title('Image imput'), plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(magnitude_spc, cmap='gray')

plt.title('Image output'), plt.xticks([]), plt.yticks([])

plt.savefig("./output/transf_freq.png")