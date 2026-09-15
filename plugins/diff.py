import os
import difflib

SCHEMA = {
    "type": "function",
    "function": {
        "name": "diff_files",
        "description": (
            "Compara dois arquivos do projeto e mostra "
            "as diferenças entre eles."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file1": {
                    "type": "string",
                    "description": "Primeiro arquivo"
                },
                "file2": {
                    "type": "string",
                    "description": "Segundo arquivo"
                }
            },
            "required": ["file1", "file2"]
        }
    }
}


def caminho_seguro(base, caminho):

    alvo = os.path.abspath(
        os.path.join(
            base,
            caminho
        )
    )

    if not (
        alvo == base
        or alvo.startswith(base + os.sep)
    ):
        raise ValueError(
            "caminho fora do projeto"
        )

    return alvo


def executar(args: dict) -> str:

    base_dir = os.path.abspath(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )

    try:

        arquivo1 = caminho_seguro(
            base_dir,
            args["file1"]
        )

        arquivo2 = caminho_seguro(
            base_dir,
            args["file2"]
        )

    except Exception as erro:

        return f"erro: {erro}"

    if not os.path.isfile(arquivo1):
        return f"erro: arquivo não encontrado: {args['file1']}"

    if not os.path.isfile(arquivo2):
        return f"erro: arquivo não encontrado: {args['file2']}"

    try:

        with open(
            arquivo1,
            "r",
            encoding="utf-8",
            errors="replace"
        ) as f:
            linhas1 = f.readlines()

        with open(
            arquivo2,
            "r",
            encoding="utf-8",
            errors="replace"
        ) as f:
            linhas2 = f.readlines()

    except Exception as erro:

        return f"erro lendo arquivos: {erro}"

    relativo1 = os.path.relpath(
        arquivo1,
        base_dir
    )

    relativo2 = os.path.relpath(
        arquivo2,
        base_dir
    )

    diff = difflib.unified_diff(
        linhas1,
        linhas2,
        fromfile=relativo1,
        tofile=relativo2,
        lineterm=""
    )

    resultado = "\n".join(diff)

    if not resultado:

        return "Os arquivos são idênticos."

    return resultado