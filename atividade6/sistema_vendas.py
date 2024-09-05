class Produto:
    def __init__(self, nome:str, preco:float, quantidade:int):
        self.__nome=nome
        self.__preco=preco
        self.__quantidade=quantidade

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome: str):
        self.__nome = nome
    def get_preco(self):
        return self.__preco
    def set_preco(self, preco: float):
        self.__preco = preco
    def get_quantidade(self):
        return self.__quantidade
    def set_quantidade(self, quantidade: int):
        self.__quantidade = quantidade
    def exibir_produto(self):
        return "Nome: {}, Preço: {:.2f}, Quantidade: {}".format(self.__nome, self.__preco, self.__quantidade)
    
class Venda:
    def __init__(self, data_venda: str):
        self.__produtos=[]
        self.__data_venda=data_venda
        self.__total=0.0


    def get_produtos(self):
        return self.__produtos
    def set_produtos(self, produtos):
        self.__produtos = produtos
    def get_data_venda(self):
        return self.__data_venda
    def set_data_venda(self, data_venda:str):
        self.__data_venda=data_venda
    def get_total(self):
        return self.__total
    def set_total(self, total:float):
        self.__total=total
    def calcular_total(self):
        total = 0.0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        self.__total = total
        return total
    def adicionar_produto(self, produto):
        self.__produtos.append(produto)
        self.calcular_total()
    def remover_produto(self, nome_produto:str):
        for produto in self.__produtos:
            if produto.get_nome()==nome_produto:
                self.__produtos.remove(produto)
                self.calcular_total()
                break
    def listar_produtos(self):
        lista_produtos=""
        for produto in self.__produtos:
            lista_produtos += "{}\n".format(produto.exibir_produto())
        return lista_produtos
