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
    captura = cv.VideoCapture(0)
    ref_inicial, frame_inicial = captura.read()

    img_1 = frame_inicial

    while True:
        ref, frame = captura.read()
        segmentacao = segmentacao_por_movimento(img_1, frame)

        cv.imshow("Segmentacao por movimento", segmentacao)

        # se o usuario digitar a tecla q ou esc, fecha o loop
        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    captura.release()


if __name__ == "__main__":
    main()
