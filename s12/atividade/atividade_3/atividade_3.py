import cv2


def retira_fundo(imgOriginal):
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
    return res


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
    i = 0  # variável contadora para mostrar rois
    # percorre os contornos de cada roi(pegos na linha acima) baseado na mascara
    for cnt in contours:
        if 10 < cv2.contourArea(cnt):  # testa se existem mais de 10 vertices
            # pego x,y altura e largura de cada ROI(espaços brancos na mascara)
            (x, y, alt, lar) = cv2.boundingRect(cnt)  # pega posição, largura e altura do roi
            roi = imgOriginal[y:y + lar, x:x + alt]  # corta rois
            cv2.imshow("ROI" + str(i), retira_fundo(roi))  # mostra rois
            # cv2.imwrite('res/roi'+str(i)+'.jpg', roi) #grava os rois
            i += 1
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()