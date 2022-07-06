import cv2

# pega a imagem
img = cv2.imread('imagem.jpg')
cv2.imshow("imagem original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# separa a imagem pelos canais RGB
blue_channel, green_channel, red_channel = cv2.split(img)
cv2.imshow("canal azul", blue_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("canal verde", green_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("canal vermelho", red_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

# equaliza todos
equ_blue_channel = cv2.equalizeHist(blue_channel)
cv2.imshow("canal azul equalizado", equ_blue_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

equ_green_channel = cv2.equalizeHist(green_channel)
cv2.imshow("canal verde equalizado", equ_green_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

equ_red_channel = cv2.equalizeHist(red_channel)
cv2.imshow("canal vermelho equalizado", equ_red_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagem_final = cv2.merge((equ_blue_channel, equ_green_channel, equ_red_channel))
cv2.imshow("imagem equalizada", imagem_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
