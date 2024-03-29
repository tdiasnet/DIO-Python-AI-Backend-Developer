import textwrap

def menu():
    menu = """
    [d] = depositar
    [s] = sacar
    [e] = extrato
    [nc] = nova conta
    [lc] = listar contas
    [nu] = novo usuário
    [q] = sair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, deposito, extrato):
    if deposito > 0:
        saldo += deposito
        extrato += (f"Depósito de R$ {deposito:.2f}\n")

        return saldo, extrato
    else:
        return ("Digite um valor maior que 0")

def sacar(saldo, saque, extrato, limite, numero_saques, limite_saques):

    if saque > 0 and saque <= saldo and numero_saques < limite_saques:
        saldo -= saque
        extrato += (f"Saque de R$ {saque:.2f}\n")
        numero_saques += 1

        return saldo, extrato, numero_saques
    else:
        return ("Você digitou um valor negativo ou superior ao saldo ou atingiu o limite de saques.")

def exibir_extrato(saldo, extrato):
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato")
        print(extrato)
        print()
        print(f"Saldo R$ {saldo}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado)")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario[cpf] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()
        if opcao == "d":
            deposito = float(input("Valor para depósito: "))

            saldo, extrato = depositar(saldo, deposito, extrato)          

        elif opcao == "s":
            saque = float(input("Valor para saque: "))

            saldo, extrato, numero_saques = sacar(saldo, saque, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        deposito = float(input("Valor para depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato += (f"Depósito de R$ {deposito:.2f}\n")
        else:
            print("Digite um valor maior que 0")

    elif opcao == "s":
        saque = float(input("Valor para saque: "))

        if saque > 0 and saque <= saldo:
            saldo -= saque
            extrato += (f"Saque de R$ {saque:.2f}\n")
            numero_saques += 1
        else:
            print("Você digitou um valor negativo ou superior ao saldo.")

    elif opcao == "e":

        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato")
            print(extrato)
            print()
            print(f"Saldo R$ {saldo}")

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")