# -*- coding:utf-8 -*-
"""
Exemplo de hello mostrando um laço de repetição e condição
"""

#fluxo de entrada jogado em uma variável, e definindo que ele será inteiro
y =  int(input("Digite um número"))
#inicialização de uma variável
x=0
#laço de repetição que vai de 0 ao numero acima cupracitado
for x in range(y):
    #exemplo de if
    if x > 2:
        print("MAIOR imprimindo x = "+str(x)+" de "+str(y))
    elif x < 2:
        print("MENOR imprimindo x = " + str(x) + " de " + str(y))
    else:
        print("IGUAL imprimindo x = " + str(x) + " de " + str(y))