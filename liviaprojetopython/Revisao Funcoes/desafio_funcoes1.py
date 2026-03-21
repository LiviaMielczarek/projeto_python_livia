# Fazer uma função que indica que o numero é par

numero = int(input('Insira um numero'))

def ehpar (numero) :
    if numero % 2 ==0:
     print ('o numero digitado é par')
    else: 
     print ('o numero digitado é impar')

ehpar(numero)
