import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagem.jpg')
# cv2.imshow("original", img)
# cv2.waitKey(0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Cinza", img)
# cv2.waitKey(0)

equ = cv2.equalizeHist(img)
cv2.imshow("Equalizada", equ)
cv2.waitKey(0)


#coloca imagem uma do lado da outra
#res = np.hstack((img,equ))
#cv2.imshow("2 imagens", res)
#cv2.waitKey(0)

#formata imagem
#equ = equ[dx: ds - dx, dx: ds - dx]
#equ = cv2.resize(equ, (224, 224))

#pega histograma
hist, sem_uso = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')

plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

