import textwrap


def menu():
    menu = """\n
    ===========Menu===========
    [1]\t Depositar
    [2]\t Sacar
    [3]\t Extrato
    [4]\t Novo usuário
    [5]\t Nova conta
    [6]\t Listar contas
    [0]\t Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")

    else:
        print("\n@@@ Falha na operação! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
     
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print(f"\n@@@ Falha na operação! Saldo insuficiente. Seu saldo atual é de R$: {saldo:.2f}. @@@")

    elif excedeu_limite:
        print("\n@@@ Falha na operação! O valor do saque excedeu o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Falha na operação! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque:\t R$ {valor:.2f}\n"
        print("\n=== Saque realizado com sucesso! Por favor, retire as notas. ===")

    else:
        print("\n@@@ Falha na operação! O valor informado é inválido. @@@")

    return saldo, extrato

def exibit_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print("\n", 25*"-", "\n")
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print("========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe um usuário cadastrado com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário cadastrado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta ciada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibit_extrato(saldo, extrato=extrato)


        elif opcao == "4":
            criar_usuario(usuarios)
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("\nObrigado por utilizar nossos serviços. Tenha um bom dia! Até breve!!\n")
            break

        else:
            print("\nOperação inválida! Por favor selecione, dentre as opções, a operação desejada.")

main()