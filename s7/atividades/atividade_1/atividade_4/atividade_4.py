from builtins import range
import cv2 as cv


def binariza(img, limiar=127):
    for row in range(len(img)):
        for col in range(len(img[0])):
            if img[row][col] < limiar:
                img[row][col] = 0
            else:
                img[row][col] = 255
    return img


def atividade():
    img_1 = cv.imread('img_1.png')
    img_1 = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)
    img_1 = binariza(img_1)

    img_2 = cv.imread('img_2.png')
    img_2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)
    img_2 = binariza(img_2)

    img_1 = img_1 / 255
    img_2 = img_2 / 255

    for row in range(len(img_1)):
        for col in range(len(img_1[0])):
            if img_1[row][col] != img_2[row][col]:
                img_2[row][col] = 0
            else:
                img_2[row][col] = 255

    cv.imshow('result', img_2)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    atividade()
