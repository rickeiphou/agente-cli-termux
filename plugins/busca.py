import os

SCHEMA = {
    "type": "function",
    "function": {
        "name": "search_codebase",
        "description": (
            "Procura um texto, função, classe, import ou padrão "
            "nos arquivos Python do projeto."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Texto que deve ser procurado"
                },
                "path": {
                    "type": "string",
                    "description": "Diretório ou arquivo onde procurar"
                }
            },
            "required": ["query", "path"]
        }
    }
}


def executar(args: dict) -> str:

    query = args["query"]
    caminho = args["path"]

    if not query.strip():
        return "erro: query vazia"

    if not caminho:
        caminho = "."

    base_dir = os.path.abspath(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )

    alvo = os.path.abspath(
        os.path.join(
            base_dir,
            caminho
        )
    )

    # Impede sair do projeto
    if not (
        alvo == base_dir
        or alvo.startswith(base_dir + os.sep)
    ):
        return "erro: caminho fora do projeto"

    if not os.path.exists(alvo):
        return f"erro: caminho não encontrado: {caminho}"

    resultados = []

    arquivos = []

    if os.path.isfile(alvo):

        arquivos.append(alvo)

    else:

        for raiz, diretorios, nomes in os.walk(alvo):

            # Evita lixo
            diretorios[:] = [
                d for d in diretorios
                if d not in {
                    ".git",
                    "__pycache__",
                    ".venv",
                    "venv"
                }
            ]

            for nome in nomes:

                if nome.endswith(".py"):

                    arquivos.append(
                        os.path.join(
                            raiz,
                            nome
                        )
                    )

    query_lower = query.lower()

    for arquivo in arquivos:

        try:

            with open(
                arquivo,
                "r",
                encoding="utf-8",
                errors="replace"
            ) as f:

                linhas = f.readlines()

        except Exception as erro:

            resultados.append(
                f"{arquivo}: erro lendo arquivo: {erro}"
            )

            continue

        for numero, linha in enumerate(
            linhas,
            1
        ):

            if query_lower in linha.lower():

                relativo = os.path.relpath(
                    arquivo,
                    base_dir
                )

                resultados.append(
                    f"{relativo}:{numero}: "
                    f"{linha.rstrip()}"
                )

                if len(resultados) >= 100:

                    return (
                        "\n".join(resultados)
                        + "\n\n[resultado limitado a 100 ocorrências]"
                    )

    if not resultados:

        return (
            f"Nenhuma ocorrência encontrada para: {query}"
        )

    return "\n".join(resultados)