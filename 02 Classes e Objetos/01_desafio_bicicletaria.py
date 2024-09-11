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

    #def get_cor(self):
        #return self.cor
    
    #def __str__(self):
        #return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}"for chave, valor in self.__dict__.items()])}"
    

bike1 = Bicicleta("vermelha", "caloi", 2022, 600)
bike1.buzinar()
bike1.correr()
bike1.parar() 
print(bike1.cor, bike1.modelo, bike1.ano, bike1.valor)   

bike2 = Bicicleta("verde", "monark", 2000, 189)
print(bike2)
bike2.correr() #é a mesa coisa se eu fizer: Bicicleta.buzinar(bike2)