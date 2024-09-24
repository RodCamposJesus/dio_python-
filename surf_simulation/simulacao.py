from surf_simulation import prancha
from surf_simulation import condicoes

def escolher_prancha(condicoes):
    pranchas = ["5'8", "5'11", "6'2"]

    tamanho_onda_num = float(condicoes.tamanho_onda)  # Converter para float

    if condicoes.tamanho_onda < 3:
        return pranchas[0] # Ondas pequenas: prancha menor
     
    elif condicoes.tamanho_onda < 5:
        return pranchas[1]  # Ondas médias: prancha intermediária
    
    else:
        return pranchas[2] # Ondas grandes: prancha maior
    
if __name__ == "__main__":
    tamanho_onda = input("Digite o tamanho das ondas (em pés): ")
    condicoes_atuais = condicoes.Condicoes(tamanho_onda)
    prancha_escolhida = escolher_prancha(condicoes_atuais)

print(f"\nCondições: Ondas de {condicoes_atuais.tamanho_onda} pés") 
print(f"Prancha escolhida: {prancha_escolhida}")