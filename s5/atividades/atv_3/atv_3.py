import cv2 as cv
from matplotlib import pyplot as plt

original = cv.imread('imagem.png')

img = cv.cvtColor(original, cv.COLOR_BGR2GRAY)

limiar_1 = 17
aceitacao_1 = 5

limiar_2 = 30
aceitacao_2 = 5

for row in range(len(img)):
    for col in range(len(img[0])):
        if ((limiar_1 - aceitacao_1) < img[row][col]) and (img[row][col] < (limiar_1 + aceitacao_1)):
            img[row][col] = 0
        elif ((limiar_2 - aceitacao_2) < img[row][col]) and (img[row][col] < (limiar_2 + aceitacao_2)):
            img[row][col] = 0

cv.imshow('imagem', img)
cv.waitKey(0)
cv.destroyAllWindows()
