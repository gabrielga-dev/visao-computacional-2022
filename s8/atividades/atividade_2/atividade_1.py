import cv2 as cv


def selec_menu(img):
    print('A. Média')
    print('B. Gauss')
    print('C. Vertical')
    print('D. Horizontal')
    print('E. Laplaciano')
    escolha = input('Sua escolha: ')
    if escolha == 'A':
        return cv.medianBlur(img, 5)
    elif escolha == 'B':
        return cv.GaussianBlur(img, (5, 5), 0)
    elif escolha == 'C':
        return cv.blur(img, (1, 15))
    elif escolha == 'D':
        return cv.blur(img, (15, 1))
    elif escolha == 'E':
        return cv.Laplacian(img, cv.CV_64F).var()
    print('Escolha invalida')
    quit()


def main():
    img = cv.imread('img.jpg')
    img = selec_menu(img)
    cv.imshow('result', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
