import cv2 as cv


def main():
    # carrega xml de treinamento de identificação de faces
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    # carrega xml de treinamento de detecção de Boca
    boca_cascade = cv.CascadeClassifier('haarcascade_mouth.xml')
    # carrega imagens
    img = cv.imread('candidatos.jpg')
    # converte para cinza
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # detecta faces: minNeighbors mínimo de visinhos
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    # Desenha retangulos pelo x e y do ponto com largura e altura
    for (x, y, w, h) in faces:
        # desenha cada um dos retangulos
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        # identifica dentro de roi gray(rosto detectado em escala em cinza) em uma escala menor
        mouths = boca_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=9,
                                         maxSize=(35, 30))
        for (ex, ey, ew, eh) in mouths:
            cv.rectangle(roi_color, (ex + x, ey + y), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv.imshow('img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
