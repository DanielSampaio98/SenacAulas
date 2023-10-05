agenda = {}

def adicionar_contato():
    nome = input("informe o nome do contato: ")
    telefone = input("informe o telefone do contato: ")
    agenda[nome] = telefone
    print(f"contato: {nome} adicionado com sucesso!")

def lista_de_contatos():
    print("Mostra lista dos contatos:")
    for nome, telefone in agenda.items():
        print(f"Nome: {nome}, Telefone: {telefone}")

def pesquisar_contato():
    nome = input("informe o nome do contato: ")
    if nome in agenda:
        print(f"Nome: {nome}, Telefone: {agenda[nome]}")
    else:
        print(f" o contato {nome} não foi encontrado na agenda.")

while True:
    print("\nOpções:")
    print("1. Adicionar contato")
    print("2. Mostara contatos")
    print("3. Pesquisar contato")
    print("4. Sair")
    
    opcao = input("informe o numero: ")
    
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        lista_de_contatos()
    elif opcao == "3":
        pesquisar_contato()
    elif opcao == "4":
        print("finalizando a ação da agenda, saindo.")
        break
    else:
        print("a ação discada não é funcional, ERRO!!!!")
