def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados
    print(f"Carro inserido com sucesso!{marca}/{modelo}/{ano}/{placa}")

#salvar_carro("Fiat","Palio", 1999, "ADC-1234")
#salvar_carro(marca="Fiat", modelo="Palio", ano=1999,placa="ABC-1234")

salvar_carro(**{"marca": "Fiat","modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
#nessa última, os **significam que estamos passando um dicionário para
#a função salvar_carro.