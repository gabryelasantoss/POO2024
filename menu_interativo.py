from POO2024.conta_bancaria import Conta_bancaria
from POO2024.conta_corrente import Conta_corrente
from POO2024.conta_poupança import Conta_poupanca

contas = {}
opcao = 0
while opcao != 9:
    print("*** Bem-vindo ao Sistema Bancário ***")
    print("1) Criar Conta Corrente")
    print("2) Criar Conta Poupança")
    print("3) Depositar")
    print("4) Sacar")
    print("5) Verificar Saldo")
    print("6) Ver Rendimento ")
    print("7) Aplicar Rendimento (Poupança)")
    print("8) Mostrar Conta")
    print("9) SAIR")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        titular = input("Informe o nome do titular: ")
        cpf = int(input("Informe o CPF:"))
        saldo = float(input("Informe o saldo inicial: R$"))
        conta = (titular, cpf, saldo)
        contas[cpf] = conta
        print("Conta Corrente criada com sucesso!")

    elif opcao == 2:
        titular = input("Informe o nome do titular: ")
        cpf = input("Informe o CPF: ")
        saldo = float(input("Informe o saldo inicial: R$"))
        rendimento = float(input("Informe a taxa de rendimento (%): ")) / 100
        conta = Conta_poupanca(titular, cpf, saldo, rendimento)
        contas[cpf] = conta
        print("Conta Poupança criada com sucesso!")

    elif opcao == 3:
        cpf = input("Informe o CPF da conta:")
        valor = float(input("Informe o valor para depositar: R$"))
        print("valor depositado com sucesso")

    elif opcao == 4:
        cpf = input("Informe o CPF da conta: ")
        valor = float(input("Informe o valor para sacar: R$"))
        if cpf in contas:
            contas[cpf].sacar(valor)
            print("Valor sacado com sucesso!")
        else:
            print("Conta não encontrada. Retornando ao menu principal.")

    elif opcao == 5:
        cpf = input("Informe o CPF da conta: ")
        if cpf in contas:
            contas[cpf].verificar_saldo()
        else:
            print("Conta não encontrada. Retornando ao menu principal.")

    elif opcao == 6:
        cpf = input("Informe o CPF da conta: ")
        if cpf in contas and isinstance(contas[cpf], Conta_poupanca):
            contas[cpf].ver_rendimento()
        else:
            print("Conta poupança não encontrada ou CPF inválido. Retornando ao menu principal.")

    elif opcao == 7:
        cpf = input("Informe o CPF da conta: ")
        novorendimento=input("informe o rendimento em %:")
        print("rendimento aplicado com sucesso")

    elif opcao == 8:
        cpf = input("Informe o CPF da conta: ")
        if cpf in contas:
            conta = contas[cpf]
            if isinstance(conta, Conta_corrente):
                conta.mostrarcc()
            elif isinstance(conta, Conta_poupanca):
                conta.mostrar_conta()
        else:
            print("Conta não encontrada.")

    elif opcao == 9:
        print("Encerrando o sistema...")

    else:
        print("Opção inválida! Retornando ao menu principal.")