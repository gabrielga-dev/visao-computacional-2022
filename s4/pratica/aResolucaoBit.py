#importa a biblioteca
import	cv2

#carrega a imagem em uma variável
imagem	=	cv2.imread("imagem.jpg")

#transformando de BGR para cinza
cinza8 = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

print("Aguarde... processando")
cinza3 = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
#percorrendo linhas e colunas da imagem
qtdLinhas = len(cinza8)
qtdColunas = len(cinza8[0])

#peguei mais ou menos as médias de intervalo pra fazer a nova imagem descrita com menos bits
for l in range(qtdLinhas):
    for c in range(qtdColunas):
        # if(cinza8[l][c]<=37):
        #     cinza3[l][c] = 18
        # if (cinza8[l][c] > 37 and cinza8[l][c] <= 74):
        #     cinza3[l][c] = 55
        # if (cinza8[l][c] > 74 and cinza8[l][c] <= 111):
        #     cinza3[l][c] = 90
        # if (cinza8[l][c] > 111 and cinza8[l][c] <= 148):
        #     cinza3[l][c] = 133
        # if (cinza8[l][c] > 148 and cinza8[l][c] <= 185):
        #     cinza3[l][c] = 66
        # if (cinza8[l][c] > 185 and cinza8[l][c] <= 222):
        #     cinza3[l][c] = 199
        # if (cinza8[l][c] > 222 and cinza8[l][c] <= 255):
        #     cinza3[l][c] = 238

        if(cinza8[l][c]<=87):
            cinza3[l][c] = 42
        if (cinza8[l][c] > 87 and cinza8[l][c] <= 170):
            cinza3[l][c] = 127
        if (cinza8[l][c] > 170 and cinza8[l][c] <= 255):
            cinza3[l][c] = 212

#mostra a imagem original
cv2.imshow("Imagem",	imagem)
#mostra a imagem cinza de 8 bits
cv2.imshow("cinza 8 bit",	cinza8)
#mostra a imagem cinza de 8 bits
cv2.imshow("cinza 3 bit",	cinza3)

#aguarda um tecla a ser pressionada
cv2.waitKey(0)

#fecha a janela
cv2.destroyAllWindows()