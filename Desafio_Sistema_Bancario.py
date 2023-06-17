import pandas as pd

menu = """
************* MENU *************
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
********************************
"""

saldo = 0
extrato = []
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(deposito):
    global saldo, extrato
    if deposito <= 0:
        print("Valor de depósito inválido!")
    else:
        saldo += deposito
        registro = {"Operação": "Depósito", "Valor": "R${:.2f}".format(deposito)}
        extrato.append(registro)
        print("Operação bem sucedida!")

def sacar(saque):
    global saldo, extrato, numero_saques
    
    if saque <= 0:
        print("\nATENÇÃO:\nValor de saque inválido!")
    elif saldo - saque < 0:
        print("\nATENÇÃO:\nSaldo insuficiente!")
    elif numero_saques >= LIMITE_SAQUES:
        print("\nATENÇÃO:\nVocê atingiu o limite máximo de saques diários!")
    elif saque > limite:
        print("\nATENÇÃO:\nLimite de saque excedido!")
    else:
        saldo -= saque
        numero_saques += 1
        registro = {"Operação": "Saque", "Valor": "R${:.2f}".format(saque)}
        extrato.append(registro)
        print("Operação bem sucedida!")

def ver_extrato(extrair):
    global saldo, extrato
    extrato = extrair
    df = pd.DataFrame(extrato)
    
    if df.empty:
        df = "Não há movimentações em sua conta"
        print(f"{df}\n")
    else:
        print(f"{df}\n")
        print(f"Seu saldo é: R${saldo:.2f}")
    

while True:
    print(menu)
    opcao = int(input("Opção: "))

    if opcao == 1:
        print("\n************ DEPÓSITO ************\n")
        deposito = int(input("Informe o valor a ser depositado (ex.: 1500): "))
        print("\n**********************************")
        depositar(deposito)

        menu_sair = int(input("\nDeseja voltar ao Menu[1] ou Sair[0]: "))
        if menu_sair == 0:
            print("\n****** Obrigado, até logo ******")
            break
        
    elif opcao == 2:
        if saldo <= 0:
            print("\nATENÇÃO:\nSeu saldo é insuficiente para realizar um saque!")
        else:
            print("\n************* SAQUE *************\n")
            saque = int(input("Informe o valor a ser sacado (ex.: 1500): "))
            print("\n*********************************")
            sacar(saque)
        
        menu_sair = int(input("\nDeseja voltar ao Menu[1] ou Sair[0]: "))  
        if menu_sair == 0:
            print("\n****** Obrigado, até logo ******")
            break

    elif opcao == 3:
        print("\n************ EXTRATO ************\n")
        ver_extrato(extrato)
        print("\n*********************************")

        menu_sair = int(input("\nDeseja voltar ao Menu[1] ou Sair[0]: "))
        if menu_sair == 0:
            print("\n****** Obrigado, até logo ******")
            break

    elif opcao == 0:
        print("\n****** Obrigado, até logo ******")
        break
        
    else:
        print("\nATENÇÃO:\nOperação inválida, por favor selecione uma opção válida!")