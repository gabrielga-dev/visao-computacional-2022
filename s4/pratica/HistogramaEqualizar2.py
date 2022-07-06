from matplotlib import pyplot as plt
import numpy as np
import cv2
imgOri = cv2.imread('satelite.png')
cv2.imshow("Imagem", imgOri)

img = cv2.cvtColor(imgOri, cv2.COLOR_BGR2GRAY)
cv2.imshow("/", img)
cv2.waitKey(0)

h_eq = cv2.equalizeHist(img)
cv2.imshow("/Equalizada", h_eq)
cv2.waitKey(0)

plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()


plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

#cv2.waitKey(0)


cv2.waitKey(0)
