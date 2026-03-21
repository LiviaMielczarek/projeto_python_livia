# conversão de real para dolar

#função para converter real para dolar
def converter_real_para_dolar(dolar, real): 
    conversao = real / dolar
    print (f'Valor convertido para dolar U$: {conversao:.2f}')
    return conversao

# entrada de dados
dolar = float (input ('Digite o valor do dolar hoje: '))
real = float (input('Qual o valor em real que deseja converter: '))

# chamando a função
converter_real_para_dolar(dolar, real)