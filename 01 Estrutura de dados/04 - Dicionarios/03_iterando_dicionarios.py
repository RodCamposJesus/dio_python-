contatos = {
    "guilherme@gmail.com": {"Nome":"Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"Nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"Nome": "Chappie","telefone": "3334-9871"},
    "melaine@gmail.com":{"Nome": "Melaine", "telefone": "3333-7766", "extra":{"a": 1}}
}

#for chave in contatos:
    #print(chave, contatos[chave])

    #print("=" * 100)

for chave, valor in contatos.items():
        print(chave, valor)