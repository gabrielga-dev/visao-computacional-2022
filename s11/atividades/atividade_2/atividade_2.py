import cv2 as cv


def chroma_key_intensidade(first_layer, second_layer, start_limiar, final_limiar):
    first_layer_gray_scale = cv.cvtColor(first_layer, cv.COLOR_BGR2GRAY)

    qtd_rows = len(first_layer_gray_scale)
    qtd_cols = len(first_layer_gray_scale[0])

    for row in range(qtd_rows):
        for col in range(qtd_cols):
            current_value = first_layer_gray_scale[row][col]
            if (start_limiar <= current_value) and (current_value <= final_limiar):
                first_layer[row][col] = second_layer[row][col]

    return first_layer

def chroma_key_intervalor_de_cor(first_layer, second_layer, start_limiar, final_limiar):
    first_layer_gray_scale = cv.cvtColor(first_layer, cv.COLOR_BGR2HSV)

    qtd_rows = len(first_layer_gray_scale)
    qtd_cols = len(first_layer_gray_scale[0])

    for row in range(qtd_rows):
        for col in range(qtd_cols):
            current_value = first_layer_gray_scale[row][col][0]
            if (start_limiar <= current_value) and (current_value <= final_limiar):
                first_layer[row][col] = second_layer[row][col]

    return first_layer


def main():
    first_layer = cv.imread('first_layer.png')
    second_layer = cv.imread('second_layer.png')

    result_chroma_key_intensidade = chroma_key_intensidade(first_layer, second_layer, 140, 160)

    first_layer = cv.imread('first_layer.png')
    second_layer = cv.imread('second_layer.png')

    result_chroma_key_intervalor_de_cor = chroma_key_intervalor_de_cor(first_layer, second_layer, 58, 76)

    cv.imshow('por intensidade', result_chroma_key_intensidade)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imshow('por intensidade', result_chroma_key_intervalor_de_cor)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
#     vimos que o algoritimo que utiliza o padrao de cores HSV possui um resultado muito melhor e muito mais eficiente
