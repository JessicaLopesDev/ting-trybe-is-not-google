def exists_word(word, instance):
    word = word.lower()
    occurrences = []

    for index in range(len(instance)):
        data = instance.search(index)
        result = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": []
        }

        for line_number, line in enumerate(data["linhas_do_arquivo"], start=1):
            if word in line.lower():
                result["ocorrencias"].append({"linha": line_number})

        if result["ocorrencias"]:
            occurrences.append(result)

    return occurrences


def search_by_word(word, instance):
    word = word.lower()
    occurrences = []

    for index in range(len(instance)):
        data = instance.search(index)
        result = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": []
        }

        for line_number, line in enumerate(data["linhas_do_arquivo"], start=1):
            if word in line.lower():
                result["ocorrencias"].append({"linha": line_number, "conteudo": line})

        if result["ocorrencias"]:
            occurrences.append(result)

    return occurrences
