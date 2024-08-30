def menu():
    saldo = 0
    saques_hoje = 0
    historico = []

    while True:
        print("Olá seja bem vindo! Por favor escolha uma oção:")
        print("1. Saque")
        print("2. Extrato")
        print("3. Depósito")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")
        if opcao == "1":
            if saques_hoje >= 3:
                print("Você atingiu o seu limite de máximo de saques diários.")
            else:
                valor = float(input("Digite o valor a ser sacado: "))
                if valor <= 500 and valor <= saldo:
                    saldo -= valor
                    saques_hoje += 1
                    historico.append(f"Saque de R$ {valor:.2f}")
                    print(f"Saque {valor:.2f} realizado com sucesso")
                elif valor > 500:
                    print("Valor de saque excede o limit diário.")
                else:
                    print("Saldo insuficiente")
        if opcao == "2":
            print("Extrato:")
            print(f"Extrato atual: R$ {saldo:.2f}")
            print("Histórico de transações: ")
            for transacao in historico:
                print(transacao)
        elif opcao == "3":
            valor = float(input("Digite o valor para ser depositado: "))
            if valor > 0:  # Verifica se o valor é positivo
                saldo += valor
                historico.append(f"Depósito de R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso. ")
            else:
                print("Valor de depósito inválido. Por favor, digite um valor positivo.")
            
        if opcao == "4":
          print("Obrigado por utilizar os nosso serviços. ")
        break
    else:
        print("Opção inválida. Por favor, digite um número entre 1 e 4.")

menu()

            