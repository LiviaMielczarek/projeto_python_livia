# Autor Livia

# codigo sem funcoes 

# calculadora sem funcoes

# numero1 = float(input('Digite o primeiro numero: '))
# numero2 = float(input('Digite o segundo numero:'))

# soma = numero1 + numero2
# subtracao = numero1 - numero2
# multiplicacao = numero1 * numero2
# divisao = numero1 / numero2

# print(f'O Resultado da Soma é {soma}')
# print(f'O Resultado da Subtracao é {subtracao}')
# print(f'O Resultado da Multiplicacao é {multiplicacao}')
# print(f'O Resultado da Divisao é {divisao}')

# codigo com funcoes

# variáveis para armazenar os valores
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

# Criando a função para realizar os cálculos
def calculos(a, b):
    soma=a+b
    subtracao=valor1-valor2
    mutiplicacao=valor1*valor2
    divisao=valor1/valor2

    print("O resultado da soma é: ",soma)
    print("O resultado da subtração é: ",subtracao)
    print("O resultado da mutiplicação é: ",mutiplicacao)
    print("O resultado da divisão é: ",divisao)

# Chamando a função
calculos(valor1, valor2)
