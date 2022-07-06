import random as rand
import statistics

vetor = []
escolha = 'TESTE'

while escolha != 5:
    print("1. Gerar vetor;\n2. listar vetor;\n3. calcular Média do vetor;\n4. calcular mediana do vetor;\n5. Sair")
    escolha = int(input('sua escolha: '))

    if escolha == 1:
        for x in range(100):
            vetor.append(rand.random())
        print('Vetor gerado com sucesso')

    elif escolha == 2:
        if len(vetor) == 0:
            print('Vetor vazio!')
        print(f'Vetor: {vetor}')

    elif escolha == 3:
        if len(vetor) == 0:
            print('Vetor vazio!')
        else:
            soma = 0
            for x in vetor:
                soma = soma + x
            print(f"Média do vetor: {(soma / len(vetor))}")

    elif escolha == 4:
        if len(vetor) == 0:
            print('Vetor vazio!')
        else:
            print(statistics.median(vetor))
    elif escolha == 5:
        print("Valeu!")
    else:
        print("Escolha inválida!")
