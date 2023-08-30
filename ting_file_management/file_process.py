import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_text = txt_importer(path_file)

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_text),
        "linhas_do_arquivo": file_text,
    }

    if instance.contain(path_file):
        return

    instance.enqueue(file_data)
    sys.stdout.write(f"{file_data}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
