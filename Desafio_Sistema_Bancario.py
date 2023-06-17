import pandas as pd

menu = """
************* MENU *************\n
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
\n********************************
"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print(menu)

    opcao = int(input("Opção: "))

    if opcao == 1:
        print("\n************ DEPÓSITO ************\n")

        deposito = int(input("Informe o valor a ser depositado (ex.: 1500): "))
        
        print("\n**********************************")

        if deposito <= 0:
            print("Valor de depósito inválido!")
        else:
            saldo += deposito

            registro = {"Operação": "Depósito", "Valor": "R${:.2f}".format(deposito)}
            extrato.append(registro)
            
            print("Operação bem sucedida!")
            
            menu_sair = int(input("\nDeseja voltar ao Menu[1] ou Sair[0]: "))
            if menu_sair == 0:
                print("\nObrigado e até logo!")
                break

    elif opcao == 2:
        print("\n************* SAQUE *************\n")

        if saldo <= 0:
            print("Seu saldo é insuficiente para realizar um saque!")

            menu_sair = int(input("\nDeseja voltar ao Menu[1] ou Sair[0]: "))
            if menu_sair == 0:
                print("\nObrigado e até logo!")
                break

        elif numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite máximo de saques diários!")
            
            menu_sair = int(input("\nDeseja voltar ao Menu[1] ou Sair[0]: "))
            if menu_sair == 0:
                print("\nObrigado e até logo!")
                break

        else:
            saque = int(input("Informe o valor a ser sacado (ex.: 1500): "))

            print("\n*********************************")
            
            if saque <= 0:
                print("O valor de saque é inválido!")
                
            elif saque <= 0 or saque > limite:
                print("O valor de saque excede o limite!")
            
            else:
                if (saldo - saque) < 0:
                    print("Saldo insuficiente!")

                    menu_sair = int(input("\nDeseja voltar ao Menu[1] ou Sair[0]: "))
                    if menu_sair == 0:
                        print("\nObrigado e até logo!")
                        break

                else:
                    saldo -= saque
                    numero_saques += 1

                    registro = {"Operação": "Saque", "Valor": "R${:.2f}".format(saque)}
                    extrato.append(registro)

                    print("Operação bem sucedida!")

                    menu_sair = int(input("\nDeseja voltar ao Menu[1] ou Sair[0]: "))
                    if menu_sair == 0:
                        print("\nObrigado e até logo!")
                        break

    elif opcao == 3:
        df = pd.DataFrame(extrato)

        print("\n************ EXTRATO ************\n")
        print(f"{df}\n")
        print(f"Seu saldo é: R${saldo:.2f}")
        print("\n*********************************")

        menu_sair = int(input("\nDeseja voltar ao Menu[1] ou Sair[0]: "))
        if menu_sair == 0:
            print("\nObrigado e até logo!")
            break

    elif opcao == 0:
        print("\n********************************")
        print("Obrigado e até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")