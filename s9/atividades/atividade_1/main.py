"""
pega a mediana da visinhança
"""
from builtins import range

import cv2 as cv


def main(m, img_path='placa.png'):
    img = cv.imread(img_path)

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # pega o numero de linhas e colunas
    qtdLinhas = len(img)
    qtdColunas = len(img[0])
    # percorre toda a imagem
    for l in range(qtdLinhas):
        for c in range(qtdColunas):
            if (l >= 1) and (l <= qtdLinhas - 2) and (c >= 1) and (c <= qtdColunas - 2):
                lista = []

                # primeira linha
                lista.append(float(img[l - 1][c - 1]) * m[0][0])
                lista.append(float(img[l - 1][c]) * m[0][1])
                lista.append(float(img[l - 1][c + 1]) * m[0][2])

                # segunda linha
                lista.append(float(img[l][c - 1]) * m[1][0])
                lista.append(float(img[l][c]) * m[1][1])
                lista.append(float(img[l][c + 1]) * m[1][2])

                # terceira linha
                lista.append(float(img[l + 1][c - 1]) * m[2][0])
                lista.append(float(img[l + 1][c]) * m[2][1])
                lista.append(float(img[l + 1][c + 1]) * m[2][2])

                # ordena
                lista.sort()

                # pega a mediana
                img[l][c] = lista[4]
    return img


if __name__ == "__main__":
    img_1 = main([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    print('sem maior')
    cv.imshow('(ALTA)', img_1)
    cv.waitKey(0)
    cv.destroyAllWindows()

    img_2 = main([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    cv.imshow('(MEDIA)', img_2)
    cv.waitKey(0)
    cv.destroyAllWindows()

    img_3 = main([[1, -2, 1], [-2, 3, -2], [1, -2, 1]])
    cv.imshow('(BAIXA)', img_3 * 10)
    cv.waitKey(0)
    cv.destroyAllWindows()
