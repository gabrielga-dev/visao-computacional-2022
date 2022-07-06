import cv2 as cv
import  numpy as np


def normalize_value(value):
    if (value is None) or value < 0:
        return 0
    elif value > 255:
        return 255
    else:
        return value


def jogo_7_erros(metodo=1):
    if metodo == 1:
        img1 = cv.imread('./jogo_7_erros/11.jpg')
        img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

        img2 = cv.imread('./jogo_7_erros/11.jpg')
        img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        for row in range(len(img1)):
            for col in range(len(img1[0])):
                if img1[row][col] == img2[row][col]:
                    img1[row][col] = 255
                else:
                    img1[row][col] = 0
        cv.imshow('results', img1)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        img1 = cv.imread('./jogo_7_erros/image_1.jpeg')
        img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

        img2 = cv.imread('./jogo_7_erros/image_2.jpeg')
        img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        img1 = np.subtract(img2, img1)

        for row in range(len(img1)):
            for col in range(len(img1[0])):
                if img1[row][col] == 0:
                    img1[row][col] = 255
                else:
                    img1[row][col] = 0

        cv.imshow('results', img1)
        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == '__main__':
    jogo_7_erros(metodo=1)
