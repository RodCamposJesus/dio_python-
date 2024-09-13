class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
     return f"{self.__class__.__name__}: {", ".join
     ([f"{chave}={valor}"for chave, valor in self.__dict__.items()])}"

        

class Mamifero(Animal):
    def __init__(self,cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

   

class Ave(Animal):
    def __init__(self,cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)# key args utilizado para utilizar os 
        #argumentos(parâmetros) da classe pai(dexamos nos 
        # nas classes "filhas" somente os #
        # args correspondes dessas classes.S)

class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self,cor_bico, cor_pelo, nro_patas):
        #print(Ornitorrinco.__mro__)#vai trazer a ordem de resolução
        #print(Ornitorrinco.mro()) #outr maneira de trazer a oerdem de resolução
        
        super().__init__(cor_pelo = cor_pelo, cor_bico = cor_bico, 
    nro_patas = nro_patas)
    

gato = Gato(nro_patas= 4, cor_pelo="preto", )
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2,cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)