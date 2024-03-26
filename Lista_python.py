
def inserir_item(lista):
    novo_item = input("Digite o novo item: ")
    lista.append(novo_item)
    print("Parabens!, o seu item foi incluido com sucesso!")

def excluir_item(lista):
    item_a_excluir = input("Digite o item para excluir: ")
    if item_a_excluir in lista:
        lista.remove(item_a_excluir)
        print("Item excluído com sucesso!")
    else:
        print("O item não está mais na lista.")

def mostrar_lista(lista):
    print("Lista atual:", lista)

def main():
    lista = []
    menu = {
        '1': inserir_item,
        '2': excluir_item,
        '3': mostrar_lista,
        '4': lambda _: print("Programa encerrado.") 
    }
    
    while True:
        print("\n1. Inserir novo item na lista")
        print("2. Excluir item da lista")
        print("3. Mostrar lista atual")
        print("4. Sair")
        
        escolha = input("\nEscolha alguma opção: ")
        
        if escolha in menu:
            menu[escolha](lista)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()