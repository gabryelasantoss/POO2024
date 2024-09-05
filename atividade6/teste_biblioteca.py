from biblioteca import Autor, Livro, Biblioteca

def menu():
    biblioteca=Biblioteca()

    while True:
        print("Menu")
        print("1.Adicionar livro")
        print("2.Remover livro")
        print("3.Buscar livro")
        print("4.Listar todos os livros")
        print("5.Sair")
        opcao=input("Escolha uma opção:")

        if opcao=="1":
            titulo=input("Digite o título do livro:")
            nome_autor=input("Digite o nome do autor:")
            nacionalidade=input("Digite a nacionalidade do autor:")
            data_nascimento=input("Digite a data de nascimento do autor:")
            ano_publicacao=int(input("Digite o ano de publicação:"))
            autor=Autor(nome_autor, nacionalidade, data_nascimento)
            livro=Livro(titulo, autor, ano_publicacao)
            biblioteca.adicionar_livro(livro)

        elif opcao=="2":
            titulo=input("Digite o título do livro a ser removido:")
            biblioteca.remover_livro(titulo)

        elif opcao=="3":
            titulo=input("Digite o título do livro que deseja buscar:")
            resultado=biblioteca.buscar_livro(titulo)
            print(resultado)

        elif opcao=="4":
            biblioteca.listar_livros()

        elif opcao=="5":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
