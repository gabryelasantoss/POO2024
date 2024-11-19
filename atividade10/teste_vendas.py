from Produto import Produto
from Venda import Venda, carregar_vendas_de_json
import json

vendas = []

opcao = "0"

while opcao != "6":
    print("\nMenu:")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Listar Produtos e Mostrar Total")
    print("4. Salvar Vendas em arquivo")
    print("5. Importar Vendas de um arquivo JSON")  
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if not vendas:
            print("Você precisa importar um arquivo JSON primeiro.")
            nome_arquivo = input("Digite o nome do arquivo JSON: ")
            vendas = carregar_vendas_de_json(nome_arquivo)
            if not vendas:
                print("Falha ao carregar o arquivo. Tente novamente.")
                continue 

        nome = input("Nome do Produto: ")
        
        preco_valido = False
        while not preco_valido:
            preco = input("Preço do Produto: ")
            preco = preco.replace(',', '.')
            try:
                preco = float(preco)
                preco_valido = True
            except ValueError:
                pass 

        quantidade_valida = False
        while not quantidade_valida:
            quantidade = input("Quantidade em Estoque: ")
            if quantidade.isdigit():
                quantidade = int(quantidade)
                quantidade_valida = True
            else:
                pass 

        produto = Produto(nome, preco, quantidade)
        
        if not vendas:
            print("Não há vendas carregadas. Importe um arquivo JSON para continuar.")
            continue 
        else:
            venda = vendas[-1]

        
        venda.get_produtos().append(produto)

    elif opcao == "2":
        if vendas:
            nome = input("Nome do Produto a remover: ")
            venda = vendas[-1]  
            venda.removerProduto(nome)

    elif opcao == "3":
        if vendas:
            venda = vendas[-1]
            venda.listarProdutos() 
            print(f"Total da Venda: R${venda.calcularTotal():.2f}")

    elif opcao == "4":
        if vendas:
            Venda.salvar_vendas_em_json(vendas, "vendas.json")

    elif opcao == "5":
        nome_arquivo = input("Digite o nome do arquivo JSON: ")
        vendas = carregar_vendas_de_json(nome_arquivo)
        if vendas:
            print(f"Vendas carregadas com sucesso do arquivo '{nome_arquivo}'.")
        else:
            print(f"Não foi possível carregar as vendas do arquivo '{nome_arquivo}'.")

    elif opcao == "6":
        print("Saindo...")

    else:
        print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE")
