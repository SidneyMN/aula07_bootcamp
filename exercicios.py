
# Vamos revisar funções adicionando type hints

lista_valores = [2.3, 1.5, 4.7, 5.5, 7.3, 7.9, 6.4, 1, 3, 7.9, 5]


# 1. Calcular Média de Valores em uma Lista
from typing import List

def calcular_media(valores: List[float]) -> float:
    return round(sum(valores) / len(valores), 2)
print(f"R. 1. : { calcular_media(lista_valores) } ")


# 2. Filtrar Dados Acima de um Limite
def filtrar_acima_de(valores: List[float], limite: float) -> float:
    resultado = []
    for i in valores:
        if i > limite:
            resultado.append(i)
        resultado.sort()
    return resultado
print(f"R. 2. : { filtrar_acima_de(lista_valores, 4) } ")


# 3. Contar Valores Únicos em uma Lista
def contar_valores_unicos(valores: List[float]) -> int:
    return len(set(valores))
print(f"R. 3. : {contar_valores_unicos(lista_valores)}")


# 4. Converter Celsius para Fahrenheit em uma Lista
def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperaturas_celsius]

temperaturas_celsius = [-4, -2, 0, 16, 19, 25, 32, 36, 45]
print(f"R. 4. : {celsius_para_fahrenheit(temperaturas_celsius)}")


# 5. Calcular Desvio Padrão de uma Lista
def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = round(sum((x - media) ** 2 for x in valores) / len(valores), 2)
    return variancia ** 0.5

print(f"R. 5. : {calcular_desvio_padrao(lista_valores)}")


# 6. Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

sequencia = [1, 3, 5, 7, 9]
print(f"R. 6. : {encontrar_valores_ausentes(sequencia)}")