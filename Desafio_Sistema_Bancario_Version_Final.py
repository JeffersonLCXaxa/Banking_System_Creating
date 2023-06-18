import pandas as pd


class ContaBancaria:
    def __init__(self, cpf, numero_conta, agencia):
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = 0
        self.extrato = []
        self.limite = 500
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.historico = Historico()

    def depositar(self, deposito):
        if deposito <= 0:
            print("Valor de depósito inválido!")
        else:
            self.saldo += deposito
            registro = {"Operação": "Depósito", "Valor": "R${:.2f}".format(deposito)}
            self.extrato.append(registro)
            self.historico.adicionar_transacao(registro)
            print("Operação bem sucedida!")

    def sacar(self, saque):
        if saque <= 0:
            print("\nATENÇÃO:\nValor de saque inválido!")
        elif self.saldo - saque < 0:
            print("\nATENÇÃO:\nSaldo insuficiente!")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("\nATENÇÃO:\nVocê atingiu o limite máximo de saques diários!")
        elif saque > self.limite:
            print("\nATENÇÃO:\nLimite de saque excedido!")
        else:
            self.saldo -= saque
            self.numero_saques += 1
            registro = {"Operação": "Saque", "Valor": "R${:.2f}".format(saque)}
            self.extrato.append(registro)
            self.historico.adicionar_transacao(registro)
            print("Operação bem sucedida!")

    def ver_extrato(self):
        df = pd.DataFrame(self.extrato)

        if df.empty:
            print("Não há movimentações em sua conta\n")
        else:
            print(df.to_string() + "\n")
            print(f"Seu saldo é: R${self.saldo:.2f}")


class Usuario:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class Banco:
    def __init__(self):
        self.AGENCIA_FIXA = "0001"
        self.contas = []
        self.usuarios = []

    def cadastrar_usuario(self):
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

        novo_usuario = Usuario(cpf, nome, data_nascimento, endereco)
        self.usuarios.append(novo_usuario)

    def cadastrar_conta_bancaria(self):
        cpf = input("Digite o CPF do usuário para cadastrar a conta: ")

        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                numero_conta = len(self.contas) + 1
                nova_conta = ContaBancaria(cpf, numero_conta, self.AGENCIA_FIXA)
                self.contas.append(nova_conta)
                print(f"Conta cadastrada com sucesso! Número da conta: {numero_conta}")
                return

        print("CPF não encontrado.")

    def iniciar(self):
        while True:
            print("""
************* HOME *************
         Seja bem-vindo!
        
Escolha uma opção:
[1] Acessar a sua conta
[2] Cadastrar uma conta

[0] Sair
********************************
""")
            opcao_home = int(input("Opção: "))

            if opcao_home == 1:
                conta_corrente = input("\n********* CONTA/AGÊNCIA *********\nConta corrente: ")
                agencia = input("Agência: ")
                print("\n********************************\n")

                conta_encontrada = False
                for conta in self.contas:
                    if self.AGENCIA_FIXA == agencia and conta.numero_conta == int(conta_corrente):
                        usuario = next((u for u in self.usuarios if u.cpf == conta.cpf), None)
                        if usuario:
                            conta_encontrada = True
                            nome_cliente = usuario.nome
                            conta_bancaria = conta
                            break

                if conta_encontrada:
                    while True:
                        print(f"Usuário: {nome_cliente}")
                        print("""
************* MENU *************
[1] Depósito
[2] Saque
[3] Extrato
[4] Histórico

[0] Sair
********************************
""")
                        opcao_menu = int(input("Opção: "))

                        if opcao_menu == 1:
                            print("\n************ DEPÓSITO ************\n")
                            deposito = float(input("Informe o valor a ser depositado (ex.: 1500): "))
                            print("\n**********************************")
                            conta_bancaria.depositar(deposito)

                            menu_sair = int(input("\nVoltar ao Menu[1] ou Sair[0]: "))
                            if menu_sair == 0:
                                print("\n****** Obrigado, até logo ******")
                                break

                        elif opcao_menu == 2:
                            if conta_bancaria.saldo <= 0:
                                print("\nATENÇÃO:\nSeu saldo é insuficiente para realizar um saque!")
                            else:
                                print("\n************* SAQUE *************\n")
                                saque = float(input("Informe o valor a ser sacado (ex.: 1500): "))
                                print("\n*********************************")
                                conta_bancaria.sacar(saque)

                            menu_sair = int(input("\nVoltar ao Menu[1] ou Sair[0]: "))
                            if menu_sair == 0:
                                print("\n****** Obrigado, até logo ******")
                                break

                        elif opcao_menu == 3:
                            print("\n************ EXTRATO ************\n")
                            conta_bancaria.ver_extrato()
                            print("\n*********************************")

                            menu_sair = int(input("\nVoltar ao Menu[1] ou Sair[0]: "))
                            if menu_sair == 0:
                                print("\n****** Obrigado, até logo ******")
                                break

                        elif opcao_menu == 4:
                            print("\n************ HISTÓRICO ************\n")
                            conta_bancaria.historico.exibir_historico()
                            print("\n***********************************")

                            menu_sair = int(input("\nVoltar ao Menu[1] ou Sair[0]: "))
                            if menu_sair == 0:
                                print("\n****** Obrigado, até logo ******")
                                break

                        elif opcao_menu == 0:
                            print("\n****** Obrigado, até logo ******")
                            break

                        else:
                            print("\nOpção inválida! Tente novamente.\n")

                else:
                    print("\nATENÇÃO:\nConta/Agência não encontrada!")

            elif opcao_home == 2:
                self.cadastrar_usuario()
                self.cadastrar_conta_bancaria()

            elif opcao_home == 0:
                print("\n****** Obrigado, até logo ******")
                break

            else:
                print("\nOpção inválida! Tente novamente.\n")


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def exibir_historico(self):
        df = pd.DataFrame(self.transacoes)

        if df.empty:
            print("Não há transações no histórico.")
        else:
            print(df.to_string(index=False))


banco = Banco()
banco.iniciar()
