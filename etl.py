import csv

from typing import List


def ler_csv(nome_do_arquivo_csv: str) -> List[dict]:
    """
    Funcao que le um arquivo csv e retorna uma lista de dicionarios
    """
    with open(nome_do_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)
    

def filtrar_produtos_entregues(lista_produtos: List[dict]) -> List[dict]:
    """
    Funcao que filtra os produtos onde entrega = True
    """
    lista_com_produtos_filtrados = []
    for produto in lista_produtos:
        if produto.get("Entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados


def somar_valores_dos_produtos(lista_com_produtos_filtrados: List[dict]) -> int:
    """
    Funcao que filtra produtos onde entrega = True
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int( produto.get("Venda") )
    return valor_total

