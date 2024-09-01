contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna") #"Guilherme"
print(contato)

contato.setdefault("idade", 28) #28
print(contato) #{'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
