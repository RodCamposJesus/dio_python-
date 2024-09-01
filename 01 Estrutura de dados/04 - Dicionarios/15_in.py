contatos = {
    "guilherme@gmail.com": {"Nome":"Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"Nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"Nome": "Chappie","telefone": "3334-9871"},
    "melaine@gmail.com":{"Nome": "Melaine", "telefone": "3333-7766", "extra":{"a": 1}}
}


resultado =  "guilherme@gmail.com" in  contatos #true
print(resultado)

resultado =  "megui@gmail.com" in  contatos #false
print(resultado)

resultado = "idade" in contatos ["guilherme@gmail.com"] #false
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"] #True
print(resultado)