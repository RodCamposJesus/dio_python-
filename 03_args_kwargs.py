#def exibir_poema(data_extenso, *args, **kwargs):(por baixo dos panos)
def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem, flush=True)

    
exibir_poema(
        "Quarta-Feira, 28 de agosto de 2024",
        "Zen of Python",
        "Beufiful is better than ugly.",
        "Explicit is better than implicit.",
        "Simple is better than complex.",
        "Complex is better than complicated.",
        "Flat is better than nested.",
        "Sparse is better than dense.",
        "Readability counts.",
        "Special cases aren't special enought to break the rules.",
        "Although practicality beats purity.",
        "Unless explicity silenced.",
        "In the face of ambiguity, refuse  the temptation to guess.",
        "There should be one-- and preferably only one-- obvious way to do it.",
        "Although  that way may not bebvious at first unless you're Duch. ",
        "Now is better than never.",
        "Although never is often better than *right* now.",
        "If the implementation is hard to explain, it's a bad idea.",
        "If implementation is easy to explain, it may be a good idea.",
        "Namespaces are one honking great idea -- let's  do more for those!",
        autor="Tim Peters",
        ano=1999,
        )