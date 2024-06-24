menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso!")

        else:
            print("\nFalha na operação! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nFalha na operação! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\nFalha na operação! O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("\nFalha na operação! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado com sucesso! Por favor, retire as notas.")

        else:
            print("\nFalha na operação! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("==========================================")

    elif opcao == "0":
        print("\nObrigado por utilizar nossos serviços. Tenha um bom dia! Até breve!!\n")
        break

    else:
        print("\nOperação inválida! Por favor selecione, dentre as opções, a operação desejada.")