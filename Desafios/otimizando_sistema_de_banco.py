menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """




saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaBancaria:
    def __init__(self, saldo=0, limite=500):
        self.saldo = saldo
        self.limite = limite
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_numero_de_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return False

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            return False

        if excedeu_numero_de_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            return False

        self.saldo -= valor
        self.extrato += f"Saque: R$ {valor:.2f}\n"
        self.numero_saques += 1
        return True

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor: .2f}\n"
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

def visualizar_extrato():
    # Implementação da função para visualizar o extrato
    pass

def criar_cliente():
    # Implementação da função para criar um cliente
    pass

def criar_conta_corrente():
    # Implementação da função para criar uma conta corrente
    pass



while True:
    opcao = input(menu)

    if opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor > 0:
            if sacar(valor):
                print("Saque realizado com sucesso.")
    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            depositar(valor)
            print("Depósito realizado com sucesso.")
    elif opcao == "e":
        visualizar_extrato()
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

        
        
        
        
        
        #código
        #elif opcao == "s":
        #valor = float(input("Informe o valor do saque: "))

        #else:
            #print("Operação falhou! O valor informado é inválido.")

        #elif opcao == "s":
        #valor = float(input("Informe o valor do saque: "))

        #excedeu_saldo = valor > saldo

        #excedeu_limite = valor > limite

        #excedeu_saques = numero_saques >= LIMITE_SAQUES

        #if excedeu_saldo:
            #print("Operação falhou! Você não tem saldo suficiente.")

        #elif excedeu_limite:
           # print("Operação falhou! O valor do saque excede o limite.")

        #elif excedeu_saques:
           # print("Operação falhou! Número máximo de saques excedido.")

        #elif valor > 0:
            #saldo -= valor
            #extrato += f"Saque: R$ {valor:.2f}\n"
            #numero_saques += 1

        #else:
            #print("Operação falhou! O valor informado é inválido.")

    #elif opcao == "e":
        #print("\n================ EXTRATO ================")
        #print("Não foram realizadas movimentações." if not extrato else extrato)
        #print(f"\nSaldo: R$ {saldo:.2f}")
        #print("==========================================")

    #elif opcao == "q":
        #break

    #else:
        #print("Operação inválida, por favor selecione novamente a operação desejada.")