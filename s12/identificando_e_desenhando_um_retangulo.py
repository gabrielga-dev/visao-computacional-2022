import cv2


def main():
    # carrego imagem
    imgOriginal = cv2.imread("cafe.png")
    # transformo em escala em cinza
    imgGray = img = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)
    # aplico a binarização invertida
    metodo = cv2.THRESH_BINARY_INV
    ret, imgBinarizada = cv2.threshold(imgGray, 135, 255, metodo)
    # aplico o filtro da mediana para tirar os "respingos" pretos da área branca do grão
    imgMascaraSegmentacao = cv2.medianBlur(imgBinarizada, 9, dst=None)
    # pego contornos da área branca
    contours, hier = cv2.findContours(imgMascaraSegmentacao, cv2.RETR_LIST,
                                      cv2.CHAIN_APPROX_SIMPLE)
    # percorro os contornos de cada elemento encontrado
    for cnt in contours:
        if cv2.contourArea(cnt):
            # pego x,y altura e largura de cada ROI(espaços brancos na mascara)
            (x, y, alt, lar) = cv2.boundingRect(cnt)
            # desenho os retângulos na tela
            cv2.rectangle(imgOriginal, (x, y), (x + alt, y + lar), (0, 255, 0), 2)
    # imprimo as imagens
    cv2.imshow("ImagemGrey", imgGray)
    cv2.imshow("ImagemBinarizada", imgBinarizada)
    cv2.imshow("Mascara de Segmentacao", imgMascaraSegmentacao)
    cv2.imshow("ImagemOriginal identificada", imgOriginal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
