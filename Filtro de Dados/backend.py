import csv

def get_registros(coluna, valor):

    registros = [
        line for line in dados
        if line.get(coluna.capitalize()) == valor.capitalize()
    ]
    return registros

dados = []

arquivo = "ProjetosPython/Filtro de Dados/dados.csv"
with open(arquivo) as file:
    data = csv.DictReader(file)
    for linha in data:
        dados.append(linha)

if __name__ == "__main__":
    log = get_registros(input("Coluna: "), input("Valor: "))
    [[print(f"{key}: {value}") for key, value in info.items()] for info in log]