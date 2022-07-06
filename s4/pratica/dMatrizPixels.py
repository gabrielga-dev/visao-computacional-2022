"""

from PIL import Image, ImageFilter

#Read image
im = Image.open( '../ifmg.jpg' )
#Display image
im.show()

#pega tamanho da imagem
imageW = im.size[0]
imageH = im.size[1]

print(imageH, imageW)

"""
import cv2
print (cv2.__version__)
#capturando a imagem de um arquivo
img = cv2.imread('imagem.jpg')
#converto a imagem matricial para escala em cinza
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #pego a quantidade de linhas e colunas
qtdLinhas = len(img)
qtdColunas = len(img[0])
print(qtdLinhas,qtdColunas)
#imprimo todos os valores dos pixels
for l in range(qtdLinhas):
    for c in range(qtdColunas):
        print(img[l][c])

