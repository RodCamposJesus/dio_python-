#menu = """

#[d] Depositar
#[s] Sacar
#[e] Extrato
#[q] Sair

#=> """

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


    def criar_usuario(self, nome, cpf):
        usuario = Cliente(nome, cpf)
        return usuario
    
    def criar_conta(self, usuario):
        return ContaBancaria(usuario)

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        if valor > self.limite:
            print("Limite excedido.")
            return False
        if self.numero_saques >= self.LIMITE_SAQUES:
            print("Número máximo de saques excedido.")
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
        
    def visualisar_extrato(self):
        print("Extrato:\n", self.extrato)


    
    cliente_atual = None
    conta_atual = None
    
    
  

    
while True:
    print("""
    [cu] Criar usuário
    [cc] Criar conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """)
   

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "cu":
        nome = input("Digite seu nome: ")
        # ... (criar usuário)
        conta_atual = ContaBancaria()
        print(f"Conta criada com sucesso para {nome}!")

    elif opcao == 'd':
        if conta_atual is not None:
            valor = float(input("Digite o valor do depósito: "))
            conta_atual.depositar(valor)
        else:
            print("Você precisa criar uma conta antes de realizar operações.")


    if opcao == 'd':
        valor = float(input("Digite o valor do depósito: "))
        conta_atual.depositar(valor)
    elif opcao == 's':
        valor = float(input("Digite o valor do saque: "))
        conta_atual.sacar(valor)
    elif opcao == 'e':
        conta_atual.visualizar_extrato()


    elif opcao == 'q':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")

        
        
    

# ... (restante do código)
        
        
        
        
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