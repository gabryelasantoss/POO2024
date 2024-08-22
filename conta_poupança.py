from POO2024.conta_bancaria import Conta_bancaria

class Conta_poupanca(Conta_bancaria):
    def __init__(self, titular, cpf, saldo, rendimento):
        super().__init__(titular, cpf, saldo)
        self.rendimento=rendimento

    def ver_rendimento(self):
        print(f"Rendimento: {self.rendimento * 100:.2f}% ao mês")

    def render(self):
        valor_rendimento = self.saldo * self.rendimento
        self.saldo+=valor_rendimento
        print(f"Rendimento aplicado: R${valor_rendimento:.2f}")