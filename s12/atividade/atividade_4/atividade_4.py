import cv2 as cv


def main():
    # carrego imagem
    imgOriginal = cv.imread("cafe.png")
    # transformo em gray
    imgGray = img = cv.cvtColor(imgOriginal, cv.COLOR_BGR2GRAY)
    # aplico a binarização invertida
    metodo = cv.THRESH_BINARY_INV
    ret, imgBinarizada = cv.threshold(imgGray, 135, 255, metodo)
    # aplico o filtro da mediana para tirar os "respingos" pretos da área branca (grão)
    imgMascaraSegmentacao = cv.medianBlur(imgBinarizada, 9, dst=None)

    for row in range(len(imgOriginal)):
        for col in range(len(imgOriginal[0])):
            if imgMascaraSegmentacao[row][col] == 0:
                imgOriginal[row][col] = imgMascaraSegmentacao[row][col]

    cv.imshow('result', imgOriginal)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
