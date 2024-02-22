
def calcular_letra_nota(nota):
    if nota >= 100:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 60:
        return "C"
    elif nota >= 40:
        return "D"
    else:
        return "F"


nota_aluno = float(input("Digite a sua nota: "))


letra = calcular_letra_nota(nota_aluno)


print(f"A nota {nota_aluno:.2f} corresponde à letra {letra}.")