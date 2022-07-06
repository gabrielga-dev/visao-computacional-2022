import cv2


def main():
    # carrego imagem já em gray
    imgOriginal = cv2.imread("cafe.png")
    imgGray = img = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)
    # aplico a binarização invertida
    metodo = cv2.THRESH_BINARY_INV
    ret, imgBinarizada = cv2.threshold(imgGray, 135, 255, metodo)
    # aplico o filtro da mediana para tirar os "respingos" pretos da área branca de grão
    imgMascaraSegmentacao = cv2.medianBlur(imgBinarizada, 9, dst=None)
    # pego contornos da área branca
    contours, hier = cv2.findContours(imgMascaraSegmentacao, cv2.RETR_LIST,
                                      cv2.CHAIN_APPROX_SIMPLE)
    # retira o fundo da imagem, baseado na máscara da mesma
    res = cv2.bitwise_and(imgOriginal, imgOriginal, mask=imgMascaraSegmentacao)
    # imprimo as imagens
    cv2.imshow("ImagemOriginal", imgOriginal)
    cv2.imshow("ImagemBinarizada", imgBinarizada)
    cv2.imshow("Mascara de Segmentacao", imgMascaraSegmentacao)
    cv2.imshow("ImagemFundo Retirado", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
