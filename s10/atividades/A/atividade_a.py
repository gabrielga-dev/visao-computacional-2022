# -*- coding:utf-8 -*-
import math
import numpy as np

"""
Filtro que permite mostrar bordas, mesmo na presença de ruido
primeiro suaviza o ruido com a derivada de gauss
aplica mascaras de gradiente (assim como o sobel)
em seguida faz a supreção de não máximos(na direção do gradiente,não na conexção de
pixel)
limiarização por histerese(adaptativa)
"""
import cv2


def lim(x):
    if (x > 253):
        return 253
    else:
        return x


def abs(x):
    if (x < 0):
        return x * -1
    else:
        return x


def primeiraDerifadaGaussUni(x, desvio):
    fator = float(1.0 / float(desvio * math.sqrt(2.0 * math.pi)))
    return fator * math.exp(float(float(-1.0 * x ** 2) / float(2.0 * desvio ** 2)))


def primeiraDerifadaGaussBi(x, desvio):
    fator = float(1.0 / float(desvio * math.sqrt(2.0 * math.pi)))
    return fator * math.exp(float(float(-1.0 * x ** 2) / float(2.0 * desvio ** 2)))


def getMaiorIntensidade(l, c, imgX):
    li = l - 1
    ci = c - 1
    maiorIntensidade = 0
    while (li < l + 1):
        while (ci < c + 1):
            if (maiorIntensidade < imgX[li][ci]):
                maiorIntensidade = imgX[li][ci]
            ci += 1
        li += 1
    return maiorIntensidade


def main():
    # pega imagem convertendo para escala em cinza
    img = cv2.imread('ifmg.png')
    # Mostra a imagem
    cv2.imshow("Cinza", img)
    cv2.waitKey(0)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    cv2.imshow("blur", img)
    cv2.waitKey(0)
    # sobel horizontal
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # sobel vertical
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imagem crua para fazer a convolução
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ####################################
    # aplicação dos gradientes de sobel
    mh = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]  # horizontal
    mv = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]  # vertical
    md1 = [
        [0, -1, -2],
        [1, 0, -1],
        [2, 1, 0]
    ]  # diagonal 1
    md2 = [
        [-2, -1, 0],
        [-1, 0, 1],
        [0, 1, 2]
    ]  # diagonal 2
    # pega o numero de linhas e colunas
    qtdLinhas = len(img)
    qtdColunas = len(img[0])
    print(qtdLinhas, qtdColunas)

    # percorre toda a imagem
    for l in range(qtdLinhas):
        for c in range(qtdColunas):
            # se não for a primeira coluna ou linha de pixels nem as ultimas,
            # faça(por causa da convolução pixel a pixel)
            if (l >= 1 and l <= qtdLinhas - 2 and c >= 1 and c <= qtdColunas - 2):
                lm = 0
                somaH = 0.0
                somaV = 0.0
                for lf in range(l - 1, l + 2):
                    cm = 0
                    for cf in range(c - 1, c + 2):
                        somaH += float(img[lf][cf] * md1[lm][cm])
                        somaV += float(img[lf][cf] * md2[lm][cm])
                        cm += 1
                    lm += 1
                somaH = lim(abs(somaH))
                somaV = lim(abs(somaV))

                img1[l][c] = float(somaH)
                img2[l][c] = float(somaV)

    # adiciona o horzontal ao vertical
    img3 = cv2.absdiff(img2, img1)
    img4 = cv2.absdiff(img2, img1)
    res = np.hstack((img1, img2, img3))
    cv2.imshow("H/V Sobel e Sobel H+V", res)
    cv2.waitKey(0)

    # Supressão de não máximos
    # percorre toda a imagem
    for l in range(qtdLinhas):
        for c in range(qtdColunas):
            # se não for a primeira coluna ou linha de pixels nem as ultimas,
            # faça(por causa da convolução pixel a pixel)
            if (l >= 1 and l <= qtdLinhas - 2 and c >= 1 and c <= qtdColunas - 2):
                # verifica a intensidade máxima
                maiorIntensidade1 = getMaiorIntensidade(l, c, img1)
                maiorIntensidade2 = getMaiorIntensidade(l, c, img2)
                print(maiorIntensidade1, maiorIntensidade2)
                # suprime os não maximos da primeira imagem
                li = l - 1
                ci = c - 1
                while (li < l + 1):
                    while (ci < c + 1):
                        if (maiorIntensidade1 > img1[li][ci]):
                            img1[li][ci] = 0
                        ci += 1
                    li += 1
                # suprime os não máximos da segunda imagem
                li = l - 1
                ci = c - 1
                while (li < l + 1):
                    while (ci < c + 1):
                        if (maiorIntensidade2 > img2[li][ci]):
                            img2[li][ci] = 0
                        ci += 1
                    li += 1
    img3 = cv2.absdiff(img2, img1)
    res = np.hstack((img1, img2, img3))
    cv2.imshow("Supressao", res)
    cv2.waitKey(0)

    ##############################################
    # aplica histerese
    # define os graus de liberdade para limiarização por maior intensidade
    ##############################################
    # aplica a limiarização por faixa
    # percorrendo linhas e colunas da imagem
    grausLiberdade = 30  # (alterar para menos observando pixels não limitados)
    intensidade = 240

    # img3 = cv2.GaussianBlur(img3, (3, 3), 0)
    for l in range(qtdLinhas):
        for c in range(qtdColunas):
            if (img3[l][c] < intensidade - grausLiberdade or img3[l][c] > intensidade + grausLiberdade):
                img4[l][c] = 0
            else:
                img4[l][c] = 255
    cv2.imshow("Saida", img4)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
