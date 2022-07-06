import cv2
import numpy as np


def main():
    imagem = cv2.imread("cafe.png", 0)
    # binariza de forma invertida-------------------------------------
    metodo = cv2.THRESH_BINARY_INV
    ret, imgBinarizada = cv2.threshold(imagem, 135, 255, metodo)
    # filtro morfológico, tirando ruidos------------------------------
    e = np.ones((3, 3), np.uint8)
    imgTratada = cv2.morphologyEx(imgBinarizada, cv2.MORPH_CLOSE, e)
    # aplica a erosão para diminuir elementos-------------------
    imgTratada = cv2.erode(imgTratada, e, iterations=2)
    # aplica o filtro de Canny para obter contornos-------------
    imgSegmentada = cv2.Canny(imgTratada, 100, 200)
    # mostra tudo
    cv2.imshow("Binarizada", imgBinarizada)
    cv2.imshow("Tratada", imgTratada)
    cv2.imshow("Segmentada", imgSegmentada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
