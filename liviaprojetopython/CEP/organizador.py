#Consulta CEP em uma API pública (ViaCEP)

import requests

cep = input("Digite o CEP: ").strip().replace("-", "")

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
dados = resposta.json()

if "erro" in dados:
    print("CEP não encontrado.")
else:
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"UF: {dados['uf']}")