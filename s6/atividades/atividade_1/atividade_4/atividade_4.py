import cv2 as cv


def atividade():

    img_1 = cv.imread('./img_1.png')
    img_1 = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)
    img_2 = cv.imread('./img_2.png', cv.COLOR_BGR2GRAY)
    img_2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)

    result = cv.bitwise_and(img_1, img_2)

    cv.imshow('interseccao', result)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    atividade()
