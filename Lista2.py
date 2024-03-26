def gravar_lista(Lista):
  with open("lista.txt", "w") as arquivo:
    for item in lista:
      arquivo.write(f"{item}\n")
  print("Lista gravada com sucesso no arquivo 'lista.txt'!")

def main():
  lista = []
  menu = {
    '1': inserir_item,
    '2': excluir_item,
    '3': mostrar_lista,
    '4': gravar_lista,
    '5': lambda _: print("Programa encerrado.")
  }

  while True:
    print("1. Inserir novo item na lista")
    print("2. Excluir item da lista")
    print("3. Mostrar lista atual")
    print("4. Gravar lista")
    print("Sair")

    escolha = input("\nEscolha alguma opção: ")

    if escolha in menu:
      menu[escolha](lista)

    elif escolha == '4':
      gravar_lista(lista)
      print("Arquivo salvado com sucesso!")

    else:
      print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
  main()
