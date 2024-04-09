
print("Esse é o meu print")

valor_1 = 4
valor_2 = 6

valor_4 = 60
valor_5 = 43

def soma(valor_1_para_somar: float, valor_2_para_somar: float) -> float:
    """
    Uma funcao simples de soma de valores do tipo float que retorna float
    """
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma


valor_3 = soma(valor_1, valor_2)
print(valor_3)

valor_6 = soma(valor_4, valor_5)
print(valor_6)