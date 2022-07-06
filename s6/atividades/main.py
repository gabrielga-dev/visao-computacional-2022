import cv2 as cv
import numpy as np


def diferenca():
    captura = cv.VideoCapture(0)

    while True:
        ret, frame = captura.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow("Video", np.subtract(frame, quarto))

        k = cv.waitKey(30) & 0xff
        if k == 27:
            break

    captura.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    diferenca()
