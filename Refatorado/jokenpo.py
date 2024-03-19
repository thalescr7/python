import random

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    vitorias = 0
    
    print("Vamos jogar jokenpo?")
    print("Escolha: pedra, papel ou tesoura")

    while True:
        escolha_jogador = input("Sua escolha:")
        if escolha_jogador not in opcoes:
            print("Escolha inválida. Tente novamente!")
            continue

        escolha_computador = random.choice(opcoes)

        print(f"Computador escolheu: {escolha_computador}")

        resultado = ganhador(escolha_jogador, escolha_computador)

        resultado = ganhador(escolha_jogador, escolha_computador)
        print(resultado)

        if resultado == "Voce ganhou!":
            vitorias += 1
        elif resultado == "Voce perdeu!":
            vitorias -=1 

        if escolha_jogador == escolha_computador:
            print("Empate")
        elif(
            (escolha_jogador == "papel" and escolha_jogador == "pedra")or
            (escolha_jogador == "tesoura" and escolha_jogador == "papel") or
            (escolha_jogador == "pedra" and escolha_jogador == "tesoura")  ):
            print("Voce ganhou!")
            
        else:
            print("Voce perdeu!")

        jogar_novamente = input("Você deseja jogar novamente?").lower()
        if jogar_novamente != "sim":
            break

    
def ganhador(escolha_jogador, escolha_computador):

        if escolha_jogador == escolha_computador:
            print("Empate")
        elif(
            (escolha_jogador == "papel" and escolha_jogador == "pedra")or
            (escolha_jogador == "tesoura" and escolha_jogador == "papel") or
            (escolha_jogador == "pedra" and escolha_jogador == "tesoura")
        ):
            return "Voce ganhou!"
            
        else:
            return "Voce perdeu!"
    


if __name__ == "__main__":
    jogar_jokenpo()
