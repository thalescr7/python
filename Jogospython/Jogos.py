import forca1
import advinhacao

def escolha_Jogo():
    print('-------------------------------------------')
    print('-------------Escolha o jogo----------------')
    print('-------------------------------------------')
    print('(1) - Forca')
    print('(2) - Adivinhação')
    escolha = int(input('Digite a opção desejada: '))
    if escolha == 1:
        forca1.jogar()
    elif escolha == 2:
        advinhacao.jogar()
    else:
        print('Digite uma opção certa o filho de uma boa mae!')

if(__name__=="__main__"):
    escolha_Jogo()