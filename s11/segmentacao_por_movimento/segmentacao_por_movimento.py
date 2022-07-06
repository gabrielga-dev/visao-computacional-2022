import cv2
import numpy as np


def main():
    cap1 = cv2.imread("pecas_1.png")
    cap2 = cv2.imread("pecas_2.png")
    cv2.imshow("Peca1", cap1)
    cv2.imshow("Peca2", cap2)
    cv2.waitKey(0)
    imgRGB = cv2.subtract(cap2, cap1)
    cv2.imshow("subtraida", imgRGB)
    cv2.waitKey(0)
    imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)
    tomClaro = np.array([0, 120, 120])
    tomEscuro = np.array([180, 255, 255])
    imgSegmentada = cv2.inRange(imgHSV, tomClaro, tomEscuro)
    cv2.imshow("Segmentada", imgSegmentada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
