import cv2 as cv
import numpy as np


def segmenta(imgHSV, tomClaro, tomEscuro):
    qtd_rows = len(imgHSV)
    qtd_cols = len(imgHSV[0])

    escuro_cor, escuro_brilho, escuro_saturacao = tomEscuro
    claro_cor, claro_brilho, claro_saturacao = tomClaro

    for row in range(qtd_rows):
        for col in range(qtd_cols):
            cor = imgHSV[row][col][2]
            brilho = imgHSV[row][col][1]
            saturacao = imgHSV[row][col][0]


            if (escuro_cor <= cor <= claro_cor) and \
                    (escuro_brilho <= brilho <= claro_brilho) and \
                    (escuro_saturacao <= saturacao <= claro_saturacao):
                imgHSV[row][col] = [255, 255, 255]
            else:
                imgHSV[row][col] = [0, 0, 0]
    return imgHSV


def main():
    # carrega a imagem RGB
    imgRGB = cv.imread("cubo.png")
    # converte em HSV
    imgHSV = cv.cvtColor(imgRGB, cv.COLOR_BGR2HSV)


    # cv.imshow("Original HSV", imgHSV)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # determina intervalos de cores da matiz 160 a 200,
    # de brilho 100 a 255 e saturação de 100 a 255
    tomEscuro = np.array([85,	100,	100])
    tomClaro = np.array([255,	255,	255])
    # segmenta(binarizando) o inervalo de cores
    imgSegmentada = segmenta(imgHSV, tomClaro, tomEscuro)
    cv.imshow("Original", imgRGB)
    cv.imshow("Original HSV", imgHSV)
    cv.imshow("Segmentada", imgSegmentada)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
