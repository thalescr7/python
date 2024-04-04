import os

def mostrarLista(lista):
    print("Lista atual:", lista)

def addItemLista(lista):
    novo_item = input("Digite um novo item para adicionar na lista: ")
    lista.append(novo_item)

def excluirItemLista(lista):
    itemExcluir = input("Digite o item a ser excluído da lista: ")
    if itemExcluir in lista:
        lista.remove(itemExcluir)
    else:
        print("O item não está na lista.")

def mostrarListaAtual(lista):
    mostrarLista(lista)

def gravarLista(lista):
    arquivo = input("Digite o nome do arquivo a ser gravado: ")
    try:
        with open(arquivo, 'w') as f:
            f.write(str(lista))
        print("Lista gravada com sucesso no arquivo", arquivo)
    except Exception as e:
        print("Erro ao gravar o arquivo:", e)

def lerArquivoLista():
    arquivos = os.listdir()
    print("Lista de Arquivos disponíveis:")
    for arquivo in arquivos:
        print(arquivo)
    arquivoEscolhido = input("Digite o nome do arquivo para ler: ")
    try:
        with open(arquivoEscolhido, 'r') as f:
            lista = eval(f.read())
            mostrarLista(lista)
            return lista
    except Exception as e:
        print("Erro ao ler o arquivo:", e)

def sair():
    print("Saindo do programa...")
    exit()

def escolherOpcao(lista):
    while True:
        print(" Escolha uma opção:")
        print("1 - Adicionar item na lista")
        print("2 - Excluir um item da lista")
        print("3 - Mostrar lista")
        print("4 - Gravar lista")
        print("5 - Ler um arquivo de lista epecifico")
        print("6 - Sair")

        opc = input("Digite a opção desejada: ")

        if opc == '1':
            addItemLista(lista)
        elif opc == '2':
            excluirItemLista(lista)
        elif opc == '3':
            mostrarListaAtual(lista)
        elif opc == '4':
            gravarLista(lista)
        elif opc == '5':
            lista = lerArquivoLista()
        elif opc == '6':
            sair()
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    lista = []
    escolherOpcao(lista)
