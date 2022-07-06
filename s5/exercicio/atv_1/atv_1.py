import cv2 as cv
from matplotlib import pyplot as plt

original = cv.imread('imagem.png')

original_gray_backup = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
original_gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)

for row in range(len(original_gray)):
    for col in range(len(original_gray[0])):
        if original_gray[row][col] > 127:
            original_gray[row][col] = 255
        else:
            original_gray[row][col] = 0

fig = plt.figure(figsize=(10, 7))

cv.imshow('resultado em gray', original_gray_backup)
cv.imshow('resultado', original_gray)
cv.waitKey(0)
cv.destroyAllWindows()
