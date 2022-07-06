# -*- coding:utf-8 -*-
import math
import numpy as np

import cv2 as cv


def lim(x):
    if (x > 253):
        return 255
    else:
        return x


def abs(x):
    if (x < 0):
        return x * -1
    else:
        return x


def sobel_horizontal(img):
    # sobel horizontal
    img1 = img * 1

    mh = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]  # horizontal

    # pega o numero de linhas e colunas
    qtdLinhas = len(img)
    qtdColunas = len(img[0])
    print(qtdLinhas, qtdColunas)

    # percorre toda a imagem
    for l in range(qtdLinhas):
        for c in range(qtdColunas):
            # se não for a primeira coluna ou linha de pixels nem as ultimas, faça(por causa da convolução pixel a pixel)
            if (l >= 1 and l <= qtdLinhas - 2 and c >= 1 and c <= qtdColunas - 2):
                lm = 0
                somaH = 0.0
                for lf in range(l - 1, l + 2):
                    cm = 0
                    for cf in range(c - 1, c + 2):
                        somaH += float(img[lf][cf] * mh[lm][cm])
                        cm += 1
                    lm += 1
                somaH = lim(abs(somaH))
                img1[l][c] = float(somaH)

    return img1
