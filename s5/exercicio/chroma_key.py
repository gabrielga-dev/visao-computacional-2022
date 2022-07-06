import cv2 as cv
from matplotlib import pyplot as plt

first_layer = cv.imread('first_layer.png')
second_layer = cv.imread('second_layer.png')

first_layer_gray_scale = cv.cvtColor(first_layer, cv.COLOR_BGR2GRAY)

qtd_rows = len(first_layer_gray_scale)
qtd_cols = len(first_layer_gray_scale[0])

result_image = []

for row in range(qtd_rows):
    for col in range(qtd_cols):
        current_value = first_layer_gray_scale[row][col]
        if (140 < current_value) and (current_value < 160):
            first_layer[row][col] = second_layer[row][col]


cv.imshow('resultado', first_layer)
cv.waitKey(0)
cv.destroyAllWindows()
