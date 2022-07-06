import cv2 as cv


def atividade():
    img_1 = cv.imread('img_1.jpg')
    img_1 = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)
    img_2 = cv.imread('img_2.jpg', cv.COLOR_BGR2GRAY)
    img_2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)

    cv.imshow('img_1', img_1)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imshow('img_2', img_2)
    cv.waitKey(0)
    cv.destroyAllWindows()

    result = img_1 + img_2

    for row in range(len(result)):
        for col in range(len(result[0])):
            if result[row][col] > 255:
                result[row][col] = 255

    cv.imshow('result_1', result)
    cv.waitKey(0)
    cv.destroyAllWindows()

    for row in range(len(result)):
        for col in range(len(result[0])):
            result[row][col] = result[row][col] / 2

    cv.imshow('result_2', result)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    atividade()
