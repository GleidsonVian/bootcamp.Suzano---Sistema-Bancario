menu = """"
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
def depositar_dinheiro(saldo,historico_de_extrato):
    dinheiro_para_depositar = int(input('Quanto você deseja depositar? '))
    saldo += dinheiro_para_depositar
    historico_de_extrato += f"Depositado R$ {dinheiro_para_depositar}\n"
    print(f"Depositado {dinheiro_para_depositar}")
    return saldo, historico_de_extrato

def sacar_dinheiro(saldo,quantidade_de_saques,historico_de_extrato,limite_de_saque=500):
    dinheiro_para_sacar = int(input('Quanto você deseja sacar? '))
    if quantidade_de_saques <= 0:
        print("Limite diario de saques atingido")

    elif saldo <= 0:
        print("Não será possivel sacar o dinheiro por falta de saldo")

    elif dinheiro_para_sacar > limite_de_saque:
        print(f"Limite de saque é RS {limite_de_saque}")

    elif dinheiro_para_sacar > saldo:
        print("Não será possivel sacar o dinheiro por falta de saldo")

    else:
        saldo -= dinheiro_para_sacar
        quantidade_de_saques -=1
        print(f"Saque de R$ {dinheiro_para_sacar} realizado com sucesso")
        historico_de_extrato += f"Saque de R$ {dinheiro_para_sacar}\n"
    return saldo,quantidade_de_saques,historico_de_extrato

def mostrar_extrato(saldo,historico_de_extrato):
    print(historico_de_extrato)
    print(f"Você possui R${saldo:.2f} na conta")

saldo = 0
quantidade_de_saques = 3
historico_de_extrato = ""

while True:

    opcao = input(menu)

    if opcao == 'd':
        saldo, historico_de_extrato = depositar_dinheiro(saldo,historico_de_extrato)

    elif opcao == 's':
        saldo, quantidade_de_saques,historico_de_extrato = sacar_dinheiro(saldo,quantidade_de_saques,historico_de_extrato)

    elif opcao == 'e':
        mostrar_extrato(saldo,historico_de_extrato)

    elif opcao == 'q':
        print('Obrigado por usar nosso programa, até breve')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')
