
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
      
try:
    n1 = float(input("Digite o primeiro numero:"))
    n2 = float(input("Digite o segundo numero:"))
         
except ValueError:
    print("tente novamente")
                
soma = n1 + n2

print (f"(O numero {n1} mais o numero {n2} é igual a: {soma}.")
         
