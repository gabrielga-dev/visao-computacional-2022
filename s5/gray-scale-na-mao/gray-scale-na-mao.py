from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread('image.png')

R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B

plt.imshow(imgGray, cmap='gray')
plt.show()

# tentei utilizar o vc2 juntamente com o que esse site propos, mas nao deu certo
# assim utilizei o matplotlib mesmo
# https://www.delftstack.com/pt/howto/python/convert-image-to-grayscale-python/
