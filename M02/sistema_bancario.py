menu = """
    d = depositar
    s = sacar
    e = extrato
    q = sair
"""

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