import pandas as pd

nome = ""
while nome == "":
    nome = str(input("Por favor, nos informe seu nome: "))

print(f"Olá {nome}, seja bem vindo ao meu codigo")

dadosDeClientes = {
    "nome": ["Thomas", "Paola", "Joseane", "Manoela", "Lorenzo"],
    "idade": [22, 26, 36, 18, 28],
    "cidade": ["Porto Alegre", "Sao leopoldo", "Sapucaia", "Novo hamburgo", "Gramado"],
    "ultima compra": ["Celular", "Notebook", "Tablet", "relogio Smartwatch", "Fone de ouvido s/ fio"]
}

tabela = pd.DataFrame(dadosDeClientes)

rodando = True
while rodando:
    print(f"\nComo posso te ajudar {nome}?")
    print("""
    1 - Adicionar cliente na lista
    2 - Consultar lista
    3 - Sair do programa
    """)

    pergunta = int(input("Escolha uma opção: "))

    if pergunta == 1:
        novo_nome = input("Nome: ")
        nova_idade = int(input("Idade: "))
        nova_cidade = input("Cidade: ")
        nova_compra = input("Ultima compra: ")

        novo_cliente = pd.DataFrame({
            "nome": [novo_nome],
            "idade": [nova_idade],
            "cidade": [nova_cidade],
            "ultima compra": [nova_compra]
        })

        tabela = pd.concat([tabela, novo_cliente], ignore_index=True)
        print("Cliente adicionado!")

    elif pergunta == 2:
        print(tabela)

    elif pergunta == 3:
        print("Saindo do programa...")
        rodando = False

    else:
        print("Opção inválida!")

print("obrigado :)")


