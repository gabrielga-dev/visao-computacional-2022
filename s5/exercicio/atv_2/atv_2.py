import cv2 as cv
from matplotlib import pyplot as plt

original = cv.imread('imagem.png')

img = cv.cvtColor(original, cv.COLOR_BGR2GRAY)


for row in range(len(img)):
    for col in range(len(img[0])):
        if img[row][col] < 160:
            img[row][col] = 0

cv.imshow('imagem', img)
cv.waitKey(0)
cv.destroyAllWindows()
