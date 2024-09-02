menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

#valor = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu) 

    if opcao =="d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
            print("Depósito efetuado com sucesso!")
    
            print(f"Valor depositado foi de R$ {valor: .2f}")


        else:
            print("Operação falhou! Insira um valor correto!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, por favor verifique o seu saldo! ")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o seu limite. ")

        elif excedeu_saques:
            print("Operação falhou! Você atingiou o limite de sques diários!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1
       
            print(f"Foi sacado o valor de R$ {valor: .2f}")
        
        else:
            print("Operação falhou, o valor informado é invalido!")

    elif opcao =="e":
        print("\n===============EXTRATO===============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("=======================================")

    elif opcao == "q":
     break

    else:
        print("Operação inválida, por favor selecione novamnete a operação desejada")
            