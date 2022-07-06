import	cv2 as cv


def binariza(img):
    for row in range(len(img)):
        for col in range(len(img[0])):
                if img[row][col] > 90:
                    img[row][col] = 255
                else:
                    img[row][col] = 0
    return img


captura = cv.VideoCapture(2)
frames = []

quantidade = 2

for i in range(quantidade):
    vazio = input('aperte algo ' + str(i))
    ret, frame = captura.read()
    frames.append(
        binariza(
            cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        )
    )

soma = frames[0]

for frame in frames[0:]:
    soma = soma + frame


for row in range(len(soma)):
    for col in range(len(soma[0])):
        soma[row][col] /= quantidade

cv.imshow('result', soma)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('./teste.png', img=soma)


# while (True):
#     ret,	frame	=	captura.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     for row in range(len(frame)):
#         for col in range(len(frame[0])):
#
#     cv2.imshow("Imagem", frame)
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break
# captura.release()
# cv2.destroyAllWindows()