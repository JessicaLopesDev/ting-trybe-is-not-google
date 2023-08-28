import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file, "r") as file:
            return file.read().split('\n')

    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

# Usando duas formas de exibir mensagem na stderr para fins de pesquisa futura
