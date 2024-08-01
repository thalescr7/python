def inverter_string(string):
    return string[::-1]

entrada = input("Digite um nome: ")
saida = inverter_string(entrada)
print("String invertida:", saida)