import cv2 as cv
import numpy as np


def main():
    img_1 = cv.imread('imagem_1.jpg')
    img_1 = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)

    img_2 = cv.imread('imagem_2.jpg')
    img_2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)

    result = np.subtract(img_2, img_1)
    for row in range(len(result)):
        for col in range(len(result[0])):
            result[row, col] = result[row, col] * 2

    cv.imshow('resultado', result)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
