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
    img = cv.imread('img_1.jpg')
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = binariza(img)

    img = img / 255

    for row in range(len(img)):
        for col in range(len(img[0])):
            if img[row][col] == 1:
                img[row][col] = 0
            else:
                img[row][col] = 255

    cv.imshow('result', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    atividade()
