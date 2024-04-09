from etl import ler_csv, filtrar_produtos_entregues, somar_valores_dos_produtos


PATH_ARQUIVO = "vendas.csv"

lista_de_produtos = ler_csv(PATH_ARQUIVO)
produtos_entregues = filtrar_produtos_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)

print(produtos_entregues)
print(valor_dos_produtos_entregues)