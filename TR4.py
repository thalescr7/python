
Meses = input("Digite um mes: ")

if Meses < "dezembro", "janeiro", "fevereiro":
    estação = "Verão"
elif Meses < "Março a junho":
    estação = "Outono"
elif Meses < "junho a setembro":
    estação = "Inverno"
elif Meses < "setembro a dezembro":
    estação = "Primavera"
else:
    categoria = "Meses"

print(f"Você está na estação: {estação}.")