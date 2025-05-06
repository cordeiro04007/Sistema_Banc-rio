menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = float(0)
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
            print('Depósito')
            global Valor_do_Deposito
            Valor_do_Deposito = float(input('Depósito da empresa ABCD no valor de: R$  '))
            global soma_deposito_saldo
            soma_deposito_saldo = Valor_do_Deposito + saldo
            print(f'Saldo após o depósito R$ {soma_deposito_saldo: .2f}')
            if Valor_do_Deposito > 0:
                print('Depósito realizado com sucesso!')
            else:
                print('Valores negativos de depósitos são inválidos!')
                break

    elif opcao == 's':
        print('Saque')
        if soma_deposito_saldo <= 0:
            print('Não é possível sacar por falta de saldo')
            break
        global Valor_do_Saque
        Valor_do_Saque = float(input('Saque o valor desejado: R$ '))
        if Valor_do_Saque > limite:
            print('Saques diários com limite máximo de R$ 500.00, tente novamente')
            break
        elif Valor_do_Saque > soma_deposito_saldo:
            print('Saldo insuficiente para saque, tente novamente')
            print(f'Saldo atual R$ {soma_deposito_saldo: .2f}')
            break
        else:
            soma_deposito_saldo -= Valor_do_Saque
            print(f'Saldo atual R$ {soma_deposito_saldo: .2f}')
            numero_saques += 1
        if numero_saques >= LIMITE_SAQUES:
            print('Limite de saques diários atingidos')
            break

    elif opcao == 'q':
        break

    elif opcao == 'e':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {soma_deposito_saldo:.2f}")
        print("==========================================")


    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')

