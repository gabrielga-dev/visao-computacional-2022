import cv2 as cv


def main(matrix):
    img = cv.imread('img.png')

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
                lista.append(float(img[l - 1][c - 1]) * matrix[0][0])
                lista.append(float(img[l - 1][c]) * matrix[0][1])
                lista.append(float(img[l - 1][c + 1]) * matrix[0][2])

                # segunda linha
                lista.append(float(img[l][c - 1]) * matrix[1][0])
                lista.append(float(img[l][c]) * matrix[1][1])
                lista.append(float(img[l][c + 1]) * matrix[1][2])

                # terceira linha
                lista.append(float(img[l + 1][c - 1]) * matrix[2][0])
                lista.append(float(img[l + 1][c]) * matrix[2][1])
                lista.append(float(img[l + 1][c + 1]) * matrix[2][2])

                # ordena
                lista.sort()

                # pega a mediana
                img[l][c] = lista[4]
    return img


if __name__ == '__main__':
    img1 = main(
        [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ]
    )
    img2 = main(
        [
            [-1, -1, -1],
            [-1, 9, -1],
            [-1, -1, -1]
        ]
    )
    img3 = main(
        [
            [1, -2, 1],
            [-2, 5, -2],
            [1, -2, 1]
        ]
    )

    cv.imshow('passa baixa', img1)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imshow('passa alta', img2)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imshow('passa baixa', img3)
    cv.waitKey(0)
    cv.destroyAllWindows()
