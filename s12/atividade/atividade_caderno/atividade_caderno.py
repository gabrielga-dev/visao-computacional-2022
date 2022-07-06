import cv2 as cv


def main():
    # carrego imagem
    imgOriginal = cv.imread("palheta_1.png")
    # transformo em gray
    imgGray = img = cv.cvtColor(imgOriginal, cv.COLOR_BGR2GRAY)
    # aplico a binarização invertida
    metodo = cv.THRESH_BINARY_INV
    ret, imgBinarizada = cv.threshold(imgGray, 160, 255, metodo)
    # aplico o filtro da mediana para tirar os "respingos" pretos da área branca (grão)
    imgMascaraSegmentacao = cv.medianBlur(imgBinarizada, 9, dst=None)
    # pego contornos da área branca
    contours, hier = cv.findContours(imgMascaraSegmentacao, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # desenho os contornos(pegos na linha acima) baseado na mascara
    for cnt in contours:
        if cv.contourArea(cnt):
            cv.drawContours(imgOriginal, [cnt], 0, (255, 00, 0), 2)
    # imprimo as imagens
    cv.imshow("ImagemOriginal", imgOriginal)
    cv.imshow("ImagemBinarizada", imgBinarizada)
    cv.imshow("Mascara de Segmentacao", imgMascaraSegmentacao)
    cv.imshow("ImagemOriginal identificada", imgOriginal)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
