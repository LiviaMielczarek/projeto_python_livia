#Autor: Livia Mielczarek
#Projeto: Trabalhando com Indices
#Programa que le cinco numeros e armazena em uma lista, depois solicita ao usuario que escolha 
#um numero a mostrar

numeros = [0] * 5
x = 0

while x < 5:
    numeros[x] = int(input(f'Numero ({x + 1}): '))
    x += 1

while True:
    escolha = int(input("Que posição voce quer imprimir? (1-5, 0 para sair): "))

    if escolha == 0:
        print('Encerrando o programa.')
        break
    elif escolha < 1 or escolha > 5:
        print('Numero invalido, tente novamente')
    else:
        print(f'Numero escolhido: {numeros[escolha - 1]}')
