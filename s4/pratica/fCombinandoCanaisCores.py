import	cv2
imagem	=	cv2.imread("imagem.jpg")
azul,	verde,	vermelho	=	cv2.split(imagem)
#	Combinando	os	três	canais	em	uma	única	imagem
# imagem	=	cv2.merge((azul,	verde,	vermelho))
# imagem	=	cv2.merge((verde,	verde,	vermelho))
imagem	=	cv2.merge((vermelho, azul,	verde))
cv2.imshow("Imagem",	imagem)
cv2.waitKey(0)
#cv2.destroyAllWindows()
