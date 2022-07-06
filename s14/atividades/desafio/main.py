import cv2 as cv


def detecta():
    captura_video = cv.VideoCapture(0)

    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    nose_cascade = cv.CascadeClassifier('haarcascade_nose.xml')
    correct_use = True

    while True:
        ret, frame = captura_video.read()
        frame = cv.flip(frame, 1)
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            break

        if len(faces) > 0:
            for face in faces:
                (xf, yf, wf, hf) = face
                roi = frame_gray[xf:xf + wf, yf:yf + hf]

                noses = nose_cascade.detectMultiScale(roi, scaleFactor=1.3, minNeighbors=5)

                if (len(noses)) != 0:
                    correct_use = False
                else:
                    correct_use = True

                if correct_use:
                    cv.putText(frame, "COM MASCARA", (int(xf), int(yf)), cv.QT_FONT_NORMAL, 1, (0, 255, 0), 1)
                else:
                    cv.putText(frame, "SEM MASCARA", (int(xf), int(yf)), cv.QT_FONT_NORMAL, 1, (0, 0, 255), 1)

        cv.imshow('gravando', frame)

        # se o usuario digitar a tecla q ou esc, fecha o loop
        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    captura_video.release()


if __name__ == "__main__":
    detecta()
