# hello VC
import cv2

captura	= cv2.VideoCapture("video.mp4")

#enquanto houver video carrega frame a frame na janela
while True:
    ret,	frame	=	captura.read()
    cv2.imshow("pressione Q para sair!",	frame)
    #se o usuario digitar a tecla 1 ou esc, fecha o loop
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
captura.release()
cv2.destroyAllWindows()


captura = cv2.VideoCapture(0)

while (True):
    ret, frame = captura.read()
    cv2.imshow("Imagem", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
captura.release()
cv2.destroyAllWindows()
