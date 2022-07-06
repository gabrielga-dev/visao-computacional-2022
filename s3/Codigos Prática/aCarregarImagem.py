# -*- coding:utf-8 -*-

#importa a biblioteca
import	cv2

#carrega a imagem em uma variável
imagem	=	cv2.imread("imagem.png")

#mostra a imagem em uma janela
cv2.imshow("Imagem",	imagem)

#aguarda um tecla a ser pressionada
cv2.waitKey(0)

#fecha a janela
cv2.destroyAllWindows()