import cv2 as cv
import pytesseract


def ocr(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    gray = cv.medianBlur(gray, 3)
    return pytesseract.image_to_string(gray)


def detecta_placa(img_path):
    img = cv.imread(img_path)

    img = img[130:300, 100:600]
    cv.waitKey(0)
    cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    _, bin = cv.threshold(cinza, 90, 255, cv.THRESH_BINARY)

    desfoque = cv.GaussianBlur(bin, (5, 5), 0)

    contornos, hier = cv.findContours(desfoque, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    roi = None
    for c in contornos:
        perimetro = cv.arcLength(c, True)
        if perimetro > 120:
            aprox = cv.approxPolyDP(c, 0.03 * perimetro, True)
            if len(aprox) == 4:
                (x, y, alt, lar) = cv.boundingRect(c)
                cv.rectangle(img, (x, y), (x + alt, y + lar), (0, 255, 0), 2)
                roi = img[y:y + lar, x:x + alt]
                # cv.imwrite('res/roi.jpg', roi)
    return roi


def main():
    roi = detecta_placa('./carro.jpg')
    cv.imshow('draw', roi)
    cv.waitKey(0)
    cv.destroyAllWindows()

    text = ocr(roi)
    print(text)


if __name__ == '__main__':
    main()
