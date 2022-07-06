import cv2 as cv

placa_original = cv.imread('placa_velocidade.jpeg')

#  y=6 x=202
#  y=105 x=332
cropped = placa_original[6:105, 202:332]

placa_cinza = cv.cvtColor(cropped, cv.COLOR_BGR2GRAY)

start_red_value = 35
end_red_value = 254

for row in range(len(placa_cinza)):
    for col in range(len(placa_cinza[0])):
        atual = placa_cinza[row][col]
        if (start_red_value < atual) and (atual < end_red_value):
            placa_cinza[row][col] = 255


cv.imshow('result', placa_cinza)
cv.waitKey(0)
cv.destroyAllWindows()

# Este algoritmo realiza o crop da região de interesse e, assim, deixa a imagem em escala de cinza e, assim,
# remove todas as cores que não pertencem ao valor da velocidade descrita na placa para o tal fica em evidência.