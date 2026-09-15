SCHEMA = {
    "type": "function",
    "function": {
        "name": "read_file",
        "description": "Le o conteudo de um arquivo.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Caminho do arquivo"}
            },
            "required": ["path"]
        }
    }
}

def executar(args: dict) -> str:
    path = args.get("path")
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            c = f.read()
        if len(c) > 6000:
            return c[:6000] + f"\n...<truncado, total {len(c)} chars>"
        return c if c else "<arquivo vazio>"
    except Exception as e:
        return f"erro ao ler {path}: {e}"
