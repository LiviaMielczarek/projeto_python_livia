# Escreva um função que retorne o maior valor de dois numeros

numero1 = int (input('insira o primeiro valor'))
numero2 = int (input('insira o segundo valor'))

def maior_ou_menor(maximo):
    if numero1 == maximo:
        return "maior"
    else: 
        return "menor"

print(f"O numero {numero1} é maior {numero2}.")