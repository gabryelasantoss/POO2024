from sistema_vendas import Produto, Venda  

venda=Venda("2024-09-04")

def menu():
    while True:
        print("Menu")
        print("1.Adicionar produto à venda")
        print("2.Remover produto da venda")
        print("3.Listar todos os produtos da venda")
        print("4.Mostrar total da venda")
        print("5.Sair")
        opcao = input("Escolha uma opção:")

        if opcao=="1":
            nome=input("Digite o nome do produto:")
            preco=float(input("Digite o preço do produto:"))
            quantidade=int(input("Digite a quantidade do produto:"))
            produto=Produto(nome, preco, quantidade)
            venda.adicionar_produto(produto)
            print("Produto adicionado à venda.")

        elif opcao=="2":
            nome=input("Digite o nome do produto a ser removido:")
            venda.remover_produto(nome)
            print("Produto removido da venda.")

        elif opcao=="3":
            print("Produtos na venda:")
            print(venda.listar_produtos())

        elif opcao=="4":
            print("Total da venda: {:.2f}".format(venda.calcular_total()))

        elif opcao=="5":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
