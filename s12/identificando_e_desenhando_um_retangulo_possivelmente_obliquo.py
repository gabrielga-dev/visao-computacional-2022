import cv2
import numpy as np


def main():
    # carrego imagem
    imgOriginal = cv2.imread("cafe.png")
    imgGray = img = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)
    # aplico a binarização invertida
    metodo = cv2.THRESH_BINARY_INV
    ret, imgBinarizada = cv2.threshold(imgGray, 135, 255, metodo)
    # aplico o filtro da mediana para tirar os "respingos" pretos da área branca do grão
    imgMascaraSegmentacao = cv2.medianBlur(imgBinarizada, 9, dst=None)
    # pego contornos da área branca
    contours, hier = cv2.findContours(imgMascaraSegmentacao, cv2.RETR_LIST,
                                      cv2.CHAIN_APPROX_SIMPLE)
    # desenho os contornos(pegos na linha acima) baseado na mascara
    for cnt in contours:
        if cv2.contourArea(cnt):
            # A direção é o ângulo no qual o objeto é orientado
            (x, y), (MA, ma), angle = cv2.fitEllipse(cnt)  # modifica cnt a fim de obter angulo
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            imgOriginal = cv2.drawContours(imgOriginal, [box], 0, (0, 0, 255), 2)
    # imprimo as imagens
    cv2.imshow("ImagemGrey", imgGray)
    cv2.imshow("ImagemBinarizada", imgBinarizada)
    cv2.imshow("Mascara de Segmentacao", imgMascaraSegmentacao)
    cv2.imshow("ImagemOriginal identificada", imgOriginal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
