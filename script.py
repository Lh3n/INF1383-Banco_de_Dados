arquivo_entrada = "entrada.txt"
arquivo_saida = "saida.txt"

# Indices das colunas desejadas no TXT
colunas_desejadas = [0, 1, 3, 5, 12, 17, 22]  # ajuste conforme seu TXT

# Lista de codigos de parlamentares
codigos_parlamentares = ["4132", "2776", "3919", "4160", "4483", "4155", "4368", "4011", "2919",
                         "3160", "4086", "3803", "4386", "4439"]


def formatar_valor(valor, eh_texto=False):
    # Formata valor para SQL: numeros sem aspas, strings entre aspas simples
    if eh_texto:
        # Escapar apostrofos internos
        valor = valor.replace("'", "''")
        return f"'{valor}'"
    else:
        # Trocar virgula decimal por ponto
        return valor.replace(",", ".")


with open(arquivo_entrada, "r", encoding="latin-1") as f_in, open(arquivo_saida, "w", encoding="utf-8") as f_out:
    for linha in f_in:
        campos = [c.strip('"') for c in linha.strip().split(";")]

        codigo = campos[3]  # codigo do parlamentar
        ano = int(campos[1])  # coluna do ano (ajuste se necessario)

        # Filtro 1: parlamentar valido
        # Filtro 2: ano >= 2023
        if codigo in codigos_parlamentares and ano >= 2023:

            # Selecionar apenas as colunas desejadas
            valores = [campos[i] for i in colunas_desejadas]

            # Formatar para SQL
            tupla_sql = (
                f"({formatar_valor(valores[0])}, "
                f"{formatar_valor(valores[1])}, "
                f"{formatar_valor(valores[2])}, "
                f"{formatar_valor(str(int(valores[3])))},"  # remove zeros a esquerda
                f" {formatar_valor(valores[4])}, "
                f"{formatar_valor(valores[5], eh_texto=True)}, "
                f"{formatar_valor(valores[6])}),\n"
            )

            f_out.write(tupla_sql)

print(f"Arquivo filtrado gerado com sucesso: {arquivo_saida}")
