#Autor: Livia Mielczarek
#Projeto: Adição de Elementos na Lista
#A principal vantagem de usar listas é a possibilidade de adicionar elementos a elas.

L = []
L.append('a')

print('Valor Gravado na Lista:', L[0])
print(L)

L.append('b')
L.append('c')
print('A lista final é:', L)

print('#'  * 10)

L = []

while True:
    n = int(input('Digite um numero (0 para sair): '))
    if n == 0:
        break
    L.append(n)
x = 0
for i in L:
    x += i
print('A soma dos numeros digitados é:', x)
