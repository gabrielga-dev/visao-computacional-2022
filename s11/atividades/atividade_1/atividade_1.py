import cv2 as cv
import numpy as np


def segmentacao_por_movimento(img_1, img_2):
    imgRGB = cv.subtract(img_2, img_1)
    imgHSV = cv.cvtColor(imgRGB, cv.COLOR_BGR2HSV)
    tomClaro = np.array([0, 120, 120])
    tomEscuro = np.array([180, 255, 255])
    imgSegmentada = cv.inRange(imgHSV, tomClaro, tomEscuro)
    return imgSegmentada


def main():
    imagens = list()
    for i in range(1, 11):
        imagens.append(cv.imread('./imagens/img_' + str(i) + '.png'))

    imagens_segmentadas = list()

    for img in imagens:
        imagens_segmentadas.append(
            segmentacao_por_movimento(imagens[0], img)
        )

    index = 0
    incremento = 1
    while True:
        cv.imshow("Segmentacao por movimento", imagens_segmentadas[index])
        index += incremento
        if (index == (len(imagens_segmentadas))) or (index == -1):
            incremento *= -1
            if index == (len(imagens_segmentadas)):
                index -= 1
            else:
                index += 1

        # se o usuario digitar a tecla q ou esc, fecha o loop
        if cv.waitKey(30) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()
