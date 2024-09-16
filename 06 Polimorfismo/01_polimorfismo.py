class Passaro:
 def voar(self):
  print("Voando...")

class Paradal(Passaro):
  def voar(self):
   return super().voar()
  

class Avestruz(Passaro):
 def voar(self):
  print("Avestruz não pode voar")


def plano_voo(obj):
  obj.voar()

#p1 = Paradal()
#p2 = Avestruz()

#plano_voo(p1)
#plano_voo(p2)
#resultado será o mesmo que chamando pela calsse diretamente

plano_voo(Paradal())
plano_voo(Avestruz())