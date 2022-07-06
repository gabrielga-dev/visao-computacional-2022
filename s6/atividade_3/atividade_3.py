import cv2 as cv
import numpy as np


def binarizar(img, limiar):
    for row in range(len(img)):
        for col in range(len(img[0])):
            if img[row][col] <= limiar:
                img[row][col] = 0
            else:
                img[row][col] = 255
    return img


def main():
    limiar = 150
    img_1 = cv.imread('imagem_1.jpg')
    img_1 = binarizar(cv.cvtColor(img_1, cv.COLOR_BGR2GRAY), limiar)
    img_2 = cv.imread('imagem_2.jpg')
    img_2 = binarizar(cv.cvtColor(img_2, cv.COLOR_BGR2GRAY), limiar)

    result = (img_1 / 255) - (img_2 / 255)

    cv.imshow('resultado', result)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
