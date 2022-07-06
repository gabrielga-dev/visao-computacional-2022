#encoding: utf-8

########################################################################################
#FUNÇÕES (Procedimentos)
def addValor():
    valor = float(input("Digite o valor da doação: R$"))
    vetor.append(valor)

def listarInformacoes():

    totalArrecadado=0; qtdArrecadacoes = 0
    for i in range(len(vetor)):
        totalArrecadado += vetor[i]
        qtdArrecadacoes += 1


    resp = "-Total Arrecadado: R$%10.2f" % totalArrecadado

    resp+="\n-Quantidade de doações: %d" % qtdArrecadacoes
    if(qtdArrecadacoes>0):#previne a divisão por 0

        resp+="\n-Média de arrecadações: R$%10.2f" % (totalArrecadado/qtdArrecadacoes)

    return resp


#########################################################################################
#A PARTIR DAQUI É A EXECUÇÃO DO PROGRAMA
#########################################################################################

#cabeçalho do progrma
print("-------------------------------------------------------")
print("-Este programa é responsável por receber valores de   -")
print("-doações e apresentar resultados a partir de operações-")
print("-------------------------------------------------------")

#declaração do vetor
vetor = []

#variável usada para continuação ou parada do while do menu
continua = True
while(continua):
    #imprime opções do menu
    print ("MENU PRINCIPAL:\n"
           "-1 Para adicionar doações;\n"
           "-2 listar informações sobre as doações\n"
           "-3 Para sair.\n")

    #captura a opção digitada pelo usuário
    op = int(input("Digite o número de sua opção: "))

    #testa qual a opção digitada pelo usuário
    if(op == 1):
        #chama a função addValor
        addValor()
    elif(op == 2):
        textoResposta = listarInformacoes()
        print("\n-----------------------------\n" + textoResposta + "\n-----------------------------\n")
    elif(op == 3):
        continua = False

#quando o usuário sair do laço de repetição, printa uma saudação.
print ("Obrigado por utilizar o programa!  ;-)")

"""
Como exercício de fixação, o aluno deverá criar mais uma opção no menu(a de listar), 
deverá criar uma funação que irá listar todas as doações.
"""