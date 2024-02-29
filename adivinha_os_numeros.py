import random

def descubra_numero():
    print("Bem vindo ao jogo de adivinhação de números!")
    numero_secreto = obter_numero_secreto()
    numeros_acertados = ["_" for numero in numero_secreto]
    errou = False
    acertou = False
    erros = 0
    
    print("O número é: ", "".join(numeros_acertados))
    
    while not errou and not acertou:
        chute = input("Qual o número? ").strip().lower()
        
        if chute in numero_secreto:
            index = 0
            for letra in numero_secreto:
                if chute == numero:
                    numeros_acertados[index] = letra
                index += 1 
        else:
            erros += 1 
            desenha_numeros(erros)
            errou = erros == 7 
            acertou = "_" not in numeros_acertados
            print("O número é: ", "".join(numeros_acertados))
            
    if acertou:
        print("Parabéns, você ganhou!")
    else:
        print("Você errou o número!")
        print("O número certo era " + numero_secreto)

def obter_numero_secreto():
    palavras = ['56', '98', '23', '65', '1', '87', '76', '100', '12', '20']
    return random.choice(palavras) 

def desenha_numeros(erros):
    print("___")
    print("|\\   |")
    # Adicione mais linhas aqui para desenhar o boneco da forca
    
    

descubra_numero()
