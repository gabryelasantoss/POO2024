class Autor:
    def __init__(self, nome:str, nacionalidade:str, data_nascimento:str):
        self.__nome=nome
        self.__nacionalidade=nacionalidade
        self.__data_nascimento=data_nascimento

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome: str):
        self.__nome=nome
    def get_nacionalidade(self):
        return self.__nacionalidade
    def set_nacionalidade(self, nacionalidade: str):
        self.__nacionalidade = nacionalidade
    def get_data_nascimento(self):
        return self.__data_nascimento
    def set_data_nascimento(self, data_nascimento: str):
        self.__data_nascimento = data_nascimento
    def exibir_autor(self):
        return "Nome: {}, Nacionalidade: {}, Data de Nascimento: {}".format(self.__nome, self.__nacionalidade, self.__data_nascimento)

class Livro:
    def __init__(self, titulo:str, autor:Autor, ano_publicacao:int):
        self.__titulo=titulo
        self.__autor=autor
        self.__ano_publicacao=ano_publicacao

    def get_titulo(self):
        return self.__titulo
    def set_titulo(self, titulo:str):
        self.__titulo=titulo
    def get_autor(self):
        return self.__autor
    def set_autor(self, autor: Autor):
        self.__autor=autor
    def get_ano_publicacao(self):
        return self.__ano_publicacao
    def set_ano_publicacao(self, ano_publicacao:int):
        self.__ano_publicacao=ano_publicacao
    def exibir_livro(self):
        return "Título: {}, Autor: {}, Ano de Publicação: {}".format(self.__titulo, self.__autor.get_nome(), self.__ano_publicacao)

class Biblioteca:
    def __init__(self):
        self.__livros=[]

    def adicionar_livro(self, livro:Livro):
        self.__livros.append(livro)
        print("Livro '{}' adicionado à biblioteca.".format(livro.get_titulo()))
    def remover_livro(self, titulo:str):
        for livro in self.__livros:
            if livro.get_titulo()==titulo:
                self.__livros.remove(livro)
                print("Livro '{}' removido com sucesso.".format(titulo))
                return
        print("Livro '{}' não encontrado.".format(titulo))
    def buscar_livro(self, titulo:str):
        for livro in self.__livros:
            if livro.get_titulo()==titulo:
                return livro.exibir_livro()
        return "Livro '{}' não encontrado.".format(titulo)
    def listar_livros(self):
        if not self.__livros:
            print("Nenhum livro disponível.")
        else:
            for livro in self.__livros:
                print(livro.exibir_livro())
