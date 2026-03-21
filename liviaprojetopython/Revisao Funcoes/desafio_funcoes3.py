# Escreva um função que retorne o maior valor de dois numeros

numero1 = int (input('insira o primeiro valor'))
numero2 = int (input('insira o segundo valor'))

def maior_ou_menor(maximo1, maximo2):
    if maximo1 == maximo2:
        return f"valores iguais"
    elif maximo1 > maximo2:
        return f"O valor {maximo1} é o maior"
    else: 
        return f"O valor {maximo2} é o maior"
    
print (maior_ou_menor(numero1, numero2)) 