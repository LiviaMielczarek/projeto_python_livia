#Autor: Livia Mielczarek
#Projeto: Copia de Listas

#Em Python, as listas são um recurso poderoso, mas todo recurso traz responsabilidades.
#Iremos ver um efeito colateral  ao copiar uma lista, e como evitar isso.

L = [1, 2, 3, 4, 5]

V = L

print('essa é a lista L:', L)
print('essa é a lista V:', V)

V[0] = 6
print('essa é a lista V modificada:', V)
print('essa é a lista L modificada:', L)