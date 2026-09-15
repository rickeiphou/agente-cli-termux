import os


SCHEMA = {
    "type": "function",
    "function": {
        "name": "list_dir",
        "description": (
            "Lista os arquivos e pastas de um diretorio. "
            "Use '.' para o diretorio atual."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": (
                        "Caminho do diretorio. "
                        "Se vazio ou omitido, usa o "
                        "diretorio atual."
                    )
                }
            },
            "required": []
        }
    }
}


def executar(args: dict) -> str:

    # Se o modelo mandar:
    #
    # {"path": ""}
    #
    # usamos "." em vez de tentar os.listdir("").

    path = args.get("path") or "."

    try:

        items = []

        for name in sorted(os.listdir(path)):

            p = os.path.join(
                path,
                name
            )

            try:

                if os.path.isdir(p):

                    items.append(
                        f"[dir]  {name}/"
                    )

                else:

                    tamanho = os.path.getsize(p)

                    items.append(
                        f"[file] {name} "
                        f"({tamanho} bytes)"
                    )

            except OSError as e:

                items.append(
                    f"[?] {name} "
                    f"(erro ao consultar: {e})"
                )

        if not items:
            return "<diretorio vazio>"

        return "\n".join(items)

    except FileNotFoundError:

        return (
            f"erro ao listar {path}: "
            "diretorio nao encontrado"
        )

    except PermissionError:

        return (
            f"erro ao listar {path}: "
            "permissao negada"
        )

    except NotADirectoryError:

        return (
            f"erro ao listar {path}: "
            "o caminho nao e um diretorio"
        )

    except Exception as e:

        return (
            f"erro ao listar {path}: "
            f"{type(e).__name__}: {e}"
        )