menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

extrato = ""

def deposito(saldo,valor):
    global extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo

def saque(saldo,valor):
    global extrato
    if valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
    return saldo

def extra(saldo):
    global extrato
    print("EXTRATO".center(40,'#'))
    print("Não houve movimentações na conta".center(40) if not extrato else extrato)
    print(f"\n Saldo: {saldo:.2f}")
    print('#' * 40)

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))
        saldo = deposito(saldo,valor)

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor que deseja sacar: "))
            if valor > saldo:
                print("Valor excede o disponivel em saldo")
                continue
            if valor <= limite:
                saldo = saque(saldo,valor)
                numero_saques += 1
            else:
                print("Valor do saque excedeu o limite")
        else:
            print("Numero de saques excedeu o limite")
            

    elif opcao == "e":
       
        extra(saldo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")