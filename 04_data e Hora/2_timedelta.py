from datetime import datetime,timedelta, time, date

tipo_carro = "M"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou:{data_atual}e ficará pronto as {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(print(f"O carro chegou:{data_atual}e ficará pronto as {data_estimada}"))
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(print(f"O carro chegou:{data_atual}e ficará pronto as {data_estimada}"))

    
    print(date.today() - timedelta(days=1))

    resultado = datetime(2024, 9, 2, 4,16,20) - timedelta(hours=1)
    print(resultado.time())