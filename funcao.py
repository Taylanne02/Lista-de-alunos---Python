def lerNotas(nomeArquivo):
    arquivo = open(nomeArquivo, 'r', encoding='utf8')
    dados = arquivo.read().strip()
    arquivo.close()

    if dados:
        return dados.splitlines()
    else:
        return []


def salvarDados(nomeArquivo, dados):
    with open(nomeArquivo, 'w', encoding='utf8') as arquivo:
        for dado in dados.values():
            arquivo.write(
                f"Nome: {dado['Nome']}\n"
                f"G1: {dado['G1']}\n"
                f"G2: {dado['G2']}\n"
                "-------------------\n"
                ""
            )