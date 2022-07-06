import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def main():
    captura = cv.VideoCapture(0)

    while True:
        ref, frame = captura.read()
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(frame_gray, 100, 200)
        res = np.hstack((frame_gray, edges))
        cv.imshow("Filtor de Canny", res)

        # se o usuario digitar a tecla q ou esc, fecha o loop
        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    captura.release()


if __name__ == "__main__":
    main()
