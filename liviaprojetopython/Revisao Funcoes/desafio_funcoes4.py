#Função para calculo da area do triangulo

def calculo_area(b, a):
    area = (b * a) / 2
    return area

base = float(input("valor da base:"))
altura = float(input("valor da altura:"))

resultado = calculo_area(base, altura)
print(f"A area do triangulo é {resultado:.2f}")
