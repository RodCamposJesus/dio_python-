contatos = {"guilherme@gmail.com":{"nome": "Guilherme", "telefone": "3333-2221"}}

#contatos["chave"]#keyError

resultado = contatos.get("chave", {}) #none
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
    
)#{'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)