#Criando Lista Vazia
lista = []
#Criando Lista com a Função list()
lista_com_funcao = list()
#Lista de valores heterogêneos
aleatorio = [2 , "a", 5.44, True]

#Calculo Media Usando Listas
notas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

while x < 10:
    notas[x] = float(input(f'nota {x}: '))
    soma += notas[x]
    x += 1

x = 0

while x < 10:
    print(f'nota {x}: {notas[x]}')
    x += 1

print(f"Media: {soma / x:.2f}")