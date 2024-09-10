import random
class Banco:
    def __init__(self):
        self.clientes = {}

    def criar_usuario(self, nome, cpf):
        if cpf in self.clientes:
            print("Usuário já existe!")
            return False
        self.clientes[cpf] = {'nome': nome, 'conta': None}
        print("Usuário criado com sucesso!")
        return True

    def criar_conta_corrente(self, cpf):
        if cpf not in self.clientes:
            print("Usuário não encontrado.")
            return False
        if self.clientes[cpf]['conta']:
            print("Usuário já possui uma conta.")
            return False
        numero_conta = random.randint(100000000, 999999999)
        self.clientes[cpf]['conta'] = ContaCorrente(numero_conta)
        print("Conta corrente criada com sucesso!")
        print(f"Número da conta: {self.clientes[cpf]['conta'].numero_conta}")
        return True

class ContaCorrente:
    def __init__(self, numero_conta, saldo=0, limite=500):
        self.numero_conta = numero_conta
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
        print("Extrato:\n", self.extrato)

def obter_conta(banco, cpf):
    if cpf in banco.clientes:
        conta = banco.clientes[cpf]['conta']
        if conta:
            return conta
        else:
            print("Usuário não possui conta. Crie uma conta para realizar esta operação.")
    else:
        print("Usuário não encontrado.")
    return None

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
        banco.criar_conta_corrente(cpf)
    elif opcao == "d":
        cpf = input("Digite o CPF do cliente: ")
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            conta = obter_conta(banco, cpf)
            if conta:
                conta.depositar(valor)
        else:
            print("Valor inválido para depósito.")
    elif opcao == "s":
        cpf = input("Digite o CPF do cliente: ")
        valor = float(input("Digite o valor do saque: "))
        if valor > 0:
            conta = obter_conta(banco, cpf)
            if conta:
                conta.sacar(valor)
        else:
            print("Valor inválido para saque.")
    elif opcao == "e":
        cpf = input("Digite o CPF do cliente: ")
        conta = obter_conta(banco, cpf)
        if conta:
            conta.visualizar_extrato()
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")