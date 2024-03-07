def jogar():
def jogar_forca():
    print("Bem-vindo ao jogo da forca!")
    palavra_secreta = obter_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print("A palavra é: ", " ".join(letras_acertadas))

    while(not enforcou and not acertou):
        chute = input("Qual letra? ").strip().lower()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print("A palavra é: ", " ".join(letras_acertadas))

    if(acertou):
        print("Parabéns, você ganhou!")
    else:
        print("Você foi enforcado!")
        print("A palavra era " + palavra_secreta)

def obter_palavra_secreta():
    palavras = ['casa', 'carro', 'bicicleta', 'computador', 'python','thales','paralelepipedo','carralho','kidbengala']
    return random.choice(palavras)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar_forca()
