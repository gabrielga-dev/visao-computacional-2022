import cv2 as cv
from matplotlib import pyplot as plt

video = cv.VideoCapture("video.mp4")

# enquanto houver video carrega frame a frame na janela
while True:
    ret, frame = video.read()

    frame_grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    for row in range(len(frame_grayscale)):
        for col in range(len(frame_grayscale[0])):
            if frame_grayscale[row][col] > 127:
                frame_grayscale[row][col] = 255
            else:
                frame_grayscale[row][col] = 0

    cv.imshow("Binarizada", frame_grayscale)

    # se o usuario digitar a tecla 1 ou esc, fecha o loop
    if cv.waitKey(30) & 0xFF == ord('q'):
        break
video.release()
cv.destroyAllWindows()
