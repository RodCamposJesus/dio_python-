lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(id(l2), id(lista)) #aparecem em estâncias distintas

l2[0] = 2
print(l2)
print(lista)

