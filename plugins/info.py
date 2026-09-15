import os
import platform
import sys

SCHEMA = {
    "type": "function",
    "function": {
        "name": "project_info",
        "description": (
            "Obtém informações seguras sobre o ambiente "
            "e a estrutura básica do projeto."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}


def executar(args: dict) -> str:

    base_dir = os.path.abspath(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )

    try:
        arquivos = os.listdir(base_dir)
    except Exception as erro:
        return f"erro listando projeto: {erro}"

    python_version = (
        f"{sys.version_info.major}."
        f"{sys.version_info.minor}."
        f"{sys.version_info.micro}"
    )

    diretorios = []
    arquivos_normais = []

    for item in sorted(arquivos):

        caminho = os.path.join(
            base_dir,
            item
        )

        if os.path.isdir(caminho):
            diretorios.append(item)
        else:
            arquivos_normais.append(item)

    return (
        f"Projeto: {base_dir}\n"
        f"Sistema: {platform.system()}\n"
        f"Arquitetura: {platform.machine()}\n"
        f"Python: {python_version}\n"
        f"Diretórios: {', '.join(diretorios) or '<nenhum>'}\n"
        f"Arquivos: {', '.join(arquivos_normais) or '<nenhum>'}"
    )