import cv2 as cv
from matplotlib import pyplot as plt

imagem = cv.imread('imagem.png')

imagem_gray_scale = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
plt.show()

qtd_linhas = len(imagem_gray_scale)
qtd_colunas = len(imagem_gray_scale[0])

for linha in range(qtd_linhas):
    for coluna in range(qtd_colunas):
        if imagem_gray_scale[linha][coluna] < 225:
            imagem_gray_scale[linha][coluna] = 0
        else:
            imagem_gray_scale[linha][coluna] = 255

cv.imshow('escala em cinza', imagem_gray_scale)
cv.waitKey(0)
cv.destroyAllWindows()
