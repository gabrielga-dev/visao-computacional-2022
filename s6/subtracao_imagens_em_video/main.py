import cv2 as cv
import numpy as np


def diferenca():
    v = cv.VideoCapture(0)
    cont = 0
    frame_1 = None
    frame_2 = None
    cap_frame_1 = False
    cap_frame_2 = False

    while True:
        x, frame = v.read()

        if cont == 0:
            frame_1 = frame
            cap_frame_1 = True
        cont += 1

        if cont == 14:
            frame_2 = frame
            cap_frame_2 = True
            cont = 0

        if cap_frame_1 and cap_frame_2:
            cap_frame_1 = False
            cap_frame_2 = False
            result = cv.subtract(frame_2, frame_1)
            cv.imshow("Video", result)

        k = cv.waitKey(30) & 0xff
        if k == 27:
            break

    v.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    diferenca()
