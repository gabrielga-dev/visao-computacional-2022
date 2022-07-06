from sobel_horizontal import sobel_horizontal
from sobel_vertical import sobel_vertical
import cv2 as cv


def binariza(path, limiar=100):
    img = cv.imread(path, 0)
    for row in range(len(img)):
        for col in range(len(img[0])):
            if img[row][col] > limiar:
                img[row][col] = 255
            else:
                img[row][col] = 0
    return img


def main(path):
    img_1 = sobel_horizontal(binariza(path))
    img_2 = sobel_vertical(binariza(path))

    result = img_1 + img_2

    cv.imshow('result', result)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main('placa.png')
