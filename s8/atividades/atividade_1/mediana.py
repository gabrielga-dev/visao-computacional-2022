"""
pega a mediana da visinhança
"""
from builtins import range

import cv2


#desvioPadrao = sts.stdev(mascaraGaus)
#for i in range(7):
#    mascaraGaus[i] = 1-(1/(desvioPadrao*math.sqrt(2*math.pi))) * math.exp((-1 * mascaraGaus[i]**2) / (2 * desvioPadrao**2))
#print (mascaraGaus)

#pega imagem convertendo para escala em cinza
original = cv2.imread('mediana.png')
resultante = cv2.imread('mediana.png')
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
resultante = cv2.cvtColor(resultante, cv2.COLOR_BGR2GRAY)

#Mostra a imagem antes do filtro
cv2.imshow("Cinza", original)
cv2.waitKey(0)

m = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

#pega o numero de linhas e colunas
qtdLinhas = len(original)
qtdColunas = len(original[0])
print(qtdLinhas,qtdColunas)


#percorre toda a imagem
for l in range(qtdLinhas):

    for c in range(qtdColunas):

        #se não for a primeira coluna ou linha de pixels nem as ultimas, faça(por causa da convolução pixel a pixel)
        if(l>=2 and l<=qtdLinhas-4 and c>=2 and c<=qtdColunas-4):
            lista = []  

            #primeira linha
            lista.append(float(original[l - 1][c - 1]) * m[0][0])
            lista.append(float(original[l - 1][c]) * m[0][1])
            lista.append(float(original[l - 1][c + 1]) * m[0][2])
            lista.append(float(original[l - 1][c + 2]) * m[0][3])
            lista.append(float(original[l - 1][c + 3]) * m[0][4])

            #segunda linha
            lista.append(float(original[l][c - 1]) * m[1][0])
            lista.append(float(original[l][c]) * m[1][1])
            lista.append(float(original[l][c + 1]) * m[1][2])
            lista.append(float(original[l][c + 2]) * m[1][3])
            lista.append(float(original[l][c + 3]) * m[1][4])

            #terceira linha
            lista.append(float(original[l + 1][c - 1]) * m[2][0])
            lista.append(float(original[l + 1][c]) * m[2][1])
            lista.append(float(original[l + 1][c + 1]) * m[2][2])
            lista.append(float(original[l + 1][c + 2]) * m[2][3])
            lista.append(float(original[l + 1][c + 3]) * m[2][4])

            #quarta linha
            lista.append(float(original[l + 2][c - 1]) * m[3][0])
            lista.append(float(original[l + 2][c]) * m[3][1])
            lista.append(float(original[l + 2][c + 1]) * m[3][2])
            lista.append(float(original[l + 2][c + 2]) * m[3][3])
            lista.append(float(original[l + 2][c + 3]) * m[3][4])

            #quinta linha
            lista.append(float(original[l + 3][c - 1]) * m[4][0])
            lista.append(float(original[l + 3][c]) * m[4][1])
            lista.append(float(original[l + 3][c + 1]) * m[4][2])
            lista.append(float(original[l + 3][c + 2]) * m[4][3])
            lista.append(float(original[l + 3][c + 3]) * m[4][4])

            #ordena
            lista.sort()

            #pega a mediana
            resultante[l][c] = lista[12]


#img = cv2.medianBlur(img,9,dst=None)

cv2.imshow("Mediana", resultante)
cv2.waitKey(0)