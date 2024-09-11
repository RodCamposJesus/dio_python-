class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plin, plin... ")

    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmm!")

        bike1 = Bicicleta("vermelha", "caloi", 2022, 600)
        bike1.buzinar()
        bike1.correr()
        bike1.parar()