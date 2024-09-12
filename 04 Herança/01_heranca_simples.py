class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join
    ([f"{chave}={valor}"for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas) #super serve para invocar um método da classe pai
        self.carregado = carregado

        
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "ABC-1234",2)
carro = Carro("branco", "XBE-0098", 4)
caminhao = Caminhao("roxo", "GFD-8712", 8, True)

print(moto)
print(carro)
print(caminhao)