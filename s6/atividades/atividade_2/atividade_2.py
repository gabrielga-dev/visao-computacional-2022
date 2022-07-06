import cv2 as cv


def main():
    img_1 = cv.imread('imagem_1.jpg')
    img_1 = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)

    img_2 = cv.imread('imagem_2.jpg')
    img_2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)

    result = img_1 + img_2
    for row in range(len(result)):
        for col in range(len(result[0])):
            if result[row, col] > 255:
                result[row, col] = 255
            result[row, col] = result[row, col] / 2

    cv.imshow('resultado', result)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
