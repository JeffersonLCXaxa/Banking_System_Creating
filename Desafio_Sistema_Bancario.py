import pandas as pd

home = """
************* HOME *************
         Seja bem-vindo!
        
Escolha uma opção:
[1] Acessar a sua conta
[2] Cadastrar uma conta

[0] Sair
********************************
"""

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
AGENCIA_FIXA = "0001"
contas = []
usuarios = []


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


def ver_extrato():
    global saldo, extrato
    df = pd.DataFrame(extrato)

    if df.empty:
        print("Não há movimentações em sua conta\n")
    else:
        print(df.to_string(index=False) + "\n")
        print(f"Seu saldo é: R${saldo:.2f}")


def cadastrar_usuario():
    cpf = input("CPF: ")
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento [ex.: 01/01/1990]: ")

    print("Para seu endereço, informe:")
    logradouro = input("Logradouro: ")
    numero_casa = input("Nº: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")
    estado = input("Estado: ")

    endereco = f"{logradouro}, {numero_casa} - {bairro} - {cidade}/{uf} {estado}"

    novo_usuario = {
        "Nome": nome,
        "Data de Nascimento": data_nascimento,
        "CPF": cpf,
        "Endereço": endereco
    }

    usuarios.append(novo_usuario)


def cadastrar_conta_bancaria():
    global contas, usuarios
    print("\n********* CONFIRMAÇÃO *********\n")
    cpf = input("Digite o CPF do usuário para cadastrar a conta: ")
    print("\n*******************************\n")
    numero_conta = len(contas) + 1

    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            conta = {
                "CPF": cpf,
                "Número da Conta": numero_conta,
                "Agência": AGENCIA_FIXA
            }
            contas.append(conta)
            print(f"Conta cadastrada com sucesso! Número da conta: {numero_conta}")
            return

    print("CPF não encontrado.")

while True:
    print(home)
    opcao_home = int(input("Opção: "))

    if opcao_home == 1:
        print("\n********* CONTA/AGÊNCIA *********\n")
        conta_corrente = input("Conta corrente: ")
        agencia = input("Agência: ")
        print("\n********************************\n")

        conta_encontrada = False
        for conta in contas:
            if AGENCIA_FIXA == agencia and conta["Número da Conta"] == int(conta_corrente):
                for cliente in usuarios:
                    if cliente["CPF"] == conta["CPF"]:
                        conta_encontrada = True
                        nome_cliente = cliente["Nome"]
                        break
        
        if conta_encontrada:
            while True:
                print(f"Usuário: {nome_cliente}")
                print(menu)
                opcao_menu = int(input("Opção: "))

                if opcao_menu == 1:
                    print("\n************ DEPÓSITO ************\n")
                    deposito = int(input("Informe o valor a ser depositado (ex.: 1500): "))
                    print("\n**********************************")
                    depositar(deposito)

                    menu_sair = int(input("\nVoltar ao Menu[1] ou Sair[0]: "))
                    if menu_sair == 0:
                        print("\n****** Obrigado, até logo ******")
                        break

                elif opcao_menu == 2:
                    if saldo <= 0:
                        print("\nATENÇÃO:\nSeu saldo é insuficiente para realizar um saque!")
                    else:
                        print("\n************* SAQUE *************\n")
                        saque = int(input("Informe o valor a ser sacado (ex.: 1500): "))
                        print("\n*********************************")
                        sacar(saque)

                    menu_sair = int(input("\nVoltar ao Menu[1] ou Sair[0]: "))
                    if menu_sair == 0:
                        print("\n****** Obrigado, até logo ******")
                        break

                elif opcao_menu == 3:
                    print("\n************ EXTRATO ************\n")
                    ver_extrato()
                    print("\n*********************************")

                    menu_sair = int(input("\nVoltar ao Menu[1] ou Sair[0]: "))
                    if menu_sair == 0:
                        print("\n****** Obrigado, até logo ******")
                        break

                elif opcao_menu == 0:
                    print("\n****** Obrigado, até logo ******")
                    break

                else:
                    print("\nATENÇÃO:\nOpção inválida, por favor selecione uma alternativa válida!")

        else:
            print("\nConta corrente ou agência não encontrada!")

            home_sair = int(input("\nVoltar à página principal[1] ou Sair[0]: "))
            if home_sair == 0:
                print("\n****** Obrigado, até logo ******")
                break

    elif opcao_home == 2:
        print("\n*********** CADASTRO ***********\n")
        cadastrar_usuario()
        cadastrar_conta_bancaria()
        print("\n********************************\n")
        print("Usuário cadastrado com sucesso!\n")
        print(f"Sua conta corrente é: {contas[-1]['Número da Conta']}\nSua agência é: {contas[-1]['Agência']}")
        print("\n********************************\n")

        home_sair = int(input("\nVoltar à página principal[1] ou Sair[0]: "))
        if home_sair == 0:
            print("\n****** Obrigado, até logo ******")
            break

    elif opcao_home == 0:
        print("\n****** Obrigado, até logo ******")
        break

    else:
        print("\nATENÇÃO:\nOpção inválida, por favor selecione uma alternativa válida!")
