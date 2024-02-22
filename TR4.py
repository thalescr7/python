Meses = input("Digite um Mes:")

if Mes < "dezembro", "janeiro", "fevereiro":
    estação = "Verão"
elif Mes < "Março", "abril", "junho":
    estação = "Outono"
elif Mes < "junho", "julho", "agosto":
    estação = "Inverno"
elif Mes < "setembro", "outubro", "novembro":
    estação = "Primavera"
else:
    categoria = "Meses"

print(f"Você está na estação: {estação}.")
