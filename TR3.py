
#nome = input ("Escreva o seu nome")
#idade = input("Escreva a sua idade")
#idade = int(idade)
#print(f"Olá, {nome}, você tem {idade} anos.")
#try:
 #   idade=int(input("Escreva a sua idade"))
#except ValueError:
 #       print("Você nao digitou a sua idade!")
 
#Numero1= input("Escreva um numero de 1 a 10")

#Numero2= input("Escreva um numero de 20 a 50")
#try:
  #Numero1=int(input("Escreva um numero de 1 a 10!"))
#except ValueError:
      #print("Você nao digitou um numero de 1 a 10!")
      
#try:
   # n1 = float(input("Digite o primeiro numero:"))
   # n2 = float(input("Digite o segundo numero:"))
         
#except ValueError:
   # print("tente novamente")
                
#soma = n1 + n2

#print (f"(O numero {n1} mais o numero {n2} é igual a: {soma}.")


#solicitar notas
def nota_aluno(notas):
    if notas >= 100:
        return "A"
    elif notas >= 80:
        return "B"
    elif notas >= 60:
        return "C"
    elif notas >= 40:
        return "D"
    else:
        return "F"


nota_aluno = float(input("Digite a sua nota: "))


letra_nota = calcular_letra_nota(nota_aluno)


print(f"A nota {nota_aluno:.2f} corresponde à letra {letra_nota}.")
    # TODO: write code...