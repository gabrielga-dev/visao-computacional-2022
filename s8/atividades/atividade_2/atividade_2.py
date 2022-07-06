from builtins import range
import cv2 as cv

img = cv.imread('img.jpg')

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

m = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
#pega o numero de linhas e colunas
qtdLinhas = len(img)
qtdColunas = len(img[0])
print(qtdLinhas,qtdColunas)

#percorre toda a imagem
for l in range(qtdLinhas):
    for c in range(qtdColunas):
        #se não for a primeira coluna ou linha de pixels nem as ultimas, faça(por causa da convolução pixel a pixel)
        if(l>=1 and l<=qtdLinhas-2 and c>=1 and c<=qtdColunas-2):
            lm= 0
            soma = 0.0
            for lf in range(l-1,l+2):
                cm = 0
                for cf in range(c - 1, c + 2):
                    soma += float(img[lf][cf] * m[lm][cm])
                    cm+=1
                lm+=1
            img[l][c] = float(soma/16)

cv.imshow("Gaus", img)
cv.waitKey(0)