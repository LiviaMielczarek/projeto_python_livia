import faker as apelido

falso_dado = apelido.Faker("pt_BR")

nome = falso_dado.name()

for i in range(100):
    print(falso_dado.name())
    print(f"Telefone: {falso_dado.phone_number()}")