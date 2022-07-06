import cv2
import numpy as np


def main():
    # carrega a imagem RGB
    imgRGB = cv2.imread("cubo.png")
    # converte em HSV
    imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)
    # determina intervalos de cores da matiz 160 a 200,
    # de brilho 100 a 255 e saturação de 100 a 255
    tomClaro = np.array([160, 100, 100])
    tomEscuro = np.array([200, 255, 255])
    # segmenta(binarizando) o inervalo de cores
    imgSegmentada = cv2.inRange(imgHSV, tomClaro, tomEscuro)
    cv2.imshow("Original", imgRGB)
    cv2.imshow("Segmentada", imgSegmentada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
