class Conta_bancaria:
    def __init__(self, titular, cpf, saldo):
        self.titular=titular
        self.cpf=cpf
        self.saldo=saldo

    def mostrar_conta(self):
        print(f"Titular: {self.titular}, CPF: {self.cpf}, Saldo: R${self.saldo:.2f}")
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"R${valor:.2f} valor depositado")
        else:
            print("Valor inválido.")
    def sacar(self, valor):
        if valor > 0 and valor<=self.saldo:
            self.saldo -=valor
            print(f"R${valor:.2f} sacado com sucesso!")
        else:
            print("Valor inválido.")
    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")