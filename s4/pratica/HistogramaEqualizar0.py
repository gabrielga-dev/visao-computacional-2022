# -*- coding:utf-8 -*-
"""
Para equalizar um histograma, existem vários métodos. Vou usar um método que vem da estatística, que usa duas funções
simples, a Função Massa de Probabilidade (FMP, ou em inglês PMF), e Função Distribuição Acumulada (FDA, ou em inglês
CDF).

PMF:(um descritor de variável aleatória b)

A Função Massa de Probabilidade (Probability Mass Function), consiste em pegar a quantidade de elementos de uma classe
e dividir pela quantidade total de elementos do conjunto. Ou seja, basicamente é dividir a quantidade de pixels que
possuam o tom X pela quantidade total de pixels na imagem. Logo a PMF retorna a probabilidade de ocorrência do tom X na
imagem, nem preciso dizer que aplicaremos a PMF em todos os tons da imagem ! Para simplificar a coisa, vamos pensar em
um dado de 6 faces comum, a probabilidade de ocorrência de qualquer uma das faces quando o dado é jogado é 1/6, ou seja
a PMF de qualquer face do dado é 1/6. Se tivessemos um dado com 10 faces, e 5 faces tivessem numeros de 1 a 5, e as
outras 5 faces restantes tivessem o numero 6, a PMF para os numeros de 1 a 5 seria 1/10, já a PMF do numero 6 seria
5/10 0u 1/2. (:

Vamos supor que o histograma está armazenado na forma de um vetor com 256 posições, uma para cada tom de cinza (supondo
uma imagem com 256 tons), e que a imagem possua dimensões (800×600), ou seja, a imagem possui um total de 800 * 600 =
480000 pixels. Em código a função PMF seria assim:

// totalPixels = 480000
void pmf(double *hist, int totalPixels)
{
    int i;
    for(i = 0; i < hist.length; i++)
    {
        hist[i] = hist[i] / (float) totalPixels;
    }
}

CDF
A Função Distribuição Acumulada (Cumulative Distribution Function) retorna a probabilidade de ocorrência de um tom
menor que o tom analisado. Por exemplo, vou fazer uma analogia com um dado. Cada face do dado corresponde a um tom,
ou seja, 1-6 tons de cinza. A probabilidade de ocorrência de um tom (face) é 1/6 (valor retornado pela PMF).
Se quisermos saber a probabilidade ao lançarmos o dado de um valor menor ou igual a 4, basta somar as probabilidades de
ocorrência de todas as fazer menores ou iguais a 4, ou seja, 1/6 + 1/6 + 1/6 + 1/6 = 4/6. Pronto, acabamos de calcular
a CDF da face 4, de um dado de seis faces. Vale notar que a CDF é aplicado após a PMF. Em código seria parecido com
isso:
void cdf(double *hist)
{
    int i;
    for(i = 1; i < hist.length; i++)
    {
        hist[i] = hist[i] + hist[i-1];
    }
}

Normalização
Por último precisamos normalizar o valor obtido através da CDF, ou seja, precimaos que os valores armazenados no vetor
hist[], estejam entre 0-255, ou seja, os novos tons de cinza da imagem. Para tal, basta multiplicar cada valor do vetor
por 255, vale notar que o maior número guardado no vetor no momento é 1, que corresponte justamente à CDF do tom 255.
Assim como em um dado a CDF da face 6, corresponde a 1 (1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6), a CDF do maior tom também
é 1. Em código seria parecido com isso:

void normalize(double *hist)
{
    int i;
    for(i = 0; i < hist.length; i++)
    {
       hist[i] = hist[i] * 255;
    }
}
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

#pega imagem convertendo para escala em cinza
img = cv2.imread('imagem.jpg',0)
cv2.imshow("Cinza", img)
cv2.waitKey(0)

#gera o histograma
hist,bins = np.histogram(img.flatten(),256,[0,256])

#pega cdf(Função Distribuição Acumulada)
cdf = hist.cumsum()#cumsum soma acumulada do histograma

#mostra histograma não equalizado, m
plt.plot(cdf, color ='b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('Histograma não normalizado'), loc = 'upper left')
# plt.show()

#normaliza cdf
cdf_normalizado = cdf * hist.max() / cdf.max()
#equaliza bo braço
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

#converte na imagem
img2 = cdf[img]

#mostra imagem
cv2.imshow("Equalizado", img2)
cv2.waitKey(0)

#mostra histograma equalizado, m
plt.plot(cdf_normalizado, color ='b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf normalizado','histograma equalizado'), loc = 'upper left')
plt.show()

