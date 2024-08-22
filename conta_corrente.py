from POO2024.conta_bancaria import Conta_bancaria

class Conta_corrente(Conta_bancaria):
    def __init__(self, titular, cpf, saldo, numerocc):
        super().__init__(titular, cpf, saldo)
        self.numerocc=numerocc

    def mostrarcc(self):
        self.mostrar_conta()
        print(f"Número da Conta Corrente: {self.numerocc}")