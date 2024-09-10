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

class Banco:
   def __init__(self):
        self.clientes = {}  # Dicionário para armazenar os clientes e suas contas

def criar_usuario(self, nome, cpf):
         if cpf in self.clientes:
            print("Usuário já existe!")
            return False
         self.clientes[cpf] = {'nome': nome, 'conta': None}
         print("Usuário criado com sucesso!")
         return True

def criar_conta(self, usuario):
        if cpf not in self.clientes:
            print("Usuário não encontrado.")
            return False
        if self.clientes[cpf]['conta']:
            print("Usuário já possui uma conta.")
            return False
        self.clientes[cpf]['conta'] = ContaBancaria()
        print("Conta criada com sucesso!")
        return True

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

    def visualizar_extrato(self):
        if not self.extrato:
          print ("Não há operações registradas na conta.")
        else:
          print("Extrato:\n", self.extrato)

 # Cria uma instância do banco
banco = Banco()

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
        cpf = input("Digite seu CPF: ")
        banco.criar_usuario(nome, cpf)
    elif opcao == "cc":
        cpf = input("Digite o CPF do cliente: ")
        banco.criar_conta(cpf)
        
        if opcao == 'd':
         cpf = input("Digite o CPF do cliente: ")
         valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            banco.depositar(cpf, valor)
        else:
            print("Valor inválido para depósito.")

    elif opcao == 's':
        cpf = input("Digite o CPF do cliente: ")
        valor = float(input("Digite o valor do saque: "))
        if valor > 0:
            banco.sacar(cpf, valor)
        else:
            print("Valor inválido para saque.")
    
    elif opcao == "e":
        cpf = input("Digite o CPF do cliente: ")
        if cpf in banco.clientes:
            conta = banco.clientes[cpf]['conta']
            if conta:
                conta.visualizar_extrato()
            else:
                print("Usuário não possui conta.")
        else:
            print("Usuário não encontrado.")
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