import json
from Produto import Produto

class Venda:
    def __init__(self, dataVenda):
        self.__produtos = []  
        self.__dataVenda = dataVenda
        self.__total = 0.0

    def get_produtos(self):
        return self.__produtos
        
    def get_dataVenda(self):
        return self.__dataVenda

    def get_total(self):
        return self.__total

    def set_dataVenda(self, dataVenda):
        self.__dataVenda = dataVenda

    def calcularTotal(self):
        total = 0.0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total

    def removerProduto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                print(f"Produto {nome} removido.")
                return
        print(f"Produto {nome} não encontrado.")

    def listarProdutos(self):
        if not self.__produtos:
            print("Nenhum produto na venda.")
        else:
            print(f"\nProdutos na Venda do dia {self.__dataVenda}:")
            for produto in self.__produtos:
                print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")

    def to_dict(self):
        return {
            "dataVenda": self.__dataVenda,
            "produtos": [produto.to_dict() for produto in self.__produtos],  
            "total": self.calcularTotal()
        }

    @staticmethod
    def salvar_vendas_em_json(vendas, arquivo):
        vendas_dict=[venda.to_dict() for venda in vendas]
        with open(arquivo, 'w') as f:
            json.dump(vendas_dict, f, indent=4)
        print(f"Vendas salvas no arquivo '{arquivo}'.")

    @classmethod
    def from_dict(cls, venda_data):
        venda=cls(venda_data['dataVenda'])
        for produto_data in venda_data['produtos']:
            produto=Produto(produto_data['nome'], produto_data['preco'], produto_data['quantidade'])
            venda.get_produtos().append(produto)
        return venda    

def carregar_vendas_de_json(arquivo):
    try:
        with open(arquivo, 'r') as f:
            vendas_data=json.load(f) 
            vendas=[Venda.from_dict(venda_data) for venda_data in vendas_data]  
        return vendas
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
        return []  
